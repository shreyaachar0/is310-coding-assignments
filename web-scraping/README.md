# Community Wiki Web Scraping: Pokémon

## Wiki Selection and Research Question

For this assignment, I chose Bulbapedia, which is a community-run wiki that provides information about Pokémon. I chose this because I thought it would be interesting to see how different Pokémon are categorized based on their types. My research question is: How do the primary and secondary types differ among four selected Pokémon on Bulbapedia?

I focused on Bulbasaur, Charmander, Squirtle, and Pikachu. This data could be useful to researchers who are interested in how online communities organize and categorize information. It can also help demonstrate how structured information can be collected from community-run websites.

## Web Scraping Process

I used Python with the requests and BeautifulSoup libraries to collect information from Bulbapedia. My scraper first visits the National Pokédex list page and finds links to the four Pokémon I selected. It then visits their individual pages to collect their names, primary types, secondary types, and URLs.

I saved the collected information in a CSV file called `pokemon_data.csv`. I chose CSV because it makes the data easier to organize, compare, and analyze using other programs.

## Robots.txt and Website Policies

Before scraping, I checked Bulbapedia's robots.txt file:

https://bulbapedia.bulbagarden.net/robots.txt

The file allows access to regular wiki pages under `/wiki/`, but restricts certain pages, including special search pages, random pages, shipping pages, and some page history URLs. It also specifies a crawl delay of five seconds.

I included a User-Agent identifying my student project and a five-second delay between requests. I also checked the response status codes before parsing the pages.

I reviewed Bulbapedia's general policies, which focus on responsible contributions and use of the wiki. My project only reads a small number of public pages and does not make changes to the website.

Policy page: https://bulbapedia.bulbagarden.net/wiki/Bulbapedia:Policy

## Reflection on Data Collection

One thing I noticed from this assignment is that the data I collected only represents how Pokémon are categorized on Bulbapedia. Although I collected their primary and secondary types, this does not necessarily tell us how strong or popular a Pokémon is. For example, just because a Pokémon has two types does not mean it is better than one with only one type. The data is also limited because I only selected four Pokémon rather than looking at the entire Pokédex. Someone would be wrong to use my results to make conclusions about all Pokémon. Overall, this assignment helped me understand how web scraping can collect useful information, but also how important it is to consider what the data actually measures.