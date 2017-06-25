import json
import SimpleHTTPServer
import urlparse
import urllib

from pandas.io.clipboard.clipboard import to_clipboard

from data import get_data
from data import search_movie_by_year
from data import data_search_movie



class HCIRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        # API request for data

        if "/data/" in self.path or "/data?" in self.path:
            parsed_request = urlparse.urlparse(self.path)
            data = json.dumps(get_data(dict(urlparse.parse_qsl(parsed_request[4]))))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(data)
            return

        #TODO expose API here
        if "/search" in self.path:
            try:
                parsed_request = urlparse.urlparse(self.path)
                searchRequest = json.loads(urllib.unquote(parsed_request[4]))
                query = searchRequest['movieName']
                result = data_search_movie(query)
                # filtration = searchRequest['query']
                # value = searchRequest['value']
                #### filteration was parsed
                # if filtration == 'year':
                #     fromYear = searchRequest['from']
                #     toYear = searchRequest['to']
                #     result = search_movie_by_year(fromYear, toYear)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(result)
                return

            except Exception as e:
                # TODO make sure the exception was thrown due to empty argument
                print(e)
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
