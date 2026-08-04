from validator.validator import Validator

v = Validator()

def test_diffdict():
    assert v.dict() is not v.list()

def test_norequired():
    assert v.dict().is_valid(None) == True

def test_required():
    assert v.dict().required().is_valid(None) == False

def test_anytype():
    assert v.dict().is_valid([3, 6, 9]) == False
def test_keytrue():
    schema = v.dict().shape({
        'name': v.string().required(),
        'age': v.number().positive(),
        })
    print(schema.shape_cheme)
    assert schema.is_valid({'name': 'kolya', 'age': 100}) == True

def test_noage():
    schema = v.dict().shape({
        'name': v.string().required(),
        'age': v.number().positive(),
        })
    print(schema.shape_cheme)
    assert schema.is_valid({'name': 'maya', 'age': None}) == True

def test_noname():
    schema = v.dict().shape({
        'name': v.string().required(),
        'age': v.number().positive(),
        })
    print(schema.shape_cheme)
    assert schema.is_valid({'name': '', 'age': 73}) == False

def test_nokey():
    schema = v.dict().shape({
        'name': v.string().required(),
        'age': v.number().positive(),
        })
    print(schema.shape_cheme)
    assert schema.is_valid({'name': 'Katarina'}) == True