import json
"""
    File that holds helper function to load/process data and files
"""
# Function to load json files
def read_json(json_file):
    # read JSON and return data as a dictionary
    with open(json_file, 'r') as jsonfile:
        config_data = json.load(jsonfile)
    return config_data


# Helper function to process cypher output to cleaner format
def process_cypher_output(query_results):
    """
    Processes a list of neo4j.Record objects, extracting and formatting
    the data based on available keys in each Record. Handles cases where
    the data includes lists by converting all elements to strings.

    :param results: List of neo4j.Record objects.
    :return: A string representing the extracted data, formatted for display.
    """
    if not query_results:
        return "MoBot: No results found."
    # Initialize a dictionary to hold the data extracted from each record.
    processed_data = {}
    for record in query_results:
        for key in record.keys():
            # Ensure the key exists in the dictionary and initialize if not.
            if key not in processed_data:
                processed_data[key] = []
            value = record[key]
            # Check if the value is a list and convert elements to strings if so.
            if isinstance(value, list):
                value = [str(element) for element in value]
            # Append the possibly converted value to the list under its key.
            processed_data[key].append(value)
    # Format the extracted data for display.
    formatted_responses = []
    for key, values in processed_data.items():
        # Convert all elements to strings, handling both flat and nested lists.
        formatted_values = [
            ", ".join(str(item) for item in value) if isinstance(value, list) else str(value) 
            for value in values
        ]
        formatted_response = f"{key}: " + ", ".join(formatted_values)
        formatted_responses.append(formatted_response)
    return "\n".join(formatted_responses), processed_data
