# Use image as base python
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app/requirements.txt
COPY prediction_crypto.py /app/prediction_crypto.py

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run prediction_crypto.py when the container launches
CMD ["python", "prediction_crypto.py"]