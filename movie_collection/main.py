# Add new movies to my collection
# List all the movies in my collection
# Find a movie by using the movie title

# Decide where to store movies in code
# Python list
# Decide what data we want to store for each movie
# Dictionaries: title, director, release year
# Show the user a menu and let them pick an option
# user input, while loop
# Implement each requirement in turn, each as a separate function
# Stop running the program when they type 'q' in the menu

movies = [
  {
    "Title": "Eternal Sunshine of the Spotless Mind",
    "Director": "Michel Gondry",
    "Release Year": 2004
  },
]

def view_movies():
  for movie in movies:
    print(movie["Title"])
    
def add_movie():
  new_movie_name = input("Provide the movie name: ")
  new_movie_director = input("Provide the movies director: ")
  new_movie_release = int(input("Provide the release year: "))
  movies.append({"Title": new_movie_name, "Director": new_movie_director, "Release Year": new_movie_release})
  
def find_movie():
  movie_search = input("What movie are you looking for: ")
  for movie in movies:
    if movie["Title"] == movie_search:
      print(f'{movie["Title"]}, {movie["Director"]}, {movie["Release Year"]}')

user_selection = input("Welcome to your movie collection, what would you like to do? \n(v)iew movies, (a)dd movie, (f)ind movie, or (q)uit\n")
while user_selection != "q":
  if user_selection == "v":
    view_movies()
  elif user_selection == "a":
    add_movie()
  elif user_selection == "f":
    find_movie()
  user_selection = input("Select an option: \n(v)iew movies, (a)dd movie, (f)ind movie, or (q)uit\n")