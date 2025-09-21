# Start from Python
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else
COPY . .

# Expose port 5000
EXPOSE 5000

# Run your Flask app
CMD ["python", "app.py"]


