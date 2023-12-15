# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt ./

# run pip install upgrade to avoid any errors
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY src/ ./

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run totalHours.py when the container launches
CMD ["python", "totalHours.py"]
