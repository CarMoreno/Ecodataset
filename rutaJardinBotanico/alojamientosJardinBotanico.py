# -*- coding: utf-8 -*-
from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from ontologias import GR, VCARD, ACCO, UMBEL

facebook = Namespace('https://www.facebook.com/')
twitter = Namespace('https://www.twitter.com/Ecodataset/status/')
dbr = Namespace('http://dbpedia.org/resource/')
alcaldiaTulua = Namespace('http://www.tulua.gov.co/sitio.shtml?apc=m1r1--&x=') #Habitaciones
ciudadGuru = Namespace('http://www.ciudadguru.com.co/empresas/') #Valores
hoteles = Namespace('http://hotel-az.com/viajes-turismo/tulua/')
turismoTulua = Namespace('http://rnttulua.confecamaras.co/detalle-establecimiento/') #Camas - Registro Nacional de Turismo
imgur = Namespace('http://i.imgur.com/')
maps = Namespace('https://goo.gl/maps/')
gAlojamientosJardin = Graph()


def alojamientos(uri, nombre, webpage, telefono, email, direcc, mapa, descripcion, uriRoom, uriValue, 
	uriBed, numHabitaciones, numCamas, imagen):
	if webpage == "No disponible":
		gAlojamientosJardin.add( (URIRef(uri), FOAF.homepage, Literal(webpage)))
	else:
		gAlojamientosJardin.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)))	
			
	gAlojamientosJardin.add( (URIRef(uri), RDF.type, ACCO.Hotel))
	gAlojamientosJardin.add( (URIRef(uri), RDF.type, GR.Individual) )
	gAlojamientosJardin.add( (URIRef(uri), GR.name, Literal(nombre)) )
	gAlojamientosJardin.add( (URIRef(uri), GR.description, Literal(descripcion)) )
	gAlojamientosJardin.add( (URIRef(uri), VCARD.tel, Literal(telefono)))
	gAlojamientosJardin.add( (URIRef(uri), VCARD.email, Literal(email)))
	gAlojamientosJardin.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
	gAlojamientosJardin.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))

	#Dirección según vCard 2006
	gAlojamientosJardin.add( (URIRef(mapa), RDF.type, VCARD.Address) )
	gAlojamientosJardin.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia')) )
	gAlojamientosJardin.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá')) )
	gAlojamientosJardin.add( (URIRef(mapa), VCARD['street-address'], Literal(direcc)) )

	#Horario de Atención
	gAlojamientosJardin.add( (URIRef(uri), ACCO.feature, ACCO.AccommodationFeature) )
	gAlojamientosJardin.add( (ACCO.AccommodationFeature, ACCO.availabilityTimes, Literal("24 Horas")) )

	#Habitaciones
	gAlojamientosJardin.add( (URIRef(uriRoom), RDF.type, ACCO.HotelRoom))
	gAlojamientosJardin.add( (URIRef(uriRoom), RDF.type, GR.SomeItems) )
	gAlojamientosJardin.add( (URIRef(uriRoom), ACCO.partOf, URIRef(uri)) )

	#Value
	gAlojamientosJardin.add( (URIRef(uriValue), RDF.type, GR.QuantitativeValue))
	gAlojamientosJardin.add( (URIRef(uriRoom), ACCO.numberOfRooms, URIRef(uriValue)) )
	gAlojamientosJardin.add( (URIRef(uriValue), GR.hasUnitOfMeasurement, Literal("C62"))) #No hay unidades
	gAlojamientosJardin.add( (URIRef(uriValue), GR.hasValue, Literal(numHabitaciones, datatype=XSD.int)))

	#Camas

	gAlojamientosJardin.add( (URIRef(uriBed), RDF.type, ACCO.BedDetails))
	gAlojamientosJardin.add( (URIRef(uriRoom), ACCO.bed, URIRef(uriBed)))
	gAlojamientosJardin.add( (URIRef(uriBed), ACCO.quantity, Literal(numCamas, datatype=XSD.int)))

	#gAlojamientosJardin.add( (URIRef(uri), VCARD.cateogry, Literal("Alojamientos de la Ruta del Maíz")))
	#gAlojamientosJardin.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaMaiz.Alojamientos)))

alojamientos(
	facebook['jbjuanmariacespedes'] ,#uribed
	'Jardín Botánico Juán María Céspedes',
	'http://inciva.gov.co/patrimonios-turisticos/jardin-botanico-juan-maria-cespedes-tulua/',
	'3206888271, 3156361319, 5146848',
	'jardinbotanico@inciva.gov.co',
	'Corregimiento de Mateguadua, 763028 Tuluá', #direccion
	maps['hRdkwZBgae22'],
	"""El Jardín Botánico Juan María Céspedes es un centro de investigaciones del Instituto para
	la Investigación y la Preservación del Patrimonio Cultural y Natural del Valle del Cauca - INCIVA.""",
	'http://www.livevalledelcauca.com/tulua/jardin-botanico-juan-maria-cespedes.html',
	ciudadGuru['jardin-botanico-juan-maria-cespedes-tulua/tulua/15952821'],
	facebook['pages/Jardin-Botánico-Juan-Maria-Céspedes/193724564145315'.decode('utf8')],
	'2',#NumHabitaciones
	'8',#NumCamas
	'http://i.imgur.com/QCAEQ1y.jpg',
)

print(gAlojamientosJardin.serialize(format='pretty-xml'))