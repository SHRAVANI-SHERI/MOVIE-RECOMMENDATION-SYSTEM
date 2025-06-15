# MOVIE-RECOMMENDATION-SYSTEM

An AI-based Python application that recommends top-rated movies based on genres using historical rating data. It's ideal for beginners learning data processing, recommendation logic, and CLI-based AI interactions.

AI Domain: Recommender Systems — part of Artificial Intelligence focused on personalized suggestions based on user preferences or data patterns.

## Overview

This project builds a simple movie recommender system that filters and suggests movies based on user-selected genres. It uses movie rating data, assigns genres (simulated for demo purposes), and returns highly rated titles from the selected genre.

## Requirements

This project requires only Python's standard libraries and pandas.

Install with:

pip install pandas

Modules used:
pandas – For data manipulation and analysis  
os, zipfile, random – Standard Python libraries (no installation needed)

## How It Works

Step 1: Extracts a ZIP file named archive.zip containing movie rating and title data  
Step 2: Loads data from Dataset.csv and Movie_Id_Titles.csv  
Step 3: Randomly assigns genres such as Action, Comedy, Drama, Horror, Romance, Sci-Fi, and Toy Story to each movie  
Step 4: Merges the title and rating data into a single dataset  
Step 5: Aggregates ratings and filters based on user-chosen genre  
Step 6: Displays top-rated movies in that genre based on average score and rating count

## Example Flow

Enter a genre (Action, Comedy, Drama, Horror, Romance, Sci-Fi, Toy Story): Comedy

Top Recommended Movies in Genre: Comedy

           title     genre  average_rating  rating_count  
  Movie A (1999)   Comedy            4.8             40  
  Movie B (2001)   Comedy            4.7             35  


## Future Scope

Replace simulated genres with real ones using APIs  
Add a web interface using Streamlit or Flask  
Use collaborative or content-based filtering techniques  
Integrate NLP to detect genres or movie tags  
Enable user login and personalized recommendations

