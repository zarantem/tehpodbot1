FROM python:3.9-slim-buster
COPY . .
WORKDIR .
RUN python3 -m pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "./main.py"]
