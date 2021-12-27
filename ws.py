import cherrypy
import pandas as pd
import printer
p = printer.JokePrinter()

class MyWebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def process(self):
      p.run()
      return "Joke printed"

if __name__ == '__main__':
   config = {'server.socket_host': '0.0.0.0', 'server.socket_port': 9090}
   cherrypy.config.update(config)
   cherrypy.quickstart(MyWebService())
