from shop_app import product

def test_include_column_names():
    fake_list = []
    fake_description = []
    assert isinstance(product.include_column_names(fake_list,fake_description),list)
