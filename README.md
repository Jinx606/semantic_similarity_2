# Movie Recommendation System

This is a simple movie recommendation system that suggests the next movie to watch based on the word vector similarity of movie descriptions. It uses a pre-trained Word2Vec model and spaCy for natural language processing to calculate text similarity.

## Getting Started

Follow these instructions to set up and run the movie recommendation system.

### Prerequisites

- FROM pypy:latest

### Installation

Clone the repository to your local machine:

git clone https://github.com/Jinx606/semantic_similarity_2.git

1. Navigate to the project directory:

cd movie-recommendation-system

2. Create a virtual environment (optional but recommended):

python -m venv venv

3. Activate the virtual environment:

source venv/bin/activate

4. Install project dependencies:

pip install -r requirements.txt

## Usage

Run the movie recommendation system:

python watch_next.py

This will prompt you to enter a movie description, and it will recommend the next movie based on the input description.

## Customization

You can customize the recommendation system by providing your own movie descriptions in the 'movies.txt' file.

## Acknowledgments

This project uses spaCy for natural language processing and text similarity calculation.
Dockerfile (for reference)
Dockerfile

# Use an official Python runtime as a parent image
FROM pypy:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run recommend_movies.py when the container launches
CMD ["python", "watch_next.py"]