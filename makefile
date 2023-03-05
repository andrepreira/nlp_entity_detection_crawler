.DEFAULT_GOAL := up

# Define variables
DOCKER_IMAGE_NAME := nlp_entity_detection_crawler-app

# Build the Docker image
build:
	docker-compose build

# Start the Docker container
up: build
	docker-compose up -d

# Install dependencies
install:
	pip install -r requirements.txt

# Run unit tests
test:
	python -m unittest discover

# Stop the Docker container
stop:
	docker-compose down

# Remove the Docker container
remove:
	docker-compose rm -f

# Remove the Docker image
clean:
	docker rmi $(DOCKER_IMAGE_NAME)
