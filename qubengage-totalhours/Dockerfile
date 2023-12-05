
# Uses pip to install python, flask and flask cors
# Uses Flask to create a simple web server
# Uses Flask-CORS to allow CORS requests

FROM python:3.9-slim
WORKDIR /app
RUN pip install --no-cache-dir Flask==2.0.1 Flask-CORS==3.0.10
COPY . /app/
EXPOSE 5000 