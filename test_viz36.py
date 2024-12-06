import re
import json
import os
import uuid 
from neo4j import GraphDatabase
from fast_graphrag import GraphRAG

import logging

# Set up logging for fast_graphrag
#logging.basicConfig(level=logging.DEBUG)
#logger = logging.getLogger("fast_graphrag")

# Get Neo4j connection details from environment variables
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")  # Default to "neo4j" if the environment variable is not set
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")  # Default to "password" if the environment variable is not set

# Neo4j driver initialization
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# GraphRAG configuration
DOMAIN = "As a code review expert, your role will be to carefully examine the code for potential security flaws. Focus on how the input can be passed to function or method, the input location, sanitization, tainting, control and dataflow"

EXAMPLE_QUERIES = [
    "What are the functions used?",
    "What are the objects and methods used?",
    "Which functions take input from the user?",
    "What are the sinks?",
    "What is the control flow?",
    "What is the data flow?",
    "Which vulnerable functions are used?",
    "Which inputs are not tainted after reaching the sink?",
    "What is the filename?",
    "What is the linenumber?",
]
ENTITY_TYPES = ["Type", "Category", "Filename", "Linenumber", "Input", "Function", "Object", "Method", "Tainted", "Untainted", "Sink"]

# Initialize GraphRAG
grag = GraphRAG(
    working_dir="./test",
    domain=DOMAIN,
    example_queries="\n".join(EXAMPLE_QUERIES),
    entity_types=ENTITY_TYPES,
)

def initialize_database():
    """
    Initializes the Neo4j database, creating constraints and setting up a clean environment.
    """
    try:
        with driver.session() as session:
            session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (n:Entity) REQUIRE n.id IS UNIQUE")
            print("Database initialized with constraints.")
    except Exception as e:
        print(f"Error initializing the database: {e}")
def clear_database():
    """
    Deletes all nodes and relationships in the database.
    """
    try:
        with driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
            print("Database cleared.")
    except Exception as e:
        print(f"Error clearing the database: {e}")

def test_connection():
    """
    Tests the Neo4j connection by running a simple query.
    """
    try:
        with driver.session() as session:
            result = session.run("RETURN 'Connection Successful' AS message")
            for record in result:
                print(record["message"])
    except Exception as e:
        print(f"Connection test failed: {e}")

def parse_plain_text_nodes(response, filename):
    """
    Parses plain-text responses to extract nodes, accommodating multiple formats.
    """
    nodes = []
    lines = response.strip().split("\n")
    for line_num, line in enumerate(lines, start=1):  # Adding line number from the file
        try:
            if "-" in line:
                entity_id = str(uuid.uuid4()) 
                main_part = line.split("-", 1)  # Split at the first '-'
                entity_name = main_part[0].split(".")[1].strip()  # Extract the entity name
                entity_type = main_part[1].split(":")[0].strip() if "Description:" in main_part[1] else main_part[1].strip()
                
                # Add Filename and Linenumber as entities
                nodes.append({
                    "id": entity_id, 
                    "type": entity_name, 
                    "category": entity_type,
                    "linenumber": line_num,  # Add the line number here
                    "filename": filename  # Ensure filename is passed correctly here
                })
        except Exception as e:
            print(f"Error parsing line: {line}, Error: {e}")
    return nodes

def parse_plain_text_edges(response, filename="Unknown"):
    """
    Parses plain-text edges from the given response.
    Extracts relationships with source, target, description, and location (line number, filename).
    Default values are used if line number or filename is missing.
    """
    edges = []
    # Pattern to capture Source, Target, Description, and Location (Line and Filename)
    pattern = r"Source:\s*(.*?)\s*-*\s*Target:\s*(.*?)\s*-*\s*Description:\s*(.*?)\s*-*\s*Location:\s*(line \d+),\s*filename:\s*(\S+)"
    
    matches = re.findall(pattern, response)
    
    for match in matches:
        source, target, description, line_number, file_name = match
        
        # Check if filename is parsed correctly
        # Print parsed edge for debugging
        print(f"Parsed Edge: {source.strip()} -> {target.strip()} with filename: {file_name} on line {line_number}")
        
        # Build the edge response in the desired format
        edge = {
            "Function": source.strip(),
            "Filename": file_name,  # Ensure the filename is passed here
            "Line Number": line_number.strip(),  # Set the line number
            "Input": target.strip(),  # Set the target as user input
        }
        edges.append(edge)
    
    return edges

def clean_node_format(node):
    """Clean and normalize node attributes."""
    node['type'] = re.sub(r'^\*\*|\*\*$', '', node.get('type', '')).strip()
    node['category'] = re.sub(r'^\*\*|\*\*$', '', node.get('category', '')).strip()
    node['Linenumber'] = node.get('Linenumber') if node.get('Linenumber') is not None else "Unknown"
    node['Filename'] = node.get('Filename') if node.get('Filename') is not None else "Unknown"
    return node

