# Docker Deployment of Iris ML Application

## 1. Objective

To containerize the Iris Machine Learning application using Docker. The application is trained, packaged and deployed inside a Docker container.

## 2. Tools and Technologies

- Python 3.11
- Docker Desktop
- Docker Engine
- Scikit-learn
- Pandas and NumPy
- Joblib
- Git and GitHub

## 3. Implementation

A multi-stage Dockerfile was created.

**Builder Stage:**
- Installs the required Python libraries.
- Copies the processed Iris dataset.
- Trains the Random Forest classification model.
- Saves the trained model files.

**Runtime Stage:**
- Copies the trained model and dependencies.
- Copies the prediction API.
- Exposes port 8000.
- Configures a Docker health check.

## 4. Docker Image Creation

Command:

`docker build -t iris-classifier:v1 .`

Result: Docker image created successfully.

Image name: `iris-classifier`

Tag: `v1`

Image content size: **155 MB**

## 5. Running the Container

Command:

`docker run -d --name iris-classifier-container -p 8000:8000 iris-classifier:v1`

Result: Container started successfully and showed healthy status.

## 6. API Testing

**Health Endpoint**

`GET /health`

Output:

`{"status": "healthy"}`

**Prediction Endpoint**

`POST /predict`

Sample prediction:

- Predicted class: setosa
- Probabilities: [1.0, 0.0, 0.0]

**Invalid Input Testing**

The API returned HTTP 400 Bad Request when required features were missing.

## 7. Health Check

Docker health check was configured to monitor the application using the `/health` endpoint.

Observed status: Healthy.

## 8. Conclusion

The Iris Machine Learning application was successfully containerized using Docker. A multi-stage Docker build was used to separate model training from the runtime environment. The container was tested successfully using health and prediction endpoints. Invalid input was also handled correctly.