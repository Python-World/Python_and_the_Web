import requests


def get_movies_from_tastedive(movieName, recom_limit):
    baseurl = "https://tastedive.com/api/similar"
    params_d = {}
    params_d["q"] = movieName
    params_d["k"] = "your_tastedive_API_key"
    params_d["type"] = "movies"
    params_d["limit"] = recom_limit
    resp = requests.get(baseurl, params=params_d)
    respDic = resp.json()
    return respDic


def extract_movie_titles(movieName):
    result = []
    for listRes in movieName["Similar"]["Results"]:
        result.append(listRes["Name"])
    return result


def get_related_titles(listMovieName, recom_limit):
    if listMovieName != []:
        auxList = []
        relatedList = []
        for movieName in listMovieName:
            auxList = extract_movie_titles(
                get_movies_from_tastedive(movieName, recom_limit)
            )
            for movieNameAux in auxList:
                if movieNameAux not in relatedList:
                    relatedList.append(movieNameAux)

        return relatedList
    return listMovieName


def get_movie_data(movieName):
    baseurl = "http://www.omdbapi.com/"
    params_d = {}
    params_d["t"] = movieName
    params_d["apikey"] = "your_OMDB_API_key"
    params_d["r"] = "json"
    resp = requests.get(baseurl, params=params_d)
    respDic = resp.json()
    return respDic


def get_movie_rating(movieNameJson):
    strRanting = ""
    for typeRantingList in movieNameJson["Ratings"]:
        if typeRantingList["Source"] == "Rotten Tomatoes":
            strRanting = typeRantingList["Value"]
    if strRanting != "":
        ranting = int(strRanting[:-1])
    else:
        ranting = 0
    return ranting


def get_sorted_recommendations(listMovieTitle, recom_limit):
    listMovie = get_related_titles(listMovieTitle, recom_limit)
    listMovie = sorted(
        listMovie,
        key=lambda movieName: (
            get_movie_rating(get_movie_data(movieName)),
            movieName,
        ),
        reverse=True,
    )
    return listMovie


if __name__ == "__main__":
    movielist = input("Enter movies seprated by comma(,) - ").split(",")
    recommendation_limit = input("Enter the limit of of recommended movies - ")
    recommended_Movies = get_sorted_recommendations(
        movielist, recommendation_limit
    )
    for movies in recommended_Movies:
        print(f"{recommended_Movies.index(movies)+1}. {movies}")
