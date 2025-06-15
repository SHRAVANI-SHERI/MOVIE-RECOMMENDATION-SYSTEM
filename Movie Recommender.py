import pandas as pd
import os
import zipfile
import random

# === Step 1: Extract the Dataset ZIP ===
zip_path = os.path.join("data", "archive.zip")
extract_dir = os.path.join("data", "extracted")

if not os.path.exists(extract_dir):
    os.makedirs(extract_dir, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

# === Step 2: Load CSV Files ===
ratings_path = os.path.join(extract_dir, 'Dataset.csv')
titles_path = os.path.join(extract_dir, 'Movie_Id_Titles.csv')

ratings_df = pd.read_csv(ratings_path)
titles_df = pd.read_csv(titles_path)

# === Step 3: Add Simulated Genre Column ===
sample_genres = ['Action', 'Comedy', 'Romance', 'Drama', 'Horror', 'Sci-Fi']
random.seed(42)  # for consistent genre assignments
titles_df['genre'] = titles_df['title'].apply(lambda x: random.choice(sample_genres))

# === Step 4: Merge Ratings and Titles ===
merged_df = pd.merge(ratings_df, titles_df, on='item_id')

# === Step 5: Compute Average Rating and Count ===
movie_stats = merged_df.groupby(['title', 'genre']).agg({
    'rating': ['mean', 'count']
}).reset_index()
movie_stats.columns = ['title', 'genre', 'average_rating', 'rating_count']

# === Step 6: Recommendation Function Based on Genre ===
def recommend_by_genre(user_genre, min_ratings=10, top_n=5):
    genre_filtered = movie_stats[movie_stats['genre'].str.lower() == user_genre.lower()]
    
    if genre_filtered.empty:
        available = ', '.join(sorted(set(movie_stats['genre'])))
        return f"❌ No movies found for genre: '{user_genre}'. Try one of: {available}"
    
    genre_filtered = genre_filtered[genre_filtered['rating_count'] >= min_ratings]
    top_movies = genre_filtered.sort_values(by='average_rating', ascending=False).head(top_n)
    
    return top_movies[['title', 'genre', 'average_rating', 'rating_count']]

# === Step 7: Take User Input and Display Recommendations ===
if __name__ == "__main__":
    user_input = input("🎞️ Enter a genre (Action, Comedy, Drama, Horror, Romance, Sci-Fi): ").strip()
    result = recommend_by_genre(user_input)
    print("\n🎬 Top Recommended Movies in Genre:", user_input.capitalize())
    print(result)
