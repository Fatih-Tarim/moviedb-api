import requests

class MovieDb():
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "faae666d1fea823e165cff670c9fb827"

    def getPopular(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    def getSearchResult(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

movieapi = MovieDb()

while True:
    secim = input("1- Popular Movies\n2-Search Movie \n3- Exit\nSeçim:")
    if secim == "3":
        break;
    else:
        if secim == "1":
            movies = movieapi.getPopular()
            for movie in movies['results']:
                print(movie['title'])

        if secim == "2":
            keyword = input('keyword: ')
            movies = movieapi.getSearchResult(keyword)
            for movie in movies['results']:
                print(movie['name'])

