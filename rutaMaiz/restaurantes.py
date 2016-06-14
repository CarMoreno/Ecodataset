#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, FOAF
from ontologias import GR, VCARD

facebook = Namespace('https://www.facebook.com/')
twitter = Namespace('https://www.twitter.com/')

restaurants = Graph()

def restaurantes(uri, nombre, menu, telefono, direccion, webpage, imagen):
    if webpage == "No disponible":
        restaurants.add( (URIRef(uri), FOAF.homepage, Literal('No disponible')) )
    else:
        restaurants.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)) )
            
    restaurants.add( (URIRef(uri), RDF.type, GR.BusinessEntity) )#persona natural o razon social
    restaurants.add( (URIRef(uri), GR.category, Literal('Restaurantes Ruta del Maíz en Campoalegre')) )
    restaurants.add( (URIRef(uri), GR.name, Literal(nombre)) )
    restaurants.add( (URIRef(uri), GR.description, Literal(menu)))
    restaurants.add( (URIRef(uri), VCARD.tel, Literal(telefono)) )
    restaurants.add( (URIRef(uri), VCARD['street-address'], Literal(direccion)))
    restaurants.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) ) 

restaurantes(
    twitter['Ecodataset/status/715737460697931776'],
    'Hacienda La Leonora',
    """Tamal Valluno, Subidos de Maíz, Cordero Asado, Chicha de Maíz, Ajiaco Bogotano, Manjar  Blanco, 
    Envueltos de Choclo, Natilla de Maíz""",
    '3116404505, 3152689558',
    'Corregimiento Campoalegre',
    'No disponible',
    'http://i.imgur.com/VeoLHUb.jpg')#con imagen por defecto

restaurantes(
    twitter['Ecodataset/status/741127397727162368'],
    'El Ocaso',
    """Torta de Maíz, Chorizo Campesino, Chancarina, Fiambre Valluno""",
    '3122502184',
    'Corregimiento Campoalegre',
    'No disponible',
    'http://i.imgur.com/VeoLHUb.jpg')#con imagen por defecto

restaurantes(
    twitter['Ecodataset/status/741129909305761794'],
    'Los Almendros',
    """Ancas de Rana, Macho Rucio, Champús de Maíz con Frutas Tropicales""",
    '3152768355',
    'Corregimiento Campoalegre',
    'No disponible',
    'http://i.imgur.com/VeoLHUb.jpg')#con imagen por defecto

restaurantes(
    twitter['Ecodataset/status/741132208879079424'],
    'La Cabañuela',
    """Cerdo de raza Zungo, Plato con Media Gallina Sudada, Refrescante Aperitivo Sirope acompañado 
    con ricos Platos Mexicanos""",
    '3175935835',
    'Corregimiento Campoalegre',
    'No disponible',
    'http://i.imgur.com/VeoLHUb.jpg')#con imagen por defecto

restaurantes(
    twitter['Ecodataset/status/741133124176912384'],
    'El Jardín',
    """Tradicional Sancocho de Gallina hecho en fogón de leña,  Mazamorra de Maíz""",
    '3178767249',
    'Corregimiento Campoalegre',
    'No disponible',
    'http://i.imgur.com/VeoLHUb.jpg')#con imagen por defecto

restaurantes(
    twitter['Ecodataset/status/741135052847874049'],
    'Finca La Benilda',
    """Trasnochado de Maíz, Mazorcas de Choclo asado, Bandeja Paisa, Masato de Maíz, Arepas de Choclo""",
    '3104540005, 3182190336',
    'Corregimiento Campoalegre',
    'No disponible',
    'http://i.imgur.com/VeoLHUb.jpg')#con imagen por defecto

restaurantes(
    facebook['American-Pizza-1608357502820958/'],
    'American Pizza',
    """Jugos naturales, Lasañas, Churrasco, Ensaladas de Frutas, Sandwich, Malteadas, Pancerotes, 
    Ensaladas, Comidas Rápidas""",
    '224 0055, 224 6515',
    'Carrera 28 Calle 30 Esquina, Cra 23 Nº24–64, C.C. La Herradura',
    'http://www.americanpizza.com.co/',
    'http://i.imgur.com/UoeDHRA.jpg')

