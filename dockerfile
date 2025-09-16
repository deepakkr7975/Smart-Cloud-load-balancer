# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy backend code
COPY backend.py .

# Install Flask
RUN pip install flask

# Expose ports (5000+)
EXPOSE 5000-5100

# Run backend
CMD ["python", "backend.py", "1"]
