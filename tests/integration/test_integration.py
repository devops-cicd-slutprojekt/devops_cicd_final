import requests
def test_product(config):
    response = requests.get(
        config.base_url + '/product',
        timeout=config.TIMEOUT)
    assert response.headers['content-type'] == 'application/json'
    assert response.status_code == 200
    assert {'id': 1,
        'name': 'Hammer',
        'price': 199} in response.json()
