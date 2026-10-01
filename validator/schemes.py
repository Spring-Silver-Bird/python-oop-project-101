import abc


class BasicScheme:
    def __init__(self, custom):
        self._required = False
        self._custom_validations = custom
        self._tests = {}



    def required(self):
        self._required = True
        return self

    @abc.abstractmethod
    def is_valid(self, something):
        return

    def test(self, custom_name, custom_value):
        if custom_name not in self._custom_validations:
            raise ValueError(f"Unknown validator: {custom_name}")
        self._tests[custom_name] = custom_value
        return self

    def _check_custom(self, value):
        for name, arg in self._tests.items():
            fn = self._custom_validations[name]
            try:
                if not fn(value, arg):
                    return False
            except Exception:
                return False
        return True

class StringSchema(BasicScheme):
    def __init__(self, custom):
        super().__init__(custom)
        self.min_length = None
        self.cont = ''


    def min_len(self, length):
        self.min_length = length
        return self

    def contains(self, item):
        self.cont = item
        return self


    def is_valid(self, string):
        rules = []
        if string is None:
            if not self._required:
                return True
            return False

        if not isinstance(string, str):
            return False
        if self._required and string == '':
            return False

        if self.min_length:
            if len(string) >= self.min_length:
                rules.append(True)
            else:
                rules.append(False)
        if self.cont:
            if self.cont in string:
                rules.append(True)
            else:
                 rules.append(False)
        if self._tests:
            rules.append(self._check_custom(string))
        return all(rules)


class NumberSchema(BasicScheme):
    def __init__(self, custom):
        super().__init__(custom)
        self.pos = False
        self.ran = []


    def positive(self):
        self.pos = True
        return self

    def range(self, begin, end):
        self.ran = [begin, end]
        return self


    def is_valid(self, number):
        rules = []
        if number is None:
            if not self._required:
                return True
            return False
        else:
            if isinstance(number, int):
                rules.append(True)
            else:
                return False
        if self.pos:
            if number > 0:
                rules.append(True)
            else:
                return False
        if self.ran:
            if number >= self.ran[0] and number <= self.ran[1]:
                rules.append(True)
            else:
                 return False
        if self._tests:
            rules.append(self._check_custom(number))
        return all(rules)

class ListSchema(BasicScheme):
    def __init__(self, custom):
        super().__init__(custom)
        self.sizeoflen = None

    def sizeof(self, lenth):
        self.sizeoflen = lenth
        return self

    def is_valid(self, items):
        rules = []
        if items is None:
            if not self._required:
                return True
            else:
                return False
        else:
            if isinstance(items, list):
                rules.append(True)
            else:
                return False
        if self.sizeoflen is not None:
            if len(items) == self.sizeoflen:
                rules.append(True)
            else:
                return False
        if self._tests:
            rules.append(self._check_custom(items))
        return all(rules)

class DictSchema(BasicScheme):
    def __init__(self, custom):
        super().__init__(custom)
        self.shape_cheme = {}

    def shape(self, items):
        for key in items:
            self.shape_cheme[key] = items[key]
        return self

    def is_valid(self, items):
        rules = []
        if items is None:
            if not self._required:
                return True
            else:
                return False
        else:
            if isinstance(items, dict):
                for key in self.shape_cheme:
                    schema = self.shape_cheme[key]
                    if key in items:
                        rules.append(schema.is_valid(items[key]))
                    else:
                        rules.append(schema.is_valid(None))
            else:
                return False
        if self._tests:
            rules.append(self._check_custom(items))
        return all(rules)
