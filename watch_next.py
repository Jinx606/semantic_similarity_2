import spacy
import os

# Load spaCy's English model
nlp = spacy.load("en_core_web_md")

# Get the current working directory
current_directory = os.getcwd()

# Specify the full path to your movies.txt file in the current directory
movies_file_path = os.path.join(current_directory, "movies.txt")

# Read movie descriptions and titles from movies.txt into a dictionary
movies_data = {}
with open(movies_file_path, "r") as file:
    for line in file:
        parts = line.strip().split(":")
        if len(parts) == 2:
            movie_title = parts[0].strip()
            movie_description = parts[1].strip()
            movies_data[movie_title] = movie_description

def recommend_movie(description):
    max_similarity = -1
    recommended_movie = None

    # Calculate similarity between the input description and each movie's description
    input_doc = nlp(description)
    for title, movie_desc in movies_data.items():
        movie_doc = nlp(movie_desc)
        similarity = input_doc.similarity(movie_doc)
        if similarity > max_similarity:
            max_similarity = similarity
            recommended_movie = title

    return recommended_movie

if __name__ == "__main__":
    # Input description for "Planet Hulk"
    planet_hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

    # Recommend the next movie based on the input description
    recommended_movie = recommend_movie(planet_hulk_description)
    print("Recommended Movie:", recommended_movie)
