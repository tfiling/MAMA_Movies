import json
import SimpleHTTPServer
import urlparse
import urllib

from pandas.io.clipboard.clipboard import to_clipboard

from data import get_data
from data import data_filter_by_years
from data import data_filter_by_genre
from data import data_search_movie
from data import movie_list_to_response_json
from data import signupUser
from data import loginUser



class HCIRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):

        if "/data/" in self.path or "/data?" in self.path:
            parsed_request = urlparse.urlparse(self.path)
            data = json.dumps(get_data(dict(urlparse.parse_qsl(parsed_request[4]))))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(data)
            return

        if "/search" in self.path:
            try:
                parsed_request = urlparse.urlparse(self.path)
                searchRequest = json.loads(urllib.unquote(parsed_request[4]))
                ####search movie by name
                query = searchRequest['movieName']
                result = data_search_movie(query)
                print(result)

                ####filter results by year range
                if searchRequest['years'] is not None:
                    fromYearString = searchRequest['years']['fromYear']
                    toYearString = searchRequest['years']['toYear']
                    result = data_filter_by_years(result, int(fromYearString), int(toYearString))
                print(result)

                ####filter results by genre
                genreFilter = searchRequest['gener']
                if genreFilter is not None:
                    result = data_filter_by_genre(result, genreFilter)
                print(result)

                result = movie_list_to_response_json(result)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(result)
                return

            except Exception as e:
                # TODO make sure the exception was thrown due to empty argument
                print("search resulted exception: %s" % e)
            return

        if "/signup" in self.path:
            try:
                parsed_request = urlparse.urlparse(self.path)
                signupRequest = json.loads(urllib.unquote(parsed_request[4]))
                success, description = signupUser(signupRequest)
                userName = signupRequest["userName"] if success else ""
                result = {"description" : description,
                          "success" : success,
                          "userName" : userName}
                responseJson = json.dumps(result)
                print(responseJson)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(responseJson)
            except Exception as e:
                print("signup resulted exception: %s" % e)
            return

        if "/login" in self.path:
            try:
                parsed_request = urlparse.urlparse(self.path)
                loginRequest = json.loads(urllib.unquote(parsed_request[4]))
                success, description = loginUser(loginRequest)
                userName = loginRequest["userName"] if success else ""
                result = {"description" : description,
                          "success" : success,
                          "userName" : userName}
                responseJson = json.dumps(result)
                print(responseJson)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(responseJson)
            except Exception as e:
                print("login resulted exception: %s" % e)
            return


        # Requesting a resource (html, js, css)
        if "/shared/" not in self.path:
            if '/' == self.path:
                self.path = "/index.html"

            if "Mobi" in self.headers['user-agent']:
                # Requested by a mobile device
                self.path = '/mobile%s' % self.path
            else:
                self.path = '/desktop%s' % self.path

        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
