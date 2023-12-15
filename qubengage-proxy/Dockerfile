# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the config.json file to the /app directory
COPY requirements.txt config.json /app/

# Copy the contents of the src directory to /app/src
COPY src/ /app/src/

# run pip install upgrade to avoid any errors
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 9000 available to the world outside this container
EXPOSE 9000

# Run proxy.py when the container launches
CMD ["python", "src/proxy.py"]
