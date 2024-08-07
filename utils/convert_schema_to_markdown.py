import json
import os
import sys
import argparse

def json_to_markdown(json_data):
    markdown = f"# {json_data['schema']}[^1]\n\n"
    markdown += "[^1]: This markdown file is auto-generated."
    markdown += f"{json_data['description']}\n\n"
    markdown += f"## Version: {json_data['version']}\n\n"

    for table in json_data['tables']:
        markdown += f"### {table['label']}\n\n"
        markdown += f"{table['description']}\n\n"
        markdown += "| Property                | Description                                               | Type   |\n"
        markdown += "|-------------------------|-----------------------------------------------------------|--------|\n"

        for prop, details in table['properties'].items():
            markdown += f"| {prop.ljust(24)} | {details['description'].ljust(57)} | {details['type']} |\n"

        markdown += "\n"

    return markdown

def read_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def write_markdown_file(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)

def main(schema_name, action_flag):
    base_path = os.path.join('schemas', schema_name)
    json_filepath = os.path.join(base_path, 'schema.json')
    
    # Determine markdown file path based on action_flag presence
    markdown_filepath = os.path.join(base_path, 'SCHEMA_TEMP.md') if action_flag else os.path.join(base_path, 'SCHEMA.md')

    # Print paths for debugging
    print(f"JSON file path: {json_filepath}")
    print(f"Markdown file path: {markdown_filepath}")

    # Read JSON schema
    try:
        json_data = read_json_file(json_filepath)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        sys.exit(1)

    # Convert JSON to Markdown
    markdown_content = json_to_markdown(json_data)

    # Write Markdown to file
    try:
        write_markdown_file(markdown_filepath, markdown_content)
    except Exception as e:
        print(f"Error writing Markdown file: {e}")
        sys.exit(1)

    print("Markdown file created successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON schema to Markdown.")
    parser.add_argument("schema_name", help="Name of the schema to convert")
    parser.add_argument("--action", action='store_true', help="If specified, writes to SCHEMA_TEMP.md instead of SCHEMA.md. Used for the github action.")

    args = parser.parse_args()

    main(args.schema_name, args.action)
