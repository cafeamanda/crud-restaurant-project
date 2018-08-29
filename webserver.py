from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                r = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                output = ""
                if r != []:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output += "<html><body>"
                    output += "<form method='POST' enctype='multipart/form-data' action='restaurant/%s/delete'>" % restaurantIDPath
                    output += "<h1>Are you sure you want to delete %s?</h1>" % r.name
                    output += "<input type='submit' value='Delete'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)
                return

            if self.path.endswith("/edit"):
                restaurantIDPath = self.path.split("/")[2]
                r = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                output = ""
                if r != []:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output += "<html><body>"
                    output += "<h1>"
                    output += r.name
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action='restaurants/%s/edit'>" % restaurantIDPath
                    output += "<input name = 'newRestaurantName' type='text' placeholder='%s'>" % r.name
                    output += "<input type='submit' value='Rename'>"
                    output += "</form>"
                    output += "</body></html>"

                    self.wfile.write(output)
                print output
                return

            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += """
                            <form method='POST' enctype='multipart/form-data' action='/restaurants/new'>
                                <h1>Make a New Restaurant</h1>
                                <input name='newRestaurantName' type='text' placeholder='New Restaurant Name'>
                                <input type='submit' value='Create'>
                            </form>
                          """
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<p><a href='/restaurants/new'>Make A New Restaurant</a></p>"
                q = session.query(Restaurant).all()
                for r in q:
                    output += "<h2>" + r.name + "</h2>"
                    output += "<h3><a href='/restaurants/%s/edit'>Edit</a>" % r.id
                    output += "&emsp;"
                    output += "<a href='/restaurants/%s/delete'>Delete</a></h3>" % r.id
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                r = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                if r != []:
                    session.delete(r)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location','/restaurants')
                    self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    restaurantIDPath = self.path.split("/")[2]

                    r = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                    if r != []:
                        r.name = messagecontent[0]
                        session.add(r)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                newRestaurant = Restaurant(name = messagecontent[0])
                session.add(newRestaurant)
                session.commit()

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()

                return

        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()

if __name__ == '__main__':
    main()
