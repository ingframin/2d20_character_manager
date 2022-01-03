import cherrypy
from mako.template import Template
import os

"""
This is just a stub
"""
class Start:
    @cherrypy.expose
    def index(self):
        home = Template(filename='./templates/begin.html')
        return home.render()
    
    @cherrypy.expose
    def decision1(self,method='standard'):
        return "Hello World"


conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './templates'
        },
}
cherrypy.quickstart(Start(),'/',conf)