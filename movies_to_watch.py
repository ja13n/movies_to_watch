import random
import requests
from bs4 import BeautifulSoup
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

class MovieFinder:
    def __init__(self) -> None:
        self.response = requests.get(URL)
        self.webpage = self.response.text
        self.soup = BeautifulSoup(self.webpage, "html.parser")
        self.movies = self.soup.find_all(name="h3", class_="title")
        self.the_list = [movie.getText() for movie in self.movies]
        self.movie_list = self.the_list[::-1]

    def find_movie(self):
            with open("movies.txt", "r", encoding="utf-8") as file: 
                choice = " "
                movies = file.readlines()
                movie_choice = random.choice(movies)
                finding = True
                while finding:
                    decision = movie_choice.split()
                    right_or_wrong = input(f"Have you watched '{choice.join(decision[1:])}' before? type 'y' or 'n'. ").lower()
                    if "y"!=right_or_wrong!="n":
                        print("please type in a valid input")
                    elif right_or_wrong == "y":
                        self.find_movie()
                        finding = False
                    elif right_or_wrong == "n":
                        print("Enjoy the movie!")
                        finding = False


person = MovieFinder()
person.find_movie()
