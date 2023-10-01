# Use the latest PyPy runtime as a parent image
FROM pypy:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run watch_next.py when the container launches
CMD ["pypy3", "watch_next.py"]
