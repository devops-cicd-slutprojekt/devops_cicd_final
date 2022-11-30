import requests
def test_product(config):
    response = requests.get(
        config.base_url + '/testerproduct',
        timeout=config.TIMEOUT)
    assert response.status_code == 200
