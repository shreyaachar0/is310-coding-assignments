
import requests
from bs4 import BeautifulSoup
import time
import csv
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
from urllib.robotparser import RobotFileParser

BASE_URL = "https://bulbapedia.bulbagarden.net"

HEADERS = {
    "User-Agent": "is310-course-scraper/1.0 (student project; shreya42@illinois.edu)"
}

ROBOTS_URL = BASE_URL + "/robots.txt"
LIST_URL = BASE_URL + "/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"

POKEMON = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"]

POKEMON_TYPES = [
    "Grass", "Poison", "Fire", "Water",
    "Electric", "Normal", "Flying", "Bug",
    "Psychic", "Rock", "Ground", "Ice",
    "Dragon", "Dark", "Steel", "Fairy",
    "Fighting", "Ghost"
]

pokemon_data = []

# Check robots.txt before scraping
try:
    response = requests.get(
        ROBOTS_URL, headers=HEADERS, timeout=20
    )
    response.raise_for_status()
except requests.RequestException as error:
    raise SystemExit(f"Could not check robots.txt: {error}")

robots = RobotFileParser()
robots.parse(response.text.splitlines())

def allowed(url):
    return robots.can_fetch(HEADERS["User-Agent"], url)

def get_page(url):
    if not allowed(url):
        print("Not allowed by robots.txt:", url)
        return None

    try:
        response = requests.get(
            url, headers=HEADERS, timeout=20
        )

        if response.status_code != 200:
            print("Could not access:", url, response.status_code)
            return None

        if not allowed(response.url):
            print("Redirected to a disallowed page")
            return None

        return BeautifulSoup(response.text, "html.parser")

    except requests.RequestException as error:
        print("Request failed:", error)
        return None


# First level: scrape the Pokemon list page
print("Accessing Pokemon list page...")

soup = get_page(LIST_URL)
pokemon_urls = []

if soup is not None:
    print("Successfully accessed the Pokemon list page")

    if soup.title:
        print("Page title:", soup.title.get_text(strip=True))

    for link in soup.select("a[href]"):
        href = link.get("href", "")
        full_url = urljoin(BASE_URL, href)

        path = unquote(urlparse(full_url).path)

        for pokemon in POKEMON:
            if path == f"/wiki/{pokemon}_(Pokémon)":
                if full_url not in pokemon_urls:
                    pokemon_urls.append(full_url)

    print("Pokemon links found:", len(pokemon_urls))
else:
    print("Could not access the Pokemon list page")


# Second level: scrape individual Pokemon pages
for url in pokemon_urls:
    time.sleep(5)

    soup = get_page(url)

    if soup is None:
        continue

    heading = soup.find("h1")

    if heading is None:
        print("Pokemon name not found")
        continue

    name = heading.get_text(strip=True)
    name = name.replace(" (Pokémon)", "")

    pokemon_types = []

    # Find the types in the Pokemon information tables
    for table in soup.select("table.roundy"):
        found_types = []

        for link in table.select("a[href]"):
            href = unquote(link.get("href", ""))

            if not href.endswith("_(type)"):
                continue

            pokemon_type = link.get_text(strip=True)

            if pokemon_type in POKEMON_TYPES:
                if pokemon_type not in found_types:
                    found_types.append(pokemon_type)

        if found_types and len(found_types) <= 2:
            pokemon_types = found_types
            break

    print("Pokemon Name:", name)
    print("Types found:", pokemon_types)
    print("-------------------")

    pokemon_data.append({
        "Pokemon": name,
        "Type 1": pokemon_types[0] if pokemon_types else "",
        "Type 2": pokemon_types[1] if len(pokemon_types) > 1 else "",
        "URL": url
    })


# Save data to CSV
output_file = Path(__file__).parent / "pokemon_data.csv"

if pokemon_data:
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Pokemon", "Type 1", "Type 2", "URL"]
        )

        writer.writeheader()
        writer.writerows(pokemon_data)

    print("Scraping complete!")
    print("Data saved to:", output_file)
else:
    print("No data collected. Existing CSV was not overwritten.")
