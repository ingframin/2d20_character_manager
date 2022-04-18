import cherrypy
from mako.template import Template
import os
from generator import *

# This should be migrated to a more capable framework such as Django.

class Start:
    @cherrypy.expose
    def index(self):
        home = Template(filename='./templates/begin.html')
        cherrypy.session['test'] = "test"
        return home.render()
    
    @cherrypy.expose
    def update_session(self,**kwargs):
        print(kwargs)
        try:
            for k in kwargs:
                val = int(kwargs[k])
                cherrypy.session[k]=kwargs[k]
        except:
            #There should be different kind of errors
            #TBD
            return "Error"
        
        return "OK"
    
    # This can be a single function with different arguments
    @cherrypy.expose
    def decision1(self,**kwargs):
        dec1 = Template(filename='templates/decision1.html')
           
        return dec1.render()

    @cherrypy.expose   
    def decision2(self,**kwargs):
        dec2 = Template(filename='templates/decision2.html')
           
        return dec2.render()
        

conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './templates'
        },
}
cherrypy.quickstart(Start(),'/',conf)