def parse_plain_text_edges(response, filename="Unknown"):
    """
    Parses plain-text edges from the given response.
    Extracts relationships with source, target, description, and location (line number, filename).
    Default values are used if line number or filename is missing.
    """
    edges = []
    # Pattern to capture Source, Target, Description, and Location (Line and Filename)
    pattern = r"Source:\s*(.*?)\s*-*\s*Target:\s*(.*?)\s*-*\s*Description:\s*(.*?)\s*-*\s*Location:\s*(line \d+),\s*filename:\s*(\S+)"
    
    matches = re.findall(pattern, response)
    
    for match in matches:
        source, target, description, line_number, file_name = match
        

        # Print parsed edge for debugging
        print(f"Parsed Edge: {source.strip()} -> {target.strip()} with filename: {file_name} on line {line_number}")
        
        # Build the edge response in the desired format
        edge = {
            "Function": source.strip(),
            "Filename": file_name,  # Ensure the filename is passed here
            "Line Number": line_number.strip(),  # Set the line number
            "Input": target.strip(),  # Set the target as user input
        }
        edges.append(edge)
    
    return edges

def extract_graph_data(grag, filename="Unknown"):
    """
    Extracts and processes graph data from GraphRAG.
    Handles JSON and plain-text responses with enhanced cleaning.
    """
    try:
        print("Querying for nodes...")
        node_response = grag.query("List all entities and their types.")
        #print("Raw Node Response (Full):")
        #print(node_response.response)  # Print raw response
        nodes = []
        try:
            nodes = json.loads(node_response.response)
        except json.JSONDecodeError:
            print("Node response is not JSON formatted. Attempting plain-text parsing.")
            nodes = parse_plain_text_nodes(node_response.response, filename=filename)  # Pass filename here
        nodes = [clean_node_format(node) for node in nodes]  # Clean each node
        #print("Cleaned Nodes:", nodes)

        #print("Querying for edges...")
        #edge_response = grag.query("List all relationships between entities with filename and linenumber which are functions and get input from user and are vulnerable to attacks and nodes")
        #print("Raw Edge Response (Full):")
        #print(edge_response.response)  # Print raw response
        edges = []
        try:
            edges = json.loads(edge_response.response)
        except json.JSONDecodeError:
            print("Edge response is not JSON formatted. Attempting plain-text parsing.")
            edges = parse_plain_text_edges(edge_response.response, filename=filename)  # Pass filename here
        #print("Cleaned Edges:", edges)

        return nodes, edges
    except Exception as e:
        print(f"Error querying GraphRAG: {e}")
        return [], []

def clean_edge_format(edge):
    """Clean and normalize edge attributes."""
    edge['source'] = re.sub(r'^\*\*|\*\*$', '', edge.get('source', '')).strip()
    edge['target'] = re.sub(r'^\*\*|\*\*$', '', edge.get('target', '')).split(':')[0].strip()  # Extract node name before colon
    edge['type'] = edge.get('type', '').strip()
    return edge

def push_to_neo4j(nodes, edges):
    """
    Pushes the graph data (nodes and edges) to Neo4j for visualization.
    """
    try:
        with driver.session() as session:
            # Insert nodes with line_number and filename
            for node in nodes:
                query = """
                MERGE (n:Entity {id: $id, type: $type, category: $category, Linenumber: $line_number, Filename: $filename})
                """
                session.run(query, id=node.get("id"), 
                            type=node.get("type"), 
                            category=node.get("category"), 
                            line_number=node.get("Linenumber", "Unknown"),  # Default to 'Unknown' if line_number is None
                            filename=node.get("Filename", "Unknown"))  # Default to 'Unknown' if filename is None

            # Insert edges with line_number and filename
            for edge in edges:
                query = """
                MATCH (a:Entity {id: $source}), (b:Entity {id: $target})
                MERGE (a)-[:RELATED_TO {type: $type, Linenumber: $line_number, Filename: $filename}]->(b)
                """
                session.run(query, source=edge.get("source"), 
                            target=edge.get("target"), 
                            type=edge.get("type"),
                            line_number=edge.get("Linenumber", "Unknown"),  # Default to 'Unknown' if line_number is None
                            filename=edge.get("Filename", "Unknown"))  # Default to 'Unknown' if filename is None

        print("Graph data successfully pushed to Neo4j.")
    except Exception as e:
        print(f"Error pushing data to Neo4j: {e}")
# Example execution
if __name__ == "__main__":
    # Test connection to Neo4j
    test_connection()

    # Clear existing database content
    clear_database()

    # Initialize the database
    initialize_database()

    # Process the directory containing the source files
    directory_path = "../badcode/"  # Update this to your directory

    for dirpath, dirnames, filenames in os.walk(directory_path):
      for filename in filenames:
        print(filename)
        file_path = os.path.join(dirpath, filename)  # Get the full path to the file
        if os.path.isfile(file_path):  # Ensure it's a file, not a directory
            try:
                with open(file_path, encoding="utf-8") as f:
                    content = f.read()
                    grag.insert(content)
            except UnicodeDecodeError:
                print(f"Skipping {file_path} due to encoding issues.")
                continue
            nodes, edges = extract_graph_data(grag, filename)  # Pass filename during extraction
            print(f"Final Nodes: {nodes}")
            print(f"Final Edges: {edges}")
            push_to_neo4j(nodes, edges)



print(grag.query("List relationships between entities that involve functions, get input from users, and are vulnerable to attacks, along with the corresponding file names and line numbers").response)


