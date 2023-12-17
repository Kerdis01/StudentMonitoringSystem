# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the config.json file to the /app directory
COPY requirements.txt /app/

# Copy the contents of the src directory to /app/src
COPY src/ /app/src/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 7001 available to the world outside this container
EXPOSE 7001

# run the auth app
CMD ["python", "src/authenticate.py"]