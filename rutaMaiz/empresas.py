#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rdflib import Namespace, URIRef, Literal, Graph, BNode
from rdflib.namespace import RDF, RDFS, FOAF
from ontologias import GR, VCARD

ge = Graph()
#Namespace necesarios
facebook = Namespace('https://www.facebook.com/')
twitter = Namespace('https://www.twitter.com/')
dbr = Namespace('http://dbpedia.org/resource/')

# Esquema del grafo para empresas de la ruta del maíz.
def empresas(uri, nombre, tel, imagen, blank_node, ciudad, descripcion, direcc, email, webpage):
	ge.add( (URIRef(uri), RDF.type, GR.Location) )
	ge.add( (URIRef(uri), GR.name, Literal(nombre)) )
	ge.add( (URIRef(uri), GR.description, Literal(descripcion)))
	ge.add( (URIRef(uri), VCARD.tel, Literal(tel)) )
	ge.add( (URIRef(uri), VCARD.address ,BNode(blank_node)) )
	ge.add( (BNode(blank_node), RDF.type, VCARD.Address) )
	ge.add( (BNode(blank_node), VCARD['country-name'], Literal('Colombia')) )
	ge.add( (BNode(blank_node), VCARD['locality'], Literal(ciudad)) )
	ge.add( (URIRef(uri), VCARD['street-address'], Literal(direcc)))
	ge.add( (URIRef(uri), VCARD.email, Literal(email)) ) 
	ge.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)) )

empresas(
	facebook['AGROCORVALLE'],
	'Agroindustria Oleaginosa Corazon del Valle',
	'314 854 1375, 316 274 2948, 317 624 7417',
	'http://i.imgur.com/iVHRK2g.jpg',
	'bn_agrocorvalle',
	'Campoalegre',
	"""Dedicada al cultivo y transformación de 
	frutos de plantas oleaginosas principalmente la SACHA INCHI
	con cadenas productivas 100% organicas""",
	'No disponible',
	'sicorazondelvalle@gmail.com',
	'https://www.agrocorvalle.com'
)

empresas(
	facebook['pages/Ingenio-Sancarlos-SA/624707384217059'],
	'Ingenio San Carlos',
	'57 (2) 2311515',
	'http://i.imgur.com/IwXka7i.png',
	'bn_ingenio',
	'Via Riofrio Km. 7 Palomestizo',
	"""Empresa agroindustrial dedicada al cultivo de caña
	y su transformación en azúcares, mieles, energía limpia y otros derivados""",
	'No disponible',
	'No disponible',
	'http://www.ingeniosancarlos.com.co/' 
)

empresas(
	facebook['ViveroElRosaltulua'],
	'Vivero El Rosal',
	'225 71 51, 231 34 40, 231 97 19, 316 554 2035',
	'http://i.imgur.com/OicbmG7.jpg',
	'bn_rosal',
	'Via Tulua - Riofrio',
	'Empresa dedicada a la producción, comercialización y distribución de plantas ornamentales',
	'Calle 27 No. 3 Oeste 52',
	'No disponible',
	'http://www.viveroelrosal.com/'
)

empresas(
	facebook['pages/La-Herradura/10401777341'],
	'Centro Comercial La Herradura',
	'2249507',
	'http://i.imgur.com/yXlawlm.png',
	'bn_herradura',
	'Tuluá',
	"""Centro comercial del Corazon de Valle del Cauca donde encuentras plazoleta de comidas,
	bares, tiendas, cine, eventos y mas""",
	'Carrera 19 No. 28 - 76',
	'No disponible',
	'http://www.laherradura.com.co/'
)

empresas(
	facebook['centrocomercialtuluala14'],
	'Centro Comercial Tuluá La 14',
	'2308640',
	'http://i.imgur.com/d6zxnQe.jpg',
	'bn_la14',
	'Tuluá',
	"""Centro empresarial, comercial y de negocios, epicentro de una permanente actividad social
	y el lugar de encuentro favorito de las familias centro vallecaucanas""",
	'Carrera. 40 No. 37-51',
	'No disponible',
	'http://centrocomercialtulua.com/'
)

empresas(
	facebook['pages/Projugos-Tulua/403454439767813'],
	'Productora de Jugos S.A.S',
	'235 6100, 225 3153',
	'http://i.imgur.com/68cCsff.jpg',
	'bn_projugos',
	'Tuluá',
	"""Centro comercial del Corazon de Valle del Cauca donde encuentras plazoleta de comidas,
	bares, tiendas, cine, eventos y mas""",
	'Calle 48 No. 21 - 100',
	'info@projugos.com',
	'http://www.projugos.com/'
)

empresas(
	facebook['pages/Levapan-Tulua/481467405286461'],
	'Levapan S.A',
	'2241688',
	'http://i.imgur.com/x9N7Moc.jpg',
	'bn_levapan',
	'Tuluá',
	"""Moderna y tecnificada planta de producción de levadura""",
	'Carrera 27 A No. 40-470',
	'No disponible',
	'http://www.levapan.com/'
)

empresas(
	facebook['Agregar-centro-aguas-tulua/446894565390492'],
	'Centroaguas S.A . E.S.P',
	'2317070',
	'http://i.imgur.com/Dqh8Z8Y.jpg',
	'bn_centroaguas',
	'Tuluá',
	"""Purificación y distribucion de agua, para uso domestico y comercial""",
	'Carrera 26  No. 26 - 15',
	'info@centroaguas.com',
	'http://www.centroaguas.com/'
)

empresas(
	facebook['pages/Compa%C3%B1ia-de-Electricidad-de-Tulua-CETSA/109217362434941'],
	'Compañia de Electricidad de Tuluá S.A. E.S.P.',
	'2339000',
	'http://i.imgur.com/4KSaIUz.jpg',
	'bn_cetsa',
	'Tuluá',
	"""Comercialización de energía eléctrica""",
	'Calle 29 No. 23 - 45',
	'mlasso@cetsa.com.co',
	'http://www.cetsa.com.co'
)
empresas(
	facebook['pages/trans-tobar-tulua/127752540643366'],
	"Empresa de Transportes Tobar Limitada 'Transtobar'",
	'2242199',
	'http://i.imgur.com/HbJ0Oh2.jpg',
	'bn_tobar',
	'Tuluá',
	"""Transporte metropolitano colectivo regular de pasajeros""",
	'Cr. 8 No. 26 B - 01',
	'transtobartulua@gmail.com',
	'No disponible'
)
empresas(
	facebook['pages/Terminal-de-transportes-Tulu%C3%A1/413459778666424'],
	'Central de Transportes de Tuluá S.A.',
	'2245779, 2251477',
	'http://i.imgur.com/aKdj3Oq.jpg',
	'bn_terminal',
	'Tuluá',
	"""Transporte intermunicipal""",
	'Carrera 20 No. 26 - 32',
	'contabilidad@terminaltulua.com',
	'http://www.terminaltulua.com/'
)
empresas(
	facebook['Industria-de-Harinas-Tulua-limitada-133301366750011/'],
	'Industria de Harinas Tuluá Limitada',
	'(57) 2245815, (57) 2251477',
	'No disponible',
	'bn_harinas',
	'Tuluá',
	"""Industria dedicada a la elaboración de harina de trigo fortificada
	y sus derivados como la sémola, semolatto, salvado, mogolla, harina de
	tercera y harina integral""",
	'Carrera 28 No 32-54',
	'No disponible',
	'http://harinastulua.com/'
)
empresas(
	dbr['Banco_Popular_(Colombia)'],
	'Banco Popular agencia Tuluá',
	'2243997',
	'No disponible',
	'bn_popular',
	'Tuluá',
	"""Sede del Banco Poupular de la ciudad de Tuluá""",
	'Carrera 25 No. 27 - 92',
	'tulua@bancopopular.com.co',
	'http://www.bancopopular.com.co/'
)
empresas(
	dbr['Banco_de_Bogotá'.decode('utf8')],
	'Banco de Bogotá agencia Tuluá',
	'2244222',
	'http://i.imgur.com/byJtPab.jpg',
	'bn_bogota',
	'Tuluá',
	"""Sede del Banco de Bogotá de la ciudad de Tuluá""",
	'Carrera 26  No. 27 -32',
	'jds612@bancodebogota.com',
	'http://www.bancodebogota.com/'
)
empresas(
	dbr['Banco_de_Occidente_Credencial'],
	'Banco de Occidente agencia Tuluá',
	'2243997',
	'http://i.imgur.com/bBw3z7f.png',
	'bn_occidnete',
	'Tuluá',
	"""Sede del Banco de Occidente de la ciudad de Tuluá""",
	'Carrera 25 No. 27 - 92',
	'tulua@bancopopular.com.co',
	'http://www.bancopopular.com.co/'
)
empresas(
	dbr['Bancolombia'],
	'Bancolombia Tulua',
	'2319905',
	'http://i.imgur.com/TOTbhR5.jpg',
	'bn_bcol',
	'Tuluá',
	"""Sede de Bancolombia de la ciudad de Tuluá""",
	'Carrera 26 No. 26 - 20',
	'No disponible',
	'http://www.grupobancolombia.com/'
)
empresas(
	twitter['Ecodataset/status/707056997326311424'],
	'Artesanías y Vivero El Jazmín',
	'2321193',
	'http://i.imgur.com/9OiB5aZ.png',
	'bn_jazmin',
	'Tuluá',
	"""Comercialización de plantas y artesanías""",
	'Calle 31 Nro. 38-45',
	'viverojazmin@gmail.com',
	'http://www.viveroeljazmin.com/'
)
empresas(
	twitter['Ecodataset/status/707060058031595520'],
	'Bioverti',
	'3133000914',
	'http://i.imgur.com/IMbLvj6.jpg',
	'bn_bioverti',
	'Tuluá',
	"""Cultivo de hortalizas, raíces y tubérculos""",
	'Calle 26 No. 36-32 Apto 201',
	'anyel176@hotmail.com',
	'No disponible'
)

print (ge.serialize(format="pretty-xml"))