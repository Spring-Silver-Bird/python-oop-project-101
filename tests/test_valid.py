from validator.validator import Validator

v = Validator()

def test_vstring():
    assert v.string() is not v.string()

def test_norequired():
    assert v.string().is_valid(None) == True

def test_required():
    assert v.string().required().is_valid(None) == False

def test_minlentrue():
    assert v.string().min_len(5).is_valid('hexlet') is True

def test_minlenfalse():
    assert v.string().min_len(5).is_valid('hex') is False

def test_containstrue():
    assert v.string().required().contains('ex').is_valid('Hexlet') == True

def test_containsfalse():
    assert v.string().required().contains('ab').is_valid('Hexlet') == False

def test_doubleminlen():
    assert v.string().min_len(10).min_len(4).is_valid('Hexlet') == True