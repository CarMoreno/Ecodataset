#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rdflib import Namespace, URIRef, Literal, Graph, BNode
from rdflib.namespace import RDF, RDFS, FOAF
from ontologias import GR, VCARD, ACCO

ga = Graph()
#Namespace necesarios
facebook = Namespace('https://www.facebook.com/')
twitter = Namespace('https://www.twitter.com/')
dbr = Namespace('http://dbpedia.org/resource/')

def alojamientos(uri, nombre, webpage, telefono, email, direcc, blank_node):
	if webpage == "No disponible":
		ga.add( (URIRef(uri), FOAF.homepage, Literal(webpage)))
	else:
		ga.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)))	
			
	ga.add( (URIRef(uri), RDF.type, GR.Location) )
	ga.add( (URIRef(uri), RDF.type, ACCO.Hotel))
	ga.add( (URIRef(uri), GR.name, Literal(nombre)) )
	ga.add( (URIRef(uri), VCARD.tel, Literal(telefono)))
	ga.add( (URIRef(uri), VCARD.email, Literal(email)))
	ga.add( (URIRef(uri), VCARD.address, BNode(blank_node)))
	ga.add( (URIRef(uri), VCARD['street-address'], Literal(direcc)))
	ga.add( (BNode(blank_node), RDF.type, VCARD.Address))
	ga.add( (BNode(blank_node), VCARD['country-name'], Literal('Colombia')) )
	ga.add( (BNode(blank_node), VCARD['locality'], Literal('Tuluá')) )

alojamientos(
	facebook["hotel.trivino"],
	"Apartahotel Triviño",
	"No disponible",
	"2289631, 3164331055",
	"gerardotrivinooviedo@hotmail.com",
	"Calle 26 40sn - 120",
	"bn_trivino"
)

alojamientos(
	facebook['Apartahotel-Marques-de-la-Villa-M-337867679645873/'],
	"El Marquez De La Villa",
	"No disponible",
	"2245667, 3165244701",
	"No disponible",
	"Carrera 22 # 24 - 51",
	"bn_marques"
)

alojamientos(
	facebook['hotelcafeplaza'],
	"Hotel Cafe Plaza - C.C. Del Parque",
	"http://hotelcafeplaza.com/",
	"2246486, 2246488, 3113546020",
	"centrocomercialdelparque@hotmail.com",
	"Calle 27 # 26-60 ofi 401",
	"bn_cafeplaza"
)

alojamientos(
	facebook['Hotel-Central-Jhoanna-334144413428928'],
	"Hotel Central Johanna",
	"No disponible",
	"2243246, 2248383, 3156304788",
	"centrocomerciallascolmenas@hotmail.com",
	"Carrera 22 # 24 - 10",
	"bn_johana"
)

alojamientos(
	twitter['Ecodataset/status/702167641562214402'],
	"Hotel Cielo",
	"No disponible",
	"3006200436",
	"aruru85@hotmail.com",
	"Carrera 20 # 25 - 31",
	"bn_cielo"
)

alojamientos(
	facebook['hotelcorazondelvalle'],
	"Hotel Corazon del Valle",
	"No disponible",
	"2323208, 2256604, 3164484351, 3117998237",
	"info@hotelcorazondelvalle.com",
	"Calle 24 # 23 - 10 PISO 2",
	"bn_corazon"
)

alojamientos(
	facebook['profile.php?id=100009492184574&ref=br_rs'],
	"Hotel Don Felipe",
	"No disponible",
	"2339685, 3174074195",
	"hoteldonfelipe@hotmail.com",
	"Carrera 24 # 28 - 51",
	"bn_felipe"
)

alojamientos(
	twitter['Ecodataset/status/702168136506855427'],
	"Hotel Don Jorge La 23",
	"No disponible",
	"2259022, 3104949597",
	"james.camelo@hotmail.com",
	"Carrera 23 # 26 - 41",
	"bn_jorge"
)

alojamientos(
	facebook['people/Hotel-Don-Sebastian/100007234909156'],
	"Hotel Don Sebastian",
	"No disponible",
	"2250273, 3207255497",
	"hoteldonsebastian@outlook.es",
	"Carrera 20 # 25 - 83",
	"bn_sebastian"
)

alojamientos(
	facebook['pages/HOTEL-EL-DESCANSO-DEL-VISITANTE/229134903821536'],
	"Hotel El Descanso Del Visitante",
	"No disponible",
	"2244518, 3184395202, 2249604",
	"fabeca_23@hotmail.com",
	"Carrera 20 # 25 - 71",
	"bn_descanso"
)

alojamientos(
	facebook['pages/Jardin-del-Ed%C3%A9n/515577135188478'],
	"Hotel El Jardín Del Edén De La 26",
	"No disponible",
	"2254777, 3154889594",
	"eledenhosteria@hotmail.com",
	"Calle 26 # 26 - 39",
	"bn_jardin"
)

alojamientos(
	facebook['pages/Hotel-El-Para%C3%ADso-Ideal/155040651352392'],
	"Hotel El Paraíso Ideal",
	"No disponible",
	"2248111, 3177424939",
	"hotelparaiso13@gmail.com",
	"Carrera 22 # 25 - 90",
	"bn_paraiso"
)

alojamientos(
	facebook['maricel.pupiales/about'],
	"Hotel Escalinata Pupi",
	"No disponible",
	"2241782, 3207561454",
	"hotelescalinata@hotmail.com",
	"Carrera 27A # 34 - 30",
	"bn_escalinata"
)

alojamientos(
	facebook['Hotel-Juan-Maria-1458858754370044/?fref=ts'],
	"Hotel Juan Maria",
	"http://hoteljuanmaria.com/",
	"2244562, 3154902380",
	"administracion@hoteljuanmaria.com",
	"Carrera 28 # 27 - 10",
	"bn_juanmaria"
)

alojamientos(
	twitter['Ecodataset/status/702168954102530048'],
	"Hotel La Estrella De La Maniana",
	"No disponible",
	"2244639, 2240452, 3103725051",
	"leonelly.7@hotmail.com",
	"Calle 25 # 20 - 49",
	"bn_estrella"
)

alojamientos(
	facebook['pages/Hotel-La-Mancion-del-Sol/248019025357779?rf=820075471383988'],
	"Hotel La Mansion Del Sol",
	"No disponible",
	"22320809, 3113378579",
	"hotel_lamansiondelsol@hotmail.com",
	"Calle 26 # 22 - 17 PISO 2",
	"bn_sol"
)

alojamientos(
	twitter['Ecodataset/status/702169670200201216'],
	"Hotel La Siesta",
	"No disponible",
	"2256828, 3207090919",
	"valensan_15@hotmail.com",
	"Carrera 20 # 25 - 95",
	"bn_siesta"
)

alojamientos(
	twitter['Ecodataset/status/702170175773270019'],
	"Hotel Los Corales Del Corazon Del Valle",
	"No disponible",
	"2261771, 3155753404",
	"gerencia@hotelcorales.com",
	"Carrera 21 # 25 - 59",
	"bn_corales"
)

alojamientos(
	facebook['hotelloscristales.detulua?ref=br_rs'],
	"Hotel Los Cristales",
	"No disponible",
	"2258463, 2246499, 3153520902",
	"administracion@loscristales-hotel.com",
	"Calle 27 # 26 - 50",
	"bn_cristales"
)

alojamientos(
	twitter['Ecodataset/status/702170493336612864'],
	"Hotel Mariscal Sucre D.F.G",
	"No disponible",
	"2244065, 3174296588",
	"g.amta78@hotmail.com",
	"Carrera 24 # 27 - 76",
	"bn_cristales",
)

alojamientos(
	facebook['hotelmorfeo/timeline?ref=page_internal'],
	"Hotel Morfeo",
	"No disponible",
	"2242520, 2248383, 3156304788",
	"centrocomerciallascolmenas@hotmail.com",
	"Calle 25 # 22 - 33",
	"bn_morfeo"
)

alojamientos(
	twitter['Ecodataset/status/702170787411787782'],
	"Hotel Plaza AM",
	"No disponible",
	"2248895, 3138748347",
	"sandy-monik@hotmail.com",
	"Carrera 26 # 25 - 47",
	"bn_plazaAM"
)

alojamientos(
	facebook['principehotel'],
	"Hotel Principe",
	"http://principeh.com/",
	"2258111, 2258766, 3155635275",
	"info@principeh.com",
	"Carrera 24 # 26 - 46",
	"bn_principe"
)

alojamientos(
	facebook['pages/Hotel-Real-Calima/182751915110513'],
	"Hotel Real Calima del Centro",
	"No disponible",
	"2242543, 2249142, 3117469296",
	"linita-agudelo@hotmail.com",
	"Carrera 20 # 27 - 13",
	"bn_calima"
)

alojamientos(
	twitter['Ecodataset/status/702171106770345985'],
	"Hotel Real Lina Maria del Centro",
	"No disponible",
	"2256406, 3113631094",
	"linita-agudelo@hotmail.com",
	"Calle 27 # 20 - 39",
	"bn_linamaria"
)

alojamientos(
	twitter['Ecodataset/status/702171354318184449'],
	"Hotel Real San Diego",
	"No disponible",
	"2242220, 3122138349",
	"valensan_15@hotmail.com",
	"Calle 26 # 21 - 59",
	"bn_diego"
)

alojamientos(
	facebook['pages/Hotel-San-Gil/136459539876626?fref=ts'],
	"Hotel San Gil A.S.G",
	"http://www.hotelsangiltulua.com/",
	"2246542, 3164732789",
	"astridserna@hotmail.com",
	"Calle 26 # 23 - 78",
	"bn_sangil"
)

alojamientos(
	twitter['/Ecodataset/status/703082931703697408'],
	"Finca Villa Genia",
	"No disponible",
	"2240659, 3136399699, 3187276652",
	"mivalledecompras.com@gmail.com",
	"A 15 minutos de Tulua via Campoalegre - Andalucia",
	"bn_villagenia"
)

alojamientos(
	twitter['/Ecodataset/status/703084961021235200'],
	"Finca Villa Andrea",
	"No disponible",
	"3157400134",
	"No disponible",
	"Transversal 12 Callejon el mandarino Casa 49",
	"bn_villaAndrea"
)

alojamientos(
	twitter['/Ecodataset/status/703087399254020096'],
	"Hacienda Campoalegre (Hacienda tipcia vallecaucana)",
	"No disponible",
	"2242449, 2315857",
	"No disponible",
	"Entrada Corregimiento Campoalegre Callejon Ingenio San Carlos contiguo carrilera",
	"bn_campoalegre"
)
print(ga.serialize(format='pretty-xml'))