class Validator:
    def string(self):
        schema = StringSchema()
        return schema


class StringSchema:
    def __init__(self):
        self.flag_required = False
        self.min_lenth = 0
        self.cont = ''


    def required(self):
        self.flag_required = True
        return self


    def min_len(self, lenth):
        self.min_lenth = lenth
        return self

    def contains(self, item):
        self.cont = item
        return self


    def is_valid(self, string):
        rules = []
        if string == None:
            if not self.flag_required:
                return True
            return False

        if self.min_lenth:
            if len(string) >= self.min_lenth:
                rules.append(True)
            else:
                rules.append(False)
        if self.cont:
            if self.cont in string:
                rules.append(True)
            else:
                rules.append(False)
        return all(rules)


