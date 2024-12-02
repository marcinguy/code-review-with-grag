import asyncio
import os
import openai
from typing import Any, Dict, List, Tuple, Optional
import pandas as pd
from tqdm import tqdm
from neo4j import GraphDatabase
from langchain.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain_community.graphs import Neo4jGraph
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import OpenAI  # Import OpenAI from Langchain

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

# Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")  # Use OpenAI API key


# Set up Neo4j connection
class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
        print("Connection closed")

    def reset_database(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
        print("Database reset successfully!")

    def add_document(self, documents: list):
        self.driver.add_graph_documents(documents)

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters or {})
            return [record for record in result]

# Connect to Neo4j
uri = "bolt://localhost:7687"
user = "neo4j"
password = "password"
conn = Neo4jConnection(uri, user, password)

# Define async function to handle processing
async def main():
    # Read PHP file
    with open('code.php', 'r') as file:
      code = file.read()

    # Parse PHP code to structured data
    data = []
    for line in code:
      if '=' in line:
        key, value = line.strip().split('=', 1)
        data.append([key, value])

    # Convert the structured data into a DataFrame
    df = pd.DataFrame(data, columns=['Key', 'Value'])
    code = df


    # Reset database to ensure it's empty
    conn.reset_database()

    # Initialize OpenAI LLM (using Langchain's OpenAI class)
    llm = OpenAI(openai_api_key=openai.api_key)

    # Initialize the LLM transformer
    llm_transformer = LLMGraphTransformer(
        llm=llm,
    )

    df_sample = code

    documents = []
    for _, row in tqdm(df_sample.iterrows(),
                       total=len(df_sample),
                       desc="Creating documents",
                       position=0,
                       leave=True):
        try:
            # Format text with proper line breaks
            text = ""
            for col in df.columns:
                text += f"{col}: {row[col]}\n"
            documents.append(Document(page_content=text))
        except KeyError as e:
            tqdm.write(f"Missing column: {e}")
        except Exception as e:
            tqdm.write(f"Error processing row: {e}")

    # Convert documents to graph format
    graph_documents = await llm_transformer.aconvert_to_graph_documents(documents)
    print(f"Nodes: {graph_documents[0].nodes}")
    print(f"Relationships: {graph_documents[0].relationships}")

    # Add graph documents to Neo4j
    graph = Neo4jGraph(url=uri, username=user, password=password, enhanced_schema=True)
    graph.add_graph_documents(graph_documents)

# Entry point to run the async function
if __name__ == "__main__":
    asyncio.run(main())

