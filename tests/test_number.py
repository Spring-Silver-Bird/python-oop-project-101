from validator.validator import Validator

v = Validator()

def test_vnumber():
    assert v.number() is not v.number()

def test_norequired():
    assert v.number().is_valid(None) == True

def test_required():
    assert v.number().required().is_valid(None) == False

def test_anynumber():
    assert v.number().is_valid(7) == True

def test_positivetrue():
    assert v.number().positive().is_valid(10) == True

def test_positivefalse():
    assert v.number().positive().is_valid(-5) == False

def test_rangetrue():
    assert v.number().range(-5, 5).is_valid(2) == True

def test_rangefalse():
    assert v.number().range(-5, 5).is_valid(7) == False

def test_rangeborder():
    assert v.number().range(-5, 5).is_valid(-5) == True

def test_allrulestrue():
    assert v.number().positive().range(-5, 10).is_valid(6) == True

def test_allrulesfalse():
    assert v.number().positive().range(-5, 5).is_valid(-3) == False

def test_allrulesfalse2():
    assert v.number().positive().range(-5, 5).is_valid(0) == False

def test_allrulesfalse2():
    assert v.number().required().positive().range(-5, 5).is_valid(None) == False