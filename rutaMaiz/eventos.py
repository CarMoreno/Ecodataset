#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rdflib import Namespace, URIRef, Literal, Graph, BNode
from rdflib.namespace import RDF, RDFS, DC
from ontologias import GR, VCARD, EVENT, UMBEL
from empresas import gRutaMaiz, rutaMaiz
#Namespace necesarios
rutaMaizEventos = Namespace('http://190.14.254.237/dataseteco/RutaDelMaiz/Eventos/')

def eventos(uri, nombre, fecha, descripcion, lugar, media):
	gRutaMaiz.add(( URIRef(uri), RDF.type, EVENT.Event ) )
	gRutaMaiz.add(( URIRef(uri), EVENT.atTime, Literal(fecha, datatype=XSD.date)) )
	gRutaMaiz.add(( URIRef(uri), EVENT.atPlace, Literal(lugar)) )
	gRutaMaiz.add(( URIRef(uri), EVENT.illustrate, URIRef(media)) )
	gRutaMaiz.add(( URIRef(uri), RDFS.label, Literal(nombre)) )
	gRutaMaiz.add(( URIRef(uri), RDFS.comment, Literal(descripcion)) )# se cambio DC por RDFS
	gRutaMaiz.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaMaiz.Eventos)) )

eventos(
	'https://www.youtube.com/watch?v=gQn35OZVAM0',
	'Fiesta de los Años Dorados',
	'Mes de Junio de todos los años',
	'Evento celebrado como antesala de la feria',
	'Coliseo cubierto de la I.E. Corazón del Valle de la cuidad de Tuluá',
	rutaMaizEventos['FIESTADORADOS.mp4']
)

eventos(
	'https://www.youtube.com/watch?v=r94lfflAeMQ',
	'Desfile de Bandas Músico-marciales',
	'Mes de Junio de todos los años',
	'Con la participación de bandas provenientes del municipio de Tuluá y de otros municipios',
	'Tuluá',
	'http://i.imgur.com/yus7d2D.jpg'
)

eventos(
	'http://www.tulua.gov.co/index.shtml?apc=G1-1--&x=1520089',
	'Carnaval de Orejitas',
	'Mes de Junio de todos los años',
	'Evento celebrado como antesala de la feria de Tuluá',
	'Tuluá',
	'http://i.imgur.com/mF90nnF.jpg'
)

eventos(
	'http://tulua.gov.co/index.shtml?apc=G1-1--&x=1523520',
	'Velada Boxística',
	'Mes de Junio, todos los años',
	'Evento celebrado como antesala de la feria de Tuluá',
	'Coliseo Multipropósito del Coliseo de Ferias de Tuluá',
	rutaMaizEventos['Boxeo.mp4']
)

eventos(
	'http://www.eltabloide.com.co/carnaval-de-orejones/',
	'Carnaval de Orejones',
	'Mes de Junio, todos los años',
	'Evento celebrado como antesala de la feria de Tuluá',
	'Tuluá',
	'http://i.imgur.com/f7hcZMr.jpg'
)

eventos(
	'https://www.facebook.com/feriadetuluaoficial/',
	'Feria de Tuluá',
	'Mes de Junio de todos los años',
	"""La programación es variada y hay para todos los gustos, desde lo agropecuario,
	ganadero, artesanal hasta las presentaciones de artistas nacionales e internacionales
	de manera simultánea en cinco escenarios diferentes de la ciudad.""",
	'Tuluá',
	'http://i.imgur.com/Q9EgLz2.jpg'
)

eventos(
	'https://www.facebook.com/encuentro.deestudiantinas.94/',
	"Encuentro Nacional de Estudiantinas 'Hector Cedeño'",
	'Noviembre 13 al 15',
	"""Tiene como objetivo preservar la memoria del Maestro Hector Cedeño y difundir la música andina
	colombiana interpretada por estudiantinas. La programación del evento incluye la presentación de
	las Estudiantinas participantes del Encuentro en diferentes espacios públicos con libertad de acceso
	gratuito. Las Estudiantinas interesadas en participar deben inscribirse previamente en el Departamento
	de Arte y Cultura del Municipio en el telefax 2-2243560 ó al E-mail: arteycultura@tulua.gov.co""",
	'Parque Lineal Juan María Céspedes de Tuluá',
	'http://i.imgur.com/ziCJBhU.jpg'
)

eventos(
	'https://www.youtube.com/watch?v=pgSI7A01bWg',
	'Festival del Mate, el Guarapo y la Música Autóctona',
	'Segunda semana del mes de Agosto de cada año',
	"""El Festival del Mate y El Guarapo es un tradicional evento tulueño que rescata y preserva las raices
	culturales cultivando el amor por nuestra música, además reúne a buena parte de los grupos de música andina
	y latinoamericana de la región en un solo concierto de identidad. Los grupos musicales interesados deben
	inscribirse con antelación con la Junta Administradora del Festival""",
	'UNIVALLE TULUA, Calle 42 Cra 32',
	rutaMaizEventos['mate.mp4']
)

eventos(
	'http://www.tulua.gov.co/sitio.shtml?apc=B1--1481401-1481401&x=1480722',
	'Festival del Río Tuluá',
	'Segunda semana del mes de octubre de cada año',
	"""Durante el Festival se realiza la venta de platos típicos de la región, bebidas y dulces típicos,
	se practican juegos típicos de la zona, campeonatos de Voleyplaya, ciclomontañismo, competencias en
	triciclos y en patines, concurso de pintura para los niños, competencias en neumáticos por el lecho
	del río Tuluá, se presentan artistas en tarima y se realizan actividades de limpieza. El objeto del
	festival es generar sentido de pertenencia hacia el río Tuluá.""",
	'Costado del lecho del Río Tuluá, entre las calles 38 y 42 del barrio Fátima.',
	rutaMaizEventos['FestivalRio.mp4']
)

eventos(
	'http://www.tulua.gov.co/sitio.shtml?apc=B1-1--&x=1480719',
	'Festival Regional de Cometas Club Rotario Tuluá',
	'Segundo Domingo del mes de Agosto',
	""" La programación incluye exposición y premiación de las mejores cometas (según su complejidad de
	elaboración, diseño y tamaño), presentaciones artísticas en Tarima. A este Festival acuden cada año
	cerca de 1.000 expositores de cometas y aproximadamente 12.000 visitantes y observadores. En el marco
	del festival se hace una exposición Aérea de paracaidistas y ultralivianos, por parte de la Fuerza Aérea
	Colombiana.""",
	'Cra. 30 cerca a Tránsito Municipal de Tuluá',
	'http://i.imgur.com/8fIkCUN.jpg'
)

eventos(
	'http://www.sancochofest.co/',
	'Sancocho Fest',
	'Primer fin de semana del mes de febrero de cada año',
	"""Es un festival cultural que nace como un llamado a la tolerancia y al respeto en la ciudad, evento gratuito
	que intenta mostrar lo mejor de propuestas emergentes en el área de la música, cine, fotografía, poesía
	donde pueden participar y asistir todas las personas amantes de la cultura""",
	'Parque Lineal Juan María Céspedes de Tuluá',
	'http://i.imgur.com/CcGKhZF.jpg'
)

eventos(
	'http://www.tulua.gov.co/sitio.shtml?apc=C1v16--&x=1517450',
	'Fiestas de la Ruta del Maíz',
	'No disponible',
	"""Comprende la gastronomía en torno de productos hechos a base de maíz""",
	'Corregimiento Campoalegre',
	'http://i.imgur.com/5shLwWm.jpg'
)
# print (gRutaMaiz.serialize(format="pretty-xml"))	