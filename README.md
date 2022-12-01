# devops_cicd_final
Branch name standard for ANY coding you do:
feature/<name of your feature>

### Get up and running with the environment
On linux install virtualenv: apt install python3.10-venv

python3 -m venv .venv\
For Linux/Mac: source .venv/bin/activate | For windows: .\.venv/Scripts/activate\
pip install -r requirements.txt\
pre-commit install\
pre-commit run --all-files\
Install coverage gutter in vscode

## Docker ghcr.io
docker build -t shop_app .\
docker tag shop_app ghcr.io/devops-cicd-slutprojekt/shop_app\
docker login ghcr.io\
docker run -dp 5000:5000 ghcr.io/devops-cicd-slutprojekt/shop_app:latest


## Minikube to launch website
minikube service shop-service

## To run the environment on localy with docker
docker network create my-network
.\scripts\db.sh
.\scripts\flask.sh

## pytest (python3 if running on UNIX)
python -m pytest --cov=shop_app tests/unit
python -m pytest tests/integration

## Postman - API Test
In postman import the file 'scripts/devops_cicd.postman_collection.json
[POST] http://127.0.0.1:5000/product
{
    "name" : "{{$randomProduct}}",

    "price" : {{$randomPrice}}
}

docker run --network=my-network -t --rm --mount type=bind,source="$(pwd)"/scripts/,target=/postman,readonly postman/newman:alpine run /postman/devops_cicd.postman_collection.json --env-var="HOST=http://127.0.0.1:5000"

### xml junit result
docker run --network=my-network -t --rm --mount type=bind,source="$(pwd)"/scripts/,target=/postman postman/newman:alpine run /postman/devops_cicd.postman_collection.json --env-var="HOST=http://127.0.0.1:5000" --timeout-request=100 --reporters junit --reporter-junit-export="/postman/newman-report.xml"
