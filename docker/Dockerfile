# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libssl-dev \
    libffi-dev \
    openssl \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user and set home directory
RUN useradd -ms /bin/bash lab

# Set environment variables
ENV FLASK_APP api_fifo_server.py
ENV FLASK_ENV production
ENV PATH="/home/lab/.local/bin:$PATH"

# Set the working directory to /home/lab/app
RUN mkdir -p /home/lab/app
RUN mkdir -p /home/lab/logs
RUN chmod 775 /home/lab/app
RUN chmod 775 /home/lab/logs
WORKDIR /home/lab/app

# Copy the current directory contents into the container at /home/lab/app
COPY . .
RUN chown -R lab:lab /home/lab

# Generate SSL certificates
# RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /home/lab/app/key.pem -out /home/lab/app/cert.pem -subj "/CN=localhost"

# Ensure correct ownership and permissions
# RUN chown -R lab:lab /home/lab/app
# RUN chmod 644 /home/lab/app/cert.pem 
# RUN chmod 400 /home/lab/app/key.pem
# RUN ls -la /home/lab/app

# Switch to non-root user
USER lab

# Install any needed packages specified in requirements.txt
RUN pip install --user --no-cache-dir -r requirements.txt

# Install uWSGI
RUN pip install --user uwsgi

# Create logs directory and ensure ownership
RUN mkdir -p /home/lab/logs && chown -R lab:lab /home/lab/logs

# Expose port 8443 for uWSGI
EXPOSE 8000

# Run Checks
# RUN openssl x509 -noout -modulus -in /home/lab/app/cert.pem | openssl md5
# RUN openssl rsa -noout -modulus -in /home/lab/app/key.pem | openssl md5

# Run uWSGI
CMD ["bash", "-c", "python fifo_init.py && uwsgi --ini /home/lab/app/uwsgi.ini"]
