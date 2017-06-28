# The data for your website
import json

from tmdb3 import searchMovie
from tmdb3 import searchMovieWithYear


data = {
    # Example of a collection
    "dogs": [
        {
            "size": 'small',
            "name": 'Welsh Corgi',
            'snippet': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                       "Duis sed ultricies lectus, et porttitor diam. Vivamus viverra tincidunt sagittis. "
                       "Fusce pellentesque nibh a convallis eleifend. Ut malesuada, justo a sodales accumsan, "
                       "magna purus vehicula lorem, a tincidunt justo odio vitae leo. Nulla a enim at metus ultrices "
                       "mollis. Donec scelerisque, metus non volutpat finibus, ligula justo sollicitudin nisl, "
                       "sit amet rutrum lorem felis eu orci. Sed dictum dignissim sapien, quis sodales dolor vehicula "
                       "sit amet. Etiam tempus felis turpis, sit amet vehicula ante tincidunt at. Integer ligula mi, "
                       "lobortis a hendrerit et, posuere id elit. Donec pellentesque nisl id vestibulum porttitor."
                       "Phasellus vel felis rhoncus, vehicula nisl in, eleifend orci. Cras tellus nibh, semper nec mi "
                       "eget, interdum vehicula ante. In sed ultrices erat, vitae dictum magna. Mauris id porttitor "
                       "diam. Curabitur ut vehicula mi. Sed tempor felis nec est semper facilisis. Nunc a enim a "
                       "lectus placerat feugiat. Maecenas ante risus, sollicitudin nec ligula eget, luctus mollis "
                       "lorem."
                       "Curabitur aliquam, leo id venenatis posuere, leo ex condimentum augue, quis iaculis "
                       "elit nunc non sapien. Mauris id nunc aliquam, imperdiet diam ac, viverra ante. Praesent "
                       "hendrerit neque et nisi tincidunt, mattis ultrices eros mollis. Etiam auctor facilisis felis, "
                       "et commodo.",
            'imageUrl': '/shared/images/corgi.jpg'
        },
        {
            "size": 'small',
            "name": 'Cavalier King Charles Spaniel',
            'snippet': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                       "Duis sed ultricies lectus, et porttitor diam. Vivamus viverra tincidunt sagittis. "
                       "Fusce pellentesque nibh a convallis eleifend. Ut malesuada, justo a sodales accumsan, "
                       "magna purus vehicula lorem, a tincidunt justo odio vitae leo. Nulla a enim at metus ultrices "
                       "mollis. Donec scelerisque, metus non volutpat finibus, ligula justo sollicitudin nisl, "
                       "sit amet rutrum lorem felis eu orci. Sed dictum dignissim sapien, quis sodales dolor vehicula "
                       "sit amet. Etiam tempus felis turpis, sit amet vehicula ante tincidunt at. Integer ligula mi, "
                       "lobortis a hendrerit et, posuere id elit. Donec pellentesque nisl id vestibulum porttitor."
                       "Phasellus vel felis rhoncus, vehicula nisl in, eleifend orci. Cras tellus nibh, semper nec mi "
                       "eget, interdum vehicula ante. In sed ultrices erat, vitae dictum magna. Mauris id porttitor "
                       "diam. Curabitur ut vehicula mi. Sed tempor felis nec est semper facilisis. Nunc a enim a "
                       "lectus placerat feugiat. Maecenas ante risus, sollicitudin nec ligula eget, luctus mollis "
                       "lorem."
                       "Curabitur aliquam, leo id venenatis posuere, leo ex condimentum augue, quis iaculis "
                       "elit nunc non sapien. Mauris id nunc aliquam, imperdiet diam ac, viverra ante. Praesent "
                       "hendrerit neque et nisi tincidunt, mattis ultrices eros mollis. Etiam auctor facilisis felis, "
                       "et commodo.",
            'imageUrl': '/shared/images/cavalier.jpg'
        },
        {
            "size": 'medium',
            "name": 'Australian Shepherd',
            'snippet': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                       "Duis sed ultricies lectus, et porttitor diam. Vivamus viverra tincidunt sagittis. "
                       "Fusce pellentesque nibh a convallis eleifend. Ut malesuada, justo a sodales accumsan, "
                       "magna purus vehicula lorem, a tincidunt justo odio vitae leo. Nulla a enim at metus ultrices "
                       "mollis. Donec scelerisque, metus non volutpat finibus, ligula justo sollicitudin nisl, "
                       "sit amet rutrum lorem felis eu orci. Sed dictum dignissim sapien, quis sodales dolor vehicula "
                       "sit amet. Etiam tempus felis turpis, sit amet vehicula ante tincidunt at. Integer ligula mi, "
                       "lobortis a hendrerit et, posuere id elit. Donec pellentesque nisl id vestibulum porttitor."
                       "Phasellus vel felis rhoncus, vehicula nisl in, eleifend orci. Cras tellus nibh, semper nec mi "
                       "eget, interdum vehicula ante. In sed ultrices erat, vitae dictum magna. Mauris id porttitor "
                       "diam. Curabitur ut vehicula mi. Sed tempor felis nec est semper facilisis. Nunc a enim a "
                       "lectus placerat feugiat. Maecenas ante risus, sollicitudin nec ligula eget, luctus mollis "
                       "lorem."
                       "Curabitur aliquam, leo id venenatis posuere, leo ex condimentum augue, quis iaculis "
                       "elit nunc non sapien. Mauris id nunc aliquam, imperdiet diam ac, viverra ante. Praesent "
                       "hendrerit neque et nisi tincidunt, mattis ultrices eros mollis. Etiam auctor facilisis felis, "
                       "et commodo.",
            'imageUrl': '/shared/images/aussi.jpg'
        },

    ]
}

# TODO muted for now, consider removal:
#           will always search movies by name and will filter by years and genres
# def search_movie_by_year(fromYear = "2017", toYear = "2017"):# format: yyyy-yyyy or yyyy
#     movieList = []
#     for year in range(int(fromYear), (int(toYear) + 1)):
#         strYear = str(year)
#         res = searchMovieWithYear(strYear)
#         movieList.append(res)
#     responseJson = movie_list_to_response_json(movieList)
#     return responseJson

def data_filter_by_years(movieList = [], fromYear = 2017, toYear = 2017):
    if fromYear > toYear:
        fromYear = toYear   # handle a scenario where invalid arg is sent
    filteredList = []
    for movie in movieList:
        try:
            if ((movie.releasedate is not None) and movie.releasedate.year >= fromYear and movie.releasedate.year <= toYear):
                filteredList.append(movie)
        except Exception as e:
            print("data.data_filter_by_years exception: %s" % e)
    return filteredList

# TODO implement
def data_filter_by_genre(movieList, expectedGenre=None):
    if expectedGenre is None:
        return movieList
    filteredList = []
    for movie in movieList:
        try:
            genreList = movie.genres
            for genre in genreList:
                if genre.name == expectedGenre:
                    filteredList.append(movie)
        except Exception as e:
            print("data.data_filter_by_genre exception: %s" % e)
    return filteredList


def movie_list_to_response_json(movieList):
    movieArray = []
    resultCounter = 0
    for movie in movieList:
        imdbURL = 'http://www.imdb.com/title/%s' % movie.imdb
        movieDict = {"name" : movie.title,
                     "rating" : movie.userrating,
                     "revenues" : movie.revenue,
                     "linktopage" : imdbURL}
        movieArray.append(movieDict)
        resultCounter += 1
        if resultCounter > 5:
            break
    responseJson = json.dumps(movieArray)
    return responseJson


#returns a search results instance containing movie instances
def data_search_movie(query):
    movieList = searchMovie(query=query)# TODO remove middle man
    return movieList


def get_data(params):
    index = int(params.pop('_index', 0))
    length = int(params.pop('_length', 0))
    collection = params.pop('_collection')

    filtered_data = filter(lambda element: set(params.items()).issubset(set(element.items())),
                           data[collection])

    return filtered_data[index:index + length] if length > 0 else filtered_data[index:]
