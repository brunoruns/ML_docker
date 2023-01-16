# ML_docker
Based on https://towardsdatascience.com/build-and-run-a-docker-container-for-your-machine-learning-model-60209c2d7a7f

Building the model:
docker build -t docker-ml-model -f Dockerfile .
This might take a few minutes

Running the interference
docker run docker-ml-model python3 inference.py

If you run into a docker permission denied, see https://phoenixnap.com/kb/docker-permission-denied for more information to grant docker privilegfes to your user. Avoid the sudo approach!