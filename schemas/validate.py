from jsonschema import validate
import json
import os


def validate_argentine_banks_for_schema(json_banks: dict) -> None:
    file_path = os.path.join(os.path.dirname(__file__), 'schema_argentine_banks.json')
    with open(file_path, 'r') as values:
        SCHEMA_ARGENTINE_BANK = json.load(values)

    validate(instance=json_banks, schema=SCHEMA_ARGENTINE_BANK)