restaurantes(
    'http://www.aquieselpaisatulua.com/file/menu-aqui-es-el-paisa.pdf',
    'Aquí es el Paisa',
    """Llevamos más de diecisiete años deleitando el paladar de los tulueños con comida típica, buena mesa y sazón paisa.
    Ofrecemos los mejores platos antioqueños, asados al carbón, comida gourmet, comidas rápidas, deliciosas y variadas picadas""",
    '225 63 73, 320 711 3313, 316 478 8008',
    'Carrera 26 No. 38 - 144',
    'http://www.aquieselpaisatulua.com/',
    'http://i.imgur.com/y7LetOi.jpg')

restaurantes(
    facebook['rancho.panorama/?fref=ts'],
    'Rancho Panorama',
    """Ofrecemos tilapias, bocachicos en salsa agridulce, champiñones al natural, sancocho 
    de pescado,jugos naturales, arepas, arroz, plátano.""",
    '225 78 38, 300 619 41 47, 316 4474977',
    'Carrera 40, La Variante Km. 1 vía Tuluá - Andalucía',
    'http://www.ranchopanorama.com/',
    'http://i.imgur.com/mKGptIs.jpg')

restaurantes(
    'http://www.tulua.gov.co/sitio.shtml?apc=m1r1--&x=1475516',
    'Restaurante y Panadería La 26',
    """Asadero y panadería. Especializados en la elaboración de gran variedad de productos alimenticios pero en especial
    POLLO ASADO Y APANADO""",
    '225 27 91',
    'Carrera 26 No. 26 - 55',
    'No disponible',
    'http://i.imgur.com/VeoLHUb.jpg')#con imagen por defecto

restaurantes(
    facebook['pages/Restaurante-El-Rincón-Costeño/1497339127212455?fref=ts'.decode('utf8')],
    'Rincón Costeño',
    """Ofrecemos deliciosa comida de mar, comida Costeña, Cazuela de Mariscos""",
    '224 10 54',
    'Calle 25 No. 22 - 51',
    'No disponible',
    'http://i.imgur.com/AXpED2P.jpg')

restaurantes(
    facebook['groups/57057973652/?fref=nf'],
    'Santa Lucía Gourmet Restaurante Bar',
    """Ofrecemos la mejor cocina típica del Centro del Valle e internacional dentro de un ambiente campestre y familiar""",
    '224 44 05, 301 2295291',
    'Carrera 40 calle 17 B - La Variante',
    'No disponible',
    'http://i.imgur.com/awE45sO.jpg')

restaurantes(
    facebook['pages/Sebastián-Parrilla/675857662453037?fref=ts'.decode('utf8')],
    'Sebastián Parrilla',
    """Asadero, deliciosos Chorizos de San Rafael los mejores de Tuluá""",
    '226 26 97',
    'Carrera 28 No. 21 - 10',
    'No disponible',
    'http://i.imgur.com/PapcNxf.jpg')

restaurantes(
    facebook['Restaurante-Todo-Chuletas-Tuluá-1636237983291640/'.decode('utf8')],
    'Todo Chuletas Express Tuluá',
    """Restaurante a Manteles. Ofrecemos sopas, carne, pollo, arroz, ensaladas""",
    '224 29 79, 225 54 94',
    'Carrera 27A No. 42 - 184',
    'No disponible',
    'http://i.imgur.com/Ag2VbUV.jpg')

restaurantes(
    facebook['uban.wagner?fref=ts'],
    'Wagner`s Coffee',
    """Delicioso café en la presentación que más te gusta, 
    acompañado de crepes, sandwich, hamburguesas, cheasecake, ... y otras delicias""",
    '3164222259',
    'Carrera 32 No. 24-41',
    'No disponible',
    'http://i.imgur.com/p9b3Yyy.jpg')

restaurantes(
    facebook['RestauranteYerbabuenaCo'],
    'Yerbabuena Restaurante Vivero',
    """Yerbabuena combina la calidad gastronómica y un servicio de restaurante adecuado en medio de un ambiente 
    campestre con espacios amplios y cómodos. Exquisitos platos inspirados en la gastronomía nacional e internacional""",
    '226 23 23, 2248999, 3146616634',
    'Carrera 40 La Variante # 17B-28',
    'http://restauranteyerbabuena.co/',
    'http://i.imgur.com/qwKiXDM.png')

print (restaurants.serialize(format="pretty-xml"))   