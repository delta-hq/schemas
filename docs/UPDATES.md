# Proposing Schema Updates

This markdown document will walk you through how to make a schema update.

## High-level steps

1. Clone the repository.
2. Update the `schema.json` file.
3. Auto-generate the `SCHEMA.md` file.
4. Create a new branch and make a Pull Request.
5. Request a review and merge.

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

Steps to autogenerate all schema Markdown files at once:
```bash
python3 utils/convert_schema_to_markdown.py
```

### Review

Share the [Pull Request](https://github.com/delta-hq/schemas/pulls) with a relevant person on the research team, and ask them to review your schema changes.

As a reviewer, you should make note of the following:
- Changes to any `SCHEMA.md` file are auto-generated, so we do not need to review that.
    - However, it can be an easy way to visualize the schema changes.
- The schema version should be updated appropriately. See [semver.org](https://semver.org/) for more info.
- Descriptions should be clear and concise.

### Pull Requests

The only github functions needed for this are making a branch and creating a pull request with that branch.

The general workflow should look like this:

```bash
git checkout main # starting on the main branch
git pull
git checkout -b your-github-name/branch-name # the branch name can be anything, but I like to follow this format

# Make your code changes and repeat the following steps until done

git add . # stage all of your code changes
git commit -m "Commit message"
git push 
```

### Clone the Repository

Pull the repository into your local machine.

Requirements:
- Have git installed. See instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
- Have an IDE installed. See instructions for VS Code [here](https://code.visualstudio.com/download).

```bash
git clone git@github.com:delta-hq/schemas.git
cd schemas
code . # launch VS Code
```

### Column/Property Naming Conventions

- Using `snake_case` names.
- Try to avoid abbreviations.
- Schema type names are singular, not plural.
- `user_address` refers to the account address of the EOA that used the protocol.
