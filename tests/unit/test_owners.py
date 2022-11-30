from shop_app import owners

def test_get_owners_is_string():
    assert isinstance(owners.GetOwners(), str)

def test_get_owners_string():
    assert "Owners are: Erik and Forsman" == owners.GetOwners()
