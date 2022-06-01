from SCRIPTLIBRARIES.ESI4Py import esiobject_base_noauth as AUTHLESSESI
from SCRIPTLIBRARIES.templatemanager import template_manager as TM
from EVEWORK_ANALYSIS.EVEWORK_ANALYSIS import EVEWORK_ANALYSIS as EA
from EVEWORK_ANALYSIS.whitelistmanager import WhiteListManager as WLM


import threading
import cherrypy

def whitelistholderfunc():
    Whitelist = WLM()
    Whitelist.start()


import os.path
from datetime import datetime
import json

def DEBUG_print(toDEBUG_print):
    if DEBUG:
        print(toDEBUG_print)

def error_page_404(status, message, traceback, version):
        return "<meta http-equiv = \"refresh\" content = \"0; url = /dscan\" />"

def error_page_500(status, message, traceback, version):
        return "<meta http-equiv = \"refresh\" content = \"0; url = /dscan\" />"

class Mainsite(object):
    @cherrypy.expose
    def default(self, attr='abc'):
        DEBUG_print("EXECUTING DEFFAULT PAGE")
        return "<meta http-equiv=\"Refresh\" content=\"0; url=\'http://"+URI+"\'\" />"
    @cherrypy.expose
    def index(self):
        DEBUG_print("EXECUTING INDEX PAGE")
        indexPage = TM()
        indexPage.load_html_template("TEMPLATES/index.html")
        return indexPage.get_parsed_html()
    @cherrypy.expose
    def dscan(self):
        DEBUG_print("EXECUTING SCAN PAGE")
        dscanPage = TM()
        dscanPage.load_html_template("EVEWORK_ANALYSIS/TEMPLATES/dscan-template.html")
        #dscanPage.format_html(["yes","why"])
        return dscanPage.get_parsed_html()
    
    @cherrypy.expose
    def dscanAnalyse(self,SCANCODE="",DSCAN="",LOCAL="",useDSCAN="",useLOCAL=""):
        DEBUG_print("EXECUTING ANALYSIS PAGE")
        EAvar= EA(DEBUG,URI,SCANCODE,DSCAN,LOCAL,useDSCAN,useLOCAL)
        return EAvar.DSCANAnalyse()



if __name__ == '__main__':
    # Load config
    URI = None
    DEBUG = None
    USE_ID_WHITELIST_UPDATER = None
    f = open("config.json", "r")
    config_data = json.loads(f.read())
    f.close()
    URI = config_data["URI"]
    DEBUG = config_data["DEBUG"]
    PORT = int(config_data["PORT"])
    USE_ID_WHITELIST_UPDATER = config_data["USE ID WHITELIST UPDATER"]
    if (USE_ID_WHITELIST_UPDATER):
        WhitelistmanagerThread = threading.Thread(target=whitelistholderfunc)
        WhitelistmanagerThread.start()

    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/rsc': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './external_resources'
        }
    }
    if DEBUG == False:
            cherrypy.config.update({'error_page.500': error_page_500})

    cherrypy.config.update({'error_page.404': error_page_404})
    cherrypy.config.update({'server.socket_port': PORT})
    cherrypy.config.update({'server.socket_host': "0.0.0.0"})
    cherrypy.quickstart(Mainsite(),'/',conf)
