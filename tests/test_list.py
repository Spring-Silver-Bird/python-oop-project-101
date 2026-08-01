from validator.validator import Validator

v = Validator()

def test_vnumber():
    assert v.list() is not v.list()

def test_norequired():
    assert v.list().is_valid(None) == True

def test_required():
    assert v.list().required().is_valid(None) == False

def test_anynumber():
    assert v.list().is_valid([3, 6, 9]) == True

def test_emptylist():
    assert v.list().is_valid([]) == True

def test_sizeoftrue():
    assert v.list().sizeof(5).is_valid([3, 6, 9, 34, 5]) == True

def test_positivefalse():
    assert v.list().sizeof(3).is_valid([3, 6, 9, 34, 5]) == False


def test_doublesizetrue():
    assert v.list().sizeof(3).sizeof(5).is_valid([3, 6, 9, 34, 5]) == True
