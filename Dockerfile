# Use Python base image
FROM python:3.9-slim


# Set working directory
WORKDIR /app

# Copy files to container
COPY kmeans_dataset.py data.csv requirements.txt ./

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Run the script
CMD ["python", "kmeans_dataset.py"]
