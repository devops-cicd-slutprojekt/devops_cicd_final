FROM python:3.11-slim

WORKDIR /app
# First we copy the requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Then we copy the script just before its used, this allows the previous build to be cached
COPY shop_app shop_app

ENV PYTHONUNBUFFERED=1
ENV FLASK_APP shop_app

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0"]
