# devops_cicd_final
Branch name standard for ANY coding you do:
feature/<name of your feature>

### Get up and running with the environment
On linux install virtualenv: apt install python3.10-venv

python3 -m venv .venv\
For Linux/Mac: source .venv/bin/activate | For windows: .\.venv/Scripts/activate\
pip install -r requirements.txt\
pre-commit sample-config > .pre-commit-config.yaml\
pre-commit install\
pre-commit run --all-files\
Install coverage gutter in vscode

pytest --cov=shop_app tests

## Docker ghcr.io
docker build -t shop_app .\
docker tag shop_app ghcr.io/devops-cicd-slutprojekt/shop_app\
docker login ghcr.io\
docker run -dp 5000:5000 ghcr.io/devops-cicd-slutprojekt/shop_app


## Minikube
minikube service shop-app-pod

## docker
docker create network my-network
.\scripts\db.sh
.\scripts\flask.sh

## pytest
python -m pytest --cov=shop_app tests/unit
python -m pytest tests/integration

## Postman - API Test
docker run --network=my-network -t --rm --mount type=bind,source="$(pwd)"/scripts/,target=/postman,readonly postman/newman:alpine run /postman/devops_cicd.postman_collection.json --env-var="HOST=http://192.168.49.2:31254"

### xml junit result
docker run --network=my-network -t --rm --mount type=bind,source="$(pwd)"/scripts/,target=/postman postman/newman:alpine run /postman/devops_cicd.postman_collection.json --env-var="HOST=http://192.168.49.2:31254" --timeout-request=100 --reporters junit --reporter-junit-export="/postman/newman-report.xml"


[POST] http://127.0.0.1:5000/product
{
    "name" : "{{$randomProduct}}",

    "price" : {{$randomPrice}}
}
