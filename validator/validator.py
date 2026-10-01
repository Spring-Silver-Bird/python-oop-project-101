from validator.schemes import StringSchema, NumberSchema, ListSchema, DictSchema

class Validator:
    def __init__(self) -> None:
        self.custom_validations = {
            'string': {},
            'number': {},
            'list': {},
            'dict': {},
        }

    def string(self):
        schema = StringSchema(self.custom_validations['string'])
        return schema

    def number(self):
        schema = NumberSchema(self.custom_validations['number'])
        return schema

    def list(self):
        schema = ListSchema(self.custom_validations['list'])
        return schema

    def dict(self):
        schema = DictSchema(self.custom_validations['dict'])
        return schema

    def add_validator(self, schema_type, name, func):
        if schema_type not in self.custom_validations:
            raise ValueError(f"Unknown schema type: {schema_type}")
        self.custom_validations[schema_type][name] = func


    def is_valid(self):
        pass
