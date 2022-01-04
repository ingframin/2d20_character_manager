import cherrypy
from mako.template import Template
import os
from generator import *
"""
This is just a stub
"""
class Start:
    @cherrypy.expose
    def index(self):
        home = Template(filename='./templates/begin.html')
        cherrypy.session['test'] = "test"
        return home.render()
    
    @cherrypy.expose
    def decision1(self,**kwargs):
        dec1 = Template(filename='templates/decision1.html')
        if len(kwargs) == 0:
            cherrypy.log(str(cherrypy.session))
            return dec1.render()
        else:
            try:
                sum = 40
                for k in kwargs:
                    val = int(kwargs[k])
                    sum -= val
                    cherrypy.session[k]=kwargs[k]
                cherrypy.log(f"sum={sum}")
                if sum != 0:
                    return cherrypy.session['test']
            except:
                
                return dec1.render()

            cherrypy.log(str(kwargs))
        return "ok" 
        


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