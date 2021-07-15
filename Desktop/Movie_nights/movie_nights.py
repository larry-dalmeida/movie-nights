import random
from movies import movies

print("Welcome to random Movie generator")

genre_selection = input("Do you want to select a genre? Type - yes or no\n").lower()

if genre_selection == 'no':
  #for random movie from all lists
  num_gen = random.randint(1,len(movies))
  random_movie = movies[num_gen]
  print(f"Our movie recomendation for you is {random_movie['name']}. The movie genre can be classified as {random_movie['genre']} and it was released in {random_movie['year']}.")
elif genre_selection == 'yes':
   print("Here's a list of the genres : action, adventure, biography, comedy, drama, fantasy, history, horror, mystery, romance, scifi, thriller, war")
   genre = input("What genre would you like to select?\n")
   

   
   else:
    print('Invalid input')
else:
  print("Invalid input") 

