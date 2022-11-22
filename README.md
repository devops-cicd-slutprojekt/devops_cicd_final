# devops_cicd_final


python3 -m venv .venv
For Linux/Mac: source .venv/bin/activate | For windows: .\.venv/Scripts/activate
pip install -r requirements.txt

Install coverage gutter in vscode

pytest --cov=shop_app tests

## Docker ghcr.io
docker build -t shop_app .
docker tag shop_app ghcr.io/devops-cicd-slutprojekt/shop_app
docker login ghcr.io
docker run -dp 5000:5000 ghcr.io/devops-cicd-slutprojekt/shop_app