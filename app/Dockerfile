FROM python:3.9-slim
WORKDIR /app
RUN pwd
COPY /Users/abhayjain/jenkins/PythonFlaskScoreme/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

