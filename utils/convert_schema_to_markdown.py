import json
import os
import sys
import argparse

def json_to_markdown(json_data):
    markdown = f"# {json_data['schema']}\n\n"
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
    
    markdown += "> Note: This markdown file is auto-generated.\n"
    return markdown

def read_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def write_markdown_file(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)

def process_schema(schema_name, action_flag):
    base_path = os.path.join('schemas', schema_name)
    json_filepath = os.path.join(base_path, 'schema.json')
    
    markdown_filepath = os.path.join(base_path, 'SCHEMA_TEMP.md') if action_flag else os.path.join(base_path, 'SCHEMA.md')

    print(f"Processing schema: {schema_name}")
    print(f"JSON file path: {json_filepath}")
    print(f"Markdown file path: {markdown_filepath}")

    try:
        json_data = read_json_file(json_filepath)
        markdown_content = json_to_markdown(json_data)
        write_markdown_file(markdown_filepath, markdown_content)
        print(f"Markdown file created successfully for {schema_name}.")
    except Exception as e:
        print(f"Error processing schema {schema_name}: {e}")

def get_all_schemas():
    schemas_dir = 'schemas'
    return [name for name in os.listdir(schemas_dir) 
            if os.path.isdir(os.path.join(schemas_dir, name))]

def main(schema_name, action_flag):
    if schema_name:
        process_schema(schema_name, action_flag)
    else:
        all_schemas = get_all_schemas()
        for schema in all_schemas:
            process_schema(schema, action_flag)
        print("Successfully processed all schemas.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON schema to Markdown.")
    parser.add_argument("schema_name", nargs='?', help="Name of the schema to convert. If not provided, converts all schemas.")
    parser.add_argument("--action", action='store_true', help="If specified, writes to SCHEMA_TEMP.md instead of SCHEMA.md. Used for the github action.")

    args = parser.parse_args()

    main(args.schema_name, args.action)