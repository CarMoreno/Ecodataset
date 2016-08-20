#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, FOAF, RDFS
from ontologias import CRUZAR, VCARD, UMBEL

facebook = Namespace('https://www.facebook.com/')
univalleLugares = Namespace('http://190.14.254.237/dataseteco/RutaDelJardinBotanico/Lugares')
maps = Namespace('https://goo.gl/maps/')
gLugaresJardin = Graph()

def lugares(uri, nombre, descripcion, direccion, telefono, email, imagen, video, mapa): 
    if video == "No disponible":
        gLugaresJardin.add( (URIRef(uri), FOAF.depiction, Literal('No disponible')) )
    else:
        gLugaresJardin.add( (URIRef(uri), FOAF.depiction, URIRef(video)) )#puede ser usado para indicar contenido multimedia           
    
    gLugaresJardin.add( (URIRef(uri), RDF.type, CRUZAR['Recurso-turistico']) )
    gLugaresJardin.add( (URIRef(uri), RDF.type, VCARD.Location) )
    gLugaresJardin.add( (URIRef(uri), FOAF.name, Literal(nombre)) )
    gLugaresJardin.add( (URIRef(uri), RDFS.comment, Literal(descripcion)) )
    gLugaresJardin.add( (URIRef(uri), VCARD.tel, Literal(telefono))  )
    
    if email == "No disponible":
        gLugaresJardin.add( (URIRef(uri), VCARD.email, Literal('No disponible')) ) #agente

    gLugaresJardin.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) ) #revisar
    gLugaresJardin.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))

    #Dirección según vCard 2006
    gLugaresJardin.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    gLugaresJardin.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia')) )
    gLugaresJardin.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá')) )
    gLugaresJardin.add( (URIRef(mapa), VCARD['street-address'], Literal(direccion)) )
    
    #gLugaresJardin.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaMaiz.Lugares)))


lugares(
    facebook['jbjuanmariacespedes'],
    'Jardín Botánico Juan María Céspedes',
    """guarda un tesoro destinado para investigadores, científicos, amantes de la
    flora y la fauna y del paisaje que ofrecen los bosques secos tropicales""",
    'Corregimiento de Mateguadua, 763028 Tuluá',
    '3206888271, 3156361319, 5146848',
    'jardinbotanico@inciva.gov.co',
    'http://i.imgur.com/QIthGO2.jpg',#imagen
    univalleLugares['JardinBotanico.mp4'],#video
    maps['hRdkwZBgae22'],
)

lugares(
    'http://www.ciudadguru.com.co/empresas/cascada-de-la-arenosa-en-mateguadua/tulua/15951514',
    'Cascada la arenosa',
    """Hermoso sitio natural, agua muy fria, con arenas blancas y grandes piedras que la circundan.
    Los lugareños ofrecen la práctica del Rapell sobre la cascada y Rafting por el Río Tuluá hasta
    llegar al Jardín Botánico.""",
    'Corregimiento de Mateguadua, a 7 Km. de la cabecera municipal de Tuluá',
    '2260975, 2339300',
    'turismo@tulua.gov.co',
    'http://i.imgur.com/mJd34Ks.jpg',
    'No disponible',#video
    maps['wefveCHtHxG2']
)

lugares(
    'http://www.ciudadguru.com.co/empresas/semillero-de-guadua-y-bambu/tulua/15952774',
    'Semillero de Guadua y Bambú',
    """Vivencie los túneles que forman las guaduas y bambúes en el semillero más grande de Latinoamérica
    en el número de especies. Cierre los ojos y disfrute de los olores de las guaduas y los sonidos
    de los pájaros que despiertan los sentidos.""",
    '2260975, 3002202211',
    'No disponible',
    'http://i.imgur.com/lOZmXmJ.jpg',#imagen
    'No disponible', #VIDEO
    maps['wefveCHtHxG2']
)

print(gLugaresJardin.serialize(format='pretty-xml'))    