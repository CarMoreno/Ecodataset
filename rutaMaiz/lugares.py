#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, FOAF, RDFS
from ontologias import CRUZAR, VCARD, UMBEL
from flora import gRutaMaiz, rutaMaiz

facebook = Namespace('https://www.facebook.com/')
univalleLugares = Namespace('http://190.14.254.237/dataseteco/RutaDelMaiz/Lugares/')
maps = Namespace('https://goo.gl/maps/')
gRutaMaiz = Graph()

def lugares(uri, nombre, descripcion, direccion, telefono, email, imagen, video, mapa): 
    if video == "No disponible":
        gRutaMaiz.add( (URIRef(uri), FOAF.depiction, Literal('No disponible')) )
    else:
        gRutaMaiz.add( (URIRef(uri), FOAF.depiction, URIRef(video)) )#puede ser usado para indicar contenido multimedia           
    gRutaMaiz.add( (URIRef(uri), RDF.type, CRUZAR['Recurso-turistico']) )
    gRutaMaiz.add( (URIRef(uri), RDF.type, VCARD.Location) )
    gRutaMaiz.add( (URIRef(uri), FOAF.name, Literal(nombre)) )
    gRutaMaiz.add( (URIRef(uri), RDFS.comment, Literal(descripcion)) )
    gRutaMaiz.add( (URIRef(uri), VCARD.tel, Literal(telefono))  )
    gRutaMaiz.add( (URIRef(uri), VCARD.email, Literal(email)) ) #agente
    gRutaMaiz.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) ) #revisar
    gRutaMaiz.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))

    #Dirección según vCard 2006
    gRutaMaiz.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    gRutaMaiz.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia')) )
    gRutaMaiz.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá')) )
    gRutaMaiz.add( (URIRef(mapa), VCARD['street-address'], Literal(direccion)) )
    
    gRutaMaiz.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaMaiz.Lugares))) 

lugares(
    'https://youtube/O2Up1EVnkLQ',#video parque de la guadua
    'Parque de la Guadua "Guillermo Ponce de Leon París"',
    """Hermoso sitio natural, cuenta con abundantes cultivos de guadua y flores exóticas, senderos ecológicos, 
    cascada y piscina natural de agua tibia, espacios para la meditación y compartir en familia""",
    'Avenida Kenedy diagonal a la Productora de Jugos',
    '22251548',
    'parqueguadua@hotmail.com',
    'http://i.imgur.com/2r8lJWt.jpg',
    univalleLugares['ParqueGuadua.mp4'],
    maps['wr9jbYdmt742']
)

lugares(
    'http://www.tulua.gov.co/sitio.shtml?apc=m1G5--&x=1475586',
    'Lago Chilicote',
    """Lago artificial que se caracteriza por tener un árbol en todo el centro. A su alrededor se encuentra un parque que le permite a la ciudadanía sentarse a descansar o 
    incluso a pescar""",
    'Barrios Sajonia y el Lago',
    'No disponible',
    'No disponible',
    'http://i.imgur.com/BYqy4hZ.jpg',
    univalleLugares['lagoChilicote.mp4'],
    maps['CeSudK2K98S2']
)

lugares(
    facebook['parquecarlossarmientolora?fref=ts'],
    'Parque Carlos Sarmiento Lora',
    """Parque escenario para la recreación, el deporte y el ecoturismo. Cuenta con actividades acuáticas en sitios
    naturales y artificiales, campos de juego, camping, restaurante y un jardín japonés.""",
    'Entrada Variante Sur',
    '224 48 53, 224 16 77',
    'parquecarlosarmientolora@hotmail.com',
    'http://i.imgur.com/hVhPc5m.png',
    'No disponible',
    maps['eMYDXk6nBzk']
)

lugares(
    facebook['pages/Parque-Lineal-Cespedes/473779859367621'],
    'Parque Lineal Juan María Céspedes',
    """Punto tradicional preferido de propios y extraños para el encuentro, la tertulia, el esparcimiento en familia 
    y el descanso""",
    'Entre las Carreras 27 y 28 con Calles 26 y 27',
    'No disponible',
    'No disponible',
    'http://i.imgur.com/3Nxt5Ra.jpg',
    'No disponible',
    maps['M5i5NihUe1Q2']
)

lugares(
    'http://tulua.gov.co/?apc=m1G-1484013-1484013&x=1484013',
    'Plaza Cívica Parque de Boyacá',
    """Cuenta con espacios para la preservación de la flora y la fauna,  plaza cívica  para la celebración de los 
    acontecimientos de la comunidad tulueña""",
    'Calle 26 con Carrera 25, al frente de la alcaldía',
    'No disponible',
    'No disponible',
    'http://i.imgur.com/vjn1yxv.jpg',
    'No disponible',
    maps['ne9gP1wbxK92']
)

lugares(
    'http://www.eltiempo.com/archivo/documento/MAM-689648',
    'Museo Vial Internacional Bernal Esquivel',
    """Se pueden observar al lado del río algunas obras del pintor y escultor tulueño Angel Bernal Esquivel""",
    'Bulevar el río, a orillas del río Tuluá',
    'No disponible',
    'No disponible',
    'http://i.imgur.com/RwG1Ft2.jpg',
    'No disponible',
    maps['vxqvZiA8qZk']
)

lugares(
    'http://wikimapia.org/31342856/es/Humedal-Charco-de-Oro',
    'Humedal Charco de Oro',
    """Humedal afectado por la expansión de las fronteras agrícolas""",
    'Corregimiento Campoalegre',
    'No disponible',
    'No disponible',
    'http://i.imgur.com/b0aTDPQ.png',
    'No disponible',
    maps['T33fhUWuf3x']
)

lugares(
    'http://wikimapia.org/31342849/es/Humedal-La-Bolsa',
    'Humedal La Bolsa',
    """Humedal afectado por la expansión de las fronteras agrícolas""",
    'Corregimiento Campoalegre',
    'No disponible',
    'No disponible',
    'http://i.imgur.com/boarCCq.png',
    'No disponible',
    maps['T33fhUWuf3x']
)

#print (gRutaMaiz.serialize(format="pretty-xml")) 


