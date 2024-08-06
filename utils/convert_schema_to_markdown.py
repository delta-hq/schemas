import json
import os
import sys

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

    return markdown

def read_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def write_markdown_file(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)

def main(schema_name):
    base_path = os.path.join('schemas', schema_name)
    json_filepath = os.path.join(base_path, 'schema.json')
    markdown_filepath = os.path.join(base_path, 'SCHEMA.md')

    # Read JSON schema
    json_data = read_json_file(json_filepath)

    # Convert JSON to Markdown
    markdown_content = json_to_markdown(json_data)

    # Write Markdown to file
    write_markdown_file(markdown_filepath, markdown_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_schema_to_markdown.py <schema_name>")
        sys.exit(1)

    schema_name = sys.argv[1]
    main(schema_name)
