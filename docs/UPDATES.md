# Proposing Schema Updates

This markdown document will walk you through how to make a schema update.

## High-level steps

1. Update the `schema.json` file.
2. Auto-generate the `SCHEMA.md` file.
3. Request a review and merge.

### Schema JSON

To update a schema, you actually only need to update the JSON file associated with the schema. The `SCHEMA.md` file is auto-generated (you will learn how to update this later).

- Make any edits to the schema following the outlined schema formatting conventions.
- Update the schema version following [semver.org](https://semver.org/) (semantic versioning).
- Column names are in `snake_case`.
- Use clear and concise column names (or properties) and descriptions.

### Auto-Generate SCHEMA.md File

There is a python script that lives under `/utils` called [`convert_schema_to_markdown.py`](../utils/convert_schema_to_markdown.py) that can be utilized to auto-generate `SCHEMA.md`.

Requirement:
- `Python` or `Python3`, see instructions on how to download [here](https://wiki.python.org/moin/BeginnersGuide/Download).

Steps to run, from the root of the repository, using `lending` as an example:
```bash
python3 utils/convert_schema_to_markdown.py lending
```

### Review

Share the [Pull Request](https://github.com/delta-hq/schemas/pulls) with a relevant person on the research team, and ask them to review your schema changes.

As a reviewer, you should make note of the following:
- Changes to any `SCHEMA.md` file are auto-generated, so we do not need to review that.
    - However, it can be an easy way to visualize the schema changes.
- The schema version should be updated appropriately. See [semver.org](https://semver.org/) for more info.
- Descriptions should be clear and concise.

### Column/Property Naming Conventions

- Using `snake_case` names.
- Try to avoid abbreviations.
- Schema type names are singular, not plural.
- `user_address` refers to the account address of the EOA that used the protocol.
