# devops_cicd_final
Branch name standard for ANY coding you do:
feature/<name of your feature>

### Get up and running with the environment
On linux install virtualenv: apt install python3.10-venv

python3 -m venv .venv\
For Linux/Mac: source .venv/bin/activate | For windows: .\.venv/Scripts/activate\
pip install -r requirements.txt\
pre-commit sample-config > .precommit-config.yaml\
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
