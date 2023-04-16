import cherrypy
import os
import webview


conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/assets': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './assets'
        }
    }

class CharacterGenerator:

    @cherrypy.expose
    def begin(self):
        with open('assets/begin.html') as pf:
            content = pf.read()

        return content

website = CharacterGenerator()

webview.create_window('Hello world', 'http://127.0.0.1:8080/assets/begin.html')
webview.start(cherrypy.quickstart,(website,'/',conf))
print('exit')
cherrypy.server.stop()
cherrypy.engine.stop()
cherrypy.engine.exit()
exit(0)