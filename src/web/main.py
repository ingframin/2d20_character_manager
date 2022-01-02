import cherrypy
"""
This is just a stub
"""
class Start:
    @cherrypy.expose
    def index(self):
        return "Hello World"

cherrypy.quickstart(Start())