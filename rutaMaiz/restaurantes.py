#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, FOAF
from ontologias import GR, VCARD, UMBEL
from lugares import gRutaMaiz, rutaMaiz

facebook = Namespace('https://www.facebook.com/')
twitter = Namespace('https://www.twitter.com/')
maps = Namespace('https://goo.gl/maps/')
alcaldiaTulua = Namespace('http://www.tulua.gov.co/sitio.shtml?apc=m1r1--&x=')

def restaurantes(uri, nombre, menu, telefono, direccion, webpage, imagen, mapa, uriatencion, abre, cierra):
    if webpage == "No disponible":
        gRutaMaiz.add( (URIRef(uri), FOAF.homepage, Literal('No disponible')) )
    else:
        gRutaMaiz.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)) )
            
    gRutaMaiz.add( (URIRef(uri), RDF.type, GR.Location) )
    gRutaMaiz.add( (URIRef(uri), GR.name, Literal(nombre)) )
    gRutaMaiz.add( (URIRef(uri), GR.description, Literal(menu)))
    gRutaMaiz.add( (URIRef(uri), VCARD.tel, Literal(telefono)) )
    gRutaMaiz.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) )
    gRutaMaiz.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))
    gRutaMaiz.add( (URIRef(uri), GR.hasOpeningHoursSpecification, URIRef(uriatencion)) )
     
    #Dirección según vCard 2006
    gRutaMaiz.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    gRutaMaiz.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia')) )
    gRutaMaiz.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá')) )
    gRutaMaiz.add( (URIRef(mapa), VCARD['street-address'], Literal(direccion)) )

    #Horario de atencion
    gRutaMaiz.add( (URIRef(uriatencion), RDF.type, GR.OpeningHoursSpecification) )
    gRutaMaiz.add( (URIRef(uriatencion), GR.opens, Literal(abre, datatype=XSD.time)) )#Se especifica el tipo de dato
    gRutaMaiz.add( (URIRef(uriatencion), GR.closes, Literal(cierra, datatype=XSD.time)) )
    gRutaMaiz.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Monday) )
    gRutaMaiz.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Tuesday) )
    gRutaMaiz.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Wednesday) )
    gRutaMaiz.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Thursday) )
    gRutaMaiz.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Friday) )
    gRutaMaiz.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Saturday) )
    gRutaMaiz.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Sunday) )

    gRutaMaiz.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaMaiz.Restaurantes)))

restaurantes(
    twitter['Ecodataset/status/715737460697931776'],
    'Hacienda La Leonora',
    """Tamal Valluno, subidos de maíz, cordero asado, chicha de maíz, ajiaco bogotano, manjar  blanco, 
    envueltos de choclo, natilla de maíz.""",
    '3116404505, 3152689558',
    'Corregimiento Campoalegre',
    'No disponible',
    'http://i.imgur.com/VeoLHUb.jpg',
    maps['xduJAL6Guy52'],
    "https://www.youtube.com/watch?v=q0UgTCZa1bE",
    "09:00:00",
    "18:00:00"
)#con imagen por defecto

restaurantes(
    twitter['Ecodataset/status/741127397727162368'],
    'El Ocaso',
    """Torta de maíz, chorizo campesino, chancarina, fiambre valluno.""",
    '3122502184',
    'Corregimiento Campoalegre',
    'No disponible',
    'http://i.imgur.com/VeoLHUb.jpg',
    maps['negZQ2kbGjm'],
    "https://www.youtube.com/watch?v=q0UgTCZa1bE",
    "09:00:00",
    "18:00:00"
)#con imagen por defecto

restaurantes(
    twitter['Ecodataset/status/741129909305761794'],
    'Los Almendros',
    """Ancas de rana, macho rucio, champús de maíz con frutas tropicales.""",
    '3152768355',
    'Corregimiento Campoalegre',
    'No disponible',
    'http://i.imgur.com/VeoLHUb.jpg',
    maps['iPprdddk6AR2'],
    "https://www.youtube.com/watch?v=q0UgTCZa1bE",
    "09:00:00",
    "18:00:00"
)#con imagen por defecto

restaurantes(
    twitter['Ecodataset/status/741132208879079424'],
    'La Cabañuela',
    """cerdo de raza Zungo, plato con media gallina sudada, refrescante aperitivo sirope acompañado 
    con ricos platos mexicanos.""",
    '3175935835',
    'Corregimiento Campoalegre',
    'No disponible',
    'http://i.imgur.com/VeoLHUb.jpg',
    maps['GoRsVqBHHKU2'],
    "https://www.youtube.com/watch?v=q0UgTCZa1bE",
    "09:00:00",
    "18:00:00"
)#con imagen por defecto

restaurantes(
    twitter['Ecodataset/status/741133124176912384'],
    'El Jardín',
    """Tradicional sancocho de gallina hecho en fogón de leña,  mazamorra de maíz.""",
    '3178767249',
    'Corregimiento Campoalegre',
    'No disponible',
    'http://i.imgur.com/VeoLHUb.jpg',
    maps['iBs1aDqjjZt'],
    "https://www.youtube.com/watch?v=q0UgTCZa1bE",
    "09:00:00",
    "18:00:00"
)#con imagen por defecto

restaurantes(
    twitter['Ecodataset/status/741135052847874049'],
    'Finca La Benilda',
    """Trasnochado de maíz, mazorcas de choclo asado, bandeja paisa, masato de maíz, arepas de choclo.""",
    '3104540005, 3182190336',
    'Corregimiento Campoalegre',
    'No disponible',
    'http://i.imgur.com/VeoLHUb.jpg',
    maps['sgYUQMTqwwq'],
    "https://www.youtube.com/watch?v=q0UgTCZa1bE",
    "09:00:00",
    "18:00:00"
)#con imagen por defecto

restaurantes(
    facebook['American-Pizza-1608357502820958/'],
    'American Pizza',
    """Jugos naturales, Lasañas, Churrasco, Ensaladas de Frutas, Sandwich, Malteadas, Pancerotes, 
    Ensaladas, Comidas Rápidas.""",
    '224 0055, 224 6515',
    'Carrera 28 Calle 30 Esquina, Cra 23 Nº24–64, C.C. La Herradura',
    'http://www.americanpizza.com.co/',
    'http://i.imgur.com/UoeDHRA.jpg',
    maps['aD6R6DSjix62'],
    alcaldiaTulua['1475546'],
    "14:00:00",
    "23:00:00"
)

restaurantes(
    'http://www.aquieselpaisatulua.com/file/menu-aqui-es-el-paisa.pdf',
    'Aquí es el Paisa',
    """Lleva más de diecisiete años deleitando el paladar de los tulueños con comida típica, buena mesa y sazón paisa.
    Ofrece los mejores platos antioqueños, asados al carbón, comida gourmet, comidas rápidas, deliciosas y variadas picadas.""",
    '225 63 73, 320 711 3313, 316 478 8008',
    'Carrera 26 No. 38 - 144',
    'http://www.aquieselpaisatulua.com/',
    'http://i.imgur.com/y7LetOi.jpg',
    maps['LzCHbGg7FVt'],
    alcaldiaTulua['1475518'],
    "17:00:00",
    "01:00:00"
)

restaurantes(
    facebook['rancho.panorama/?fref=ts'],
    'Rancho Panorama',
    """Ofrece tilapias, bocachicos en salsa agridulce, champiñones al natural, sancocho 
    de pescado,jugos naturales, arepas, arroz, plátano.""",
    '225 78 38, 300 619 41 47, 316 4474977',
    'Carrera 40, La Variante Km. 1 vía Tuluá - Andalucía',
    'http://www.ranchopanorama.com/',
    'http://i.imgur.com/mKGptIs.jpg',
    maps['GpBCXuJiqZ82'],
    alcaldiaTulua['1475534'],
    "07:00:00",
    "23:00:00"
)

restaurantes(
    alcaldiaTulua['1475516'],
    'Restaurante y Panadería La 26',
    """Asadero y panadería. Expertos en la elaboración de gran variedad de productos alimenticios pero en especial
    POLLO ASADO Y APANADO.""",
    '225 27 91',
    'Carrera 26 No. 26 - 55',
    'No disponible',
    'http://i.imgur.com/VeoLHUb.jpg',
    maps['BSZnHjrLkW22'],
    "http://www.amarillascolombia.co/colombia/tulua/restaurantes/pollos-asados-mario-195432",
    "07:00:00",
    "20:00:00"
)#con imagen por defecto

restaurantes(
    facebook['pages/Restaurante-El-Rincón-Costeño/1497339127212455?fref=ts'.decode('utf8')],
    'Rincón Costeño',
    """Ofrece deliciosa comida de mar, comida costeña, cazuela de mariscos.""",
    '224 10 54',
    'Calle 25 No. 22 - 51',
    'No disponible',
    'http://i.imgur.com/AXpED2P.jpg',
    maps['f9yB84FSLT22'],
    alcaldiaTulua['1475514'],
    "09:30:00",
    "21:30:00"
)

restaurantes(
    facebook['groups/57057973652/?fref=nf'],
    'Santa Lucía Gourmet Restaurante Bar',
    """Ofrece la mejor cocina típica del Centro del Valle e internacional dentro de un ambiente campestre y familiar.""",
    '224 44 05, 301 2295291',
    'Carrera 40 calle 17 B - La Variante',
    'No disponible',
    'http://i.imgur.com/awE45sO.jpg',
    maps['nNKSLnqPFVQ2'],
    alcaldiaTulua['1475527'],
    "07:00:00",
    "21:00:00"
)

restaurantes(
    facebook['pages/Sebastián-Parrilla/675857662453037'.decode('utf8')],
    'Sebastián Parrilla',
    """Asadero, deliciosos Chorizos de San Rafael los mejores de Tuluá.""",
    '226 26 97',
    'Carrera 28 No. 21 - 10',
    'No disponible',
    'http://i.imgur.com/PapcNxf.jpg',
    maps['QFEESFyNmsT2'],
    alcaldiaTulua['1475526'],
    "06:00:00",
    "22:00:00"
)

restaurantes(
    facebook['Restaurante-Todo-Chuletas-Tuluá-1636237983291640/'.decode('utf8')],
    'Todo Chuletas Express Tuluá',
    """Restaurante a manteles. Ofrecemos sopas, carne, pollo, arroz, ensaladas.""",
    '224 29 79, 225 54 94',
    'Carrera 27A No. 42 - 184',
    'No disponible',
    'http://i.imgur.com/Ag2VbUV.jpg',
    maps['5yQt2Tz5eeG2'],
    alcaldiaTulua['1475523'],
    "10:00:00",
    "15:00:00"
)

restaurantes(
    facebook['uban.wagner?fref=ts'],
    'Wagner`s Coffee',
    """Delicioso café en la presentación que más te gusta, 
    acompañado de crepes, sandwich, hamburguesas, cheasecake, ... y otras delicias.""",
    '3164222259',
    'Carrera 32 No. 24-41',
    'No disponible',
    'http://i.imgur.com/p9b3Yyy.jpg',
    maps['YPjRMLgFdS92'],
    alcaldiaTulua['1512189'],
    "10:00:00",
    "21:00:00"
)

restaurantes(
    facebook['RestauranteYerbabuenaCo'],
    'Yerbabuena Restaurante Vivero',
    """Combina la calidad gastronómica y un servicio de restaurante adecuado en medio de un ambiente 
    campestre con espacios amplios y cómodos. Exquisitos platos inspirados en la gastronomía nacional e internacional.""",
    '226 23 23, 2248999, 3146616634',
    'Carrera 40 La Variante # 17B-28',
    'http://restauranteyerbabuena.co/',
    'http://i.imgur.com/qwKiXDM.png',
    maps['1GTzW5tqFYD2'],
    alcaldiaTulua['1475521'],
    "08:00:00",
    "21:00:00"
)

print (gRutaMaiz.serialize(format="pretty-xml"))   