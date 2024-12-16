# Use a lightweight Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the source code and tests
COPY src /app/src
COPY tests /app/tests
COPY requirements.txt /app

# Install dependencies
RUN pip install -r requirements.txt

# Command to run tests
CMD ["pytest", "tests"]
