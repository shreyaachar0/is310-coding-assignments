
import csv
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()
movies = []

console.print("Welcome to my Movie Data Collector!", style="bold cyan")
console.print("Here are some example movies:\n")

table = Table(title="My Favorite Movies")

table.add_column("Movie Title", style="cyan")
table.add_column("Genre", style="magenta")
table.add_column("Release Year")

table.add_row("Zootopia", "Animation", "2016")
table.add_row("The Devil Wears Prada", "Comedy", "2006")
table.add_row("How to Lose a Guy in 10 Days", "Romance", "2003")

console.print(table)
 

console.print("\nNow it's your turn to add a movie!", style="bold cyan")


while True:
    movie_title = input("Enter the movie title: ")
    genre = input("Enter the genre: ")
    release_year = input("Enter the release year: ")

    console.print("\nHere is the movie you entered:", style="bold green")

    console.print(f"Movie Title: {movie_title}")
    console.print(f"Genre: {genre}")
    console.print(f"Release Year: {release_year}")

    confirm = input("\nIs this information correct? (yes/no): ")

    if confirm.lower() == "yes":
        movies.append([movie_title, genre, release_year])
        console.print("Your movie information is correct!", style="bold green")

        another = input("\nWould you like to add another movie? (yes/no): ")

        if another.lower() == "no":
            break
    else:
        console.print("\nPlease enter your movie information again.", style="bold red")


file_path = Path(__file__).parent / "movie_data.csv"

with open(file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Movie Title", "Genre", "Release Year"])
    writer.writerows(movies)

console.print("\nYour movie data has been saved!", style="bold green")
console.print(f"File location: {file_path.resolve()}")

