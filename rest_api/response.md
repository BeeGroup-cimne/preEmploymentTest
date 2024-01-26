
## Running the API locally

1. pip install -r requirements.txt

2. uvicorn main:app --reload

3. To see the web content:  http://127.0.0.1:8000/consumption

4. To see the API documentation: http://127.0.0.1:8000/docs#

## Running the API in docker

1. docker build -t myimage .

2. docker run -d --name mycontainer -p 80:80 myimage

