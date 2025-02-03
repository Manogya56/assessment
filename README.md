## Instructions to run the application

### Make sure that Docker is installed and running on your machine

### This project is built using Python FastAPI. The project run on a uvicorn server(port 8080)

### To run the project locally:

From the root directory:
- Build the docker image using: docker build -t fastapi-app .
- Run the docker image using: docker run -p 8080:8080 fastapi-app

To make sure the application is up and running, in a browser open localhost:8080 and you should receive a "Hello World" message

Open localhost:8080/docs to test all the available endpoints.

## Testing Evidence:
- POST Method (/receipts/process)

![POST request 1st screenshot](testing_files\POST_req_1.png?raw=true "POST request 1st screenshot")

![POST request 1st screenshot](testing_files\POST_req_2.png?raw=true "POST request 1st screenshot")

- GET Method (/receipts/{id}/points)

![GET request screenshot](testing_files\GET_req.png?raw=true "GET request screenshot")

