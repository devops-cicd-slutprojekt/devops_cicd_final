from shop_app import testerproducts

def test_get_search_pattern():
    assert testerproducts.get_search_pattern() == "test%"
