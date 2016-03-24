# -*- coding: utf-8 -*-

import cherrypy
from rdflib import Namespace, BNode, Literal, RDF, URIRef
from conexion import Conectar
from mako.template import Template
from mako.lookup import TemplateLookup
from urllib import quote_plus


lookup = TemplateLookup(directories=['templates'])
con=Conectar('http://localhost:8080/openrdf-sesame/') #Conexion al servidor

con.use_repository('maiz') # Repositorio de la ruta del maiz

#Namespaces
con.addnamespace('JB','http://semprog.com/schemas/jobboard#')
con.addnamespace('dbpedia', 'http://dbpedia.org/resource/')
con.addnamespace('wikidata', 'http://www.wikidata.org/entity/')
con.addnamespace('facebook', 'https://www.facebook.com/')
con.addnamespace('twitter', 'https://www.twitter.com/')
con.addnamespace('productos_principe','http://principeh.com/producto/')
con.addnamespace('productos_juanmaria', 'http://hoteljuanmaria.com/es/habitaciones/')
con.addnamespace('productos_cf', 'http://hotelcafeplaza.com/producto/')


class Main(object):

    @cherrypy.expose
    def index(self):
        #return open('vistas/index.html')
        id=quote_plus('vistas/index.html')
        return 'Try visiting <a href="id=%s">here</a>' % id



    #/**
    # * Permite obtener todas las tripletas del repositorio
    # */
    @cherrypy.expose
    def verTodo(self):
        todos = con.query('SELECT ?sub ?pred ?obj WHERE { ?sub ?pred ?obj.}')
        resultado = str(todos).split(",")
        name = "Tripletas Ruta del Maiz en Campoalegre"
        return """<html>
                    <head>
                        <title>Viendo Tripletas Ruta del Maiz en Campoalegre</title>
                    </head>
                    <body>
                        <h1>ECOLOD</h1>
                    </body>
                </html>""" + todos


    #/**
    # * Permite obtener los datos desde SESAME
    # * id, identificador del objeto cuyas tripletas quieren verse
    # * Se recuperan todos las tripletas que cuentan con esta identificación como sujeto u objeto
    # */
    @cherrypy.expose
    def view(self, id):
        sa=con.query('SELECT ?pred ?obj WHERE {' + id + '?pred  ?obj .}') # el id es el sujeto
        #oa=con.query('SELECT ?pred ?sub WHERE {?sub ?pred "'+id+'".}') # el id es el objeto
        #name=id

        #if len(sa) == 0:
            #resul = str(oa)
        #else:
            #resul = str(sa)

        return str(sa)

        #t=lookup.get_template('vistaGenerica.html')
        #return t.render(name=name,sa=sa,oa=oa,qp=quote_plus)
 
cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 8099 }) # se cambia el puerto
cherrypy.quickstart(Main())
