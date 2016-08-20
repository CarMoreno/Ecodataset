#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from ontologias import GR, VCARD, ACCO, UMBEL
from RutaMaiz import g, rutaMaiz #de RutaMaiz importo el grafo de Inicio de la ruta

#Namespace necesarios
facebook = Namespace('https://www.facebook.com/')
twitter = Namespace('https://www.twitter.com/Ecodataset/status/')
dbr = Namespace('http://dbpedia.org/resource/')
alcaldiaTulua = Namespace('http://www.tulua.gov.co/sitio.shtml?apc=m1r1--&x=') #Habitaciones
ciudadGuru = Namespace('http://www.ciudadguru.com.co/empresas/') #Valores
hoteles = Namespace('http://hotel-az.com/viajes-turismo/tulua/')
turismoTulua = Namespace('http://rnttulua.confecamaras.co/detalle-establecimiento/') #Camas - Registro Nacional de Turismo
imgur = Namespace('http://i.imgur.com/')
maps = Namespace('https://goo.gl/maps/')


def alojamientos(uri, nombre, webpage, telefono, email, direcc, mapa, descripcion, uriRoom, uriValue, 
	uriBed, numHabitaciones, numCamas, imagen):
	if webpage == "No disponible":
		g.add( (URIRef(uri), FOAF.homepage, Literal(webpage)))
	else:
		g.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)))	
			
	g.add( (URIRef(uri), RDF.type, ACCO.Hotel))
	g.add( (URIRef(uri), RDF.type, GR.Individual) )
	g.add( (URIRef(uri), GR.name, Literal(nombre)) )
	g.add( (URIRef(uri), GR.description, Literal(descripcion)) )
	g.add( (URIRef(uri), VCARD.tel, Literal(telefono)))
	g.add( (URIRef(uri), VCARD.email, Literal(email)))
	g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
	g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))

	#Dirección según vCard 2006
	g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
	g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia')) )
	g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá')) )
	g.add( (URIRef(mapa), VCARD['street-address'], Literal(direcc)) )

	#Horario de Atención
	g.add( (URIRef(uri), ACCO.feature, ACCO.AccommodationFeature) )
	g.add( (ACCO.AccommodationFeature, ACCO.availabilityTimes, Literal("24 Horas")) )

	#Habitaciones
	g.add( (URIRef(uriRoom), RDF.type, ACCO.HotelRoom))
	g.add( (URIRef(uriRoom), RDF.type, GR.SomeItems) )
	g.add( (URIRef(uriRoom), ACCO.partOf, URIRef(uri)) )

	#Value
	g.add( (URIRef(uriValue), RDF.type, GR.QuantitativeValue))
	g.add( (URIRef(uriRoom), ACCO.numberOfRooms, URIRef(uriValue)) )
	g.add( (URIRef(uriValue), GR.hasUnitOfMeasurement, Literal("C62"))) #No hay unidades
	g.add( (URIRef(uriValue), GR.hasValue, Literal(numHabitaciones, datatype=XSD.int)))

	#Camas
	g.add( (URIRef(uriBed), RDF.type, ACCO.BedDetails))
	g.add( (URIRef(uriRoom), ACCO.bed, URIRef(uriBed)))
	g.add( (URIRef(uriBed), ACCO.quantity, Literal(numCamas, datatype=XSD.int)))

	#g.add( (URIRef(uri), VCARD.cateogry, Literal("Alojamientos de la Ruta del Maíz")))
	g.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaMaiz.Alojamientos)))

alojamientos(
	facebook["hotel.trivino"],
	"Apartahotel Triviño",
	"No disponible",
	"2289631, 3164331055",
	"gerardotrivinooviedo@hotmail.com",
	"Calle 26 # 40 - 120",
	maps['1t6aDroU82p'],
	"""Hotel con calidad humana y que se preocupa por el planeta, hoy está aportando un granito de arena 
	con su calentador de agua SOLAR. Número de empleados 2.""",
	alcaldiaTulua['1519548'],
	ciudadGuru['apartahotel-trivino/tulua/16788014'],
	turismoTulua['44554/apartahotel-trivino'],
	"12",
	"30",
	imgur
)

alojamientos(
	facebook['Apartahotel-Marques-de-la-Villa-M-337867679645873/'],
	"El Marqués De La Villa",
	"No disponible",
	"2245667, 3165244701",
	"No disponible",
	"Carrera 22 # 24 - 51",
	maps['TrexnwjpRJ12'],
	"""Usted encontrará un ambiente único ya sea que busque alojamiento o bien un rato de placer. Todo con la más 
	absoluta reserva; cuenta con 4 empleados, WIFI.""",
	alcaldiaTulua['1519545'],
	ciudadGuru['hotel-marques-de-la-villa/tulua/15720776'],
	turismoTulua['8629/hotel-el-marques-de-la-villa'],
	"38",
	"55",
	imgur
)

alojamientos(
	facebook['hotelcafeplaza'],
	"Hotel Café Plaza - C.C. Del Parque",
	"http://hotelcafeplaza.com/",
	"2246486, 2246488, 3113546020",
	"centrocomercialdelparque@hotmail.com",
	"Calle 27 # 26-60 ofi 401",
	maps['cEpDv4PSfuq'],
	"""Está en el corazón de la ciudad con una ubicación estratégica para el descanso y los negocios, 
	tienen la capacidad de organizar eventos y congresos. Cuenta con 13 empleados, WIFI, baño turco, 
	piscina, restaurante, jacuzzi, minibar, GYM, parqueadero, lavandería.""",
	alcaldiaTulua['1519554'],
	"https://marketingimpulsatunegocio.files.wordpress.com/2014/10/hotel-cafe-plaza.png",
	turismoTulua['44562/hotel-cafe-plaza-centro-comercial-del-parque'],
	"49",
	"59",
	imgur
)

alojamientos(
	facebook['Hotel-Central-Jhoanna-334144413428928'],
	"Hotel Central Johanna",
	"No disponible",
	"2243246, 2248383, 3156304788",
	"centrocomerciallascolmenas@hotmail.com",
	"Carrera 22 # 24 - 10",
	maps['Js6tmUGKTM72'],
	"""Número de empleados 5, WIFI.""",
	alcaldiaTulua['1519558'],
	ciudadGuru['hotel-central-johanna/tulua/15728378'],
	turismoTulua['34765/hotel-central-johanna'],
	"30",
	"35",
	imgur
)

alojamientos(
	twitter['702167641562214402'],
	"Hotel Cielo",
	"No disponible",
	"3006200436",
	"aruru85@hotmail.com",
	"Carrera 20 # 25 - 31",
	maps['DQD9V7bKVHv'],
	"""Número de empleados 1.""",
	alcaldiaTulua['1519562'],
	ciudadGuru['hotel-cielo/tulua/30257121'],
	turismoTulua['14236/hotel-cielo'],
	"15",
	"25",
	imgur
)

alojamientos(
	facebook['hotelcorazondelvalle'],
	"Hotel Corazón del Valle",
	"http://www.hotelcorazondelvalle.com/",
	"2323208, 2256604, 3164484351, 3117998237",
	"info@hotelcorazondelvalle.com",
	"Calle 24 # 23 - 10 PISO 2",
	maps['ubUAXQ61Fm22'],
	"""Número de empleados 3, piscina, cafetería, aire acondicionado, WIFI, parqueadero.""",
	turismoTulua['13984/hotel-corazon-del-valle'],
	ciudadGuru['hotel-corazon-del-valle/tulua/15728364'],
	hoteles['hotel-corazon-del-valle/'],
	"27",
	"29",
	imgur
)

alojamientos(
	facebook['profile.php?id=100009492184574&ref=br_rs'],
	"Hotel Don Felipe",
	"No disponible",
	"2339685, 3174074195",
	"hoteldonfelipe@hotmail.com",
	"Carrera 24 # 28 - 51",
	maps['stex8Ctdpqn'],
	"""Número de empleados 1, WIFI, parqueadero de motos.""",
	alcaldiaTulua['1519552'],
	ciudadGuru['hotel-don-felipe/tulua/15714864'],
	turismoTulua['3156/hotel-don-felipe'],
	"19",
	"23",
	imgur
)

alojamientos(
	twitter['702168136506855427'],
	"Hotel Don Jorge La 23",
	"No disponible",
	"2259022, 3104949597",
	"james.camelo@hotmail.com",
	"Carrera 23 # 26 - 41",
	maps['4abPEwStUGo'],
	"""Número de empleados 2, WIFI.""",
	alcaldiaTulua['1519553'],
	ciudadGuru['hotel-real-don-jorge/tulua/15722685'],
	turismoTulua['44567/hotel-don-jorge-de-la-23'],
	"10",
	"10",
	imgur
)

alojamientos(
	facebook['people/Hotel-Don-Sebastian/100007234909156'],
	"Hotel Don Sebastián",
	"No disponible",
	"2250273, 3207255497",
	"hoteldonsebastian@outlook.es",
	"Carrera 20 # 25 - 83",
	maps['umsKS6jfegF2'],
	""""Número de empleados 2, WIFI. """,
	alcaldiaTulua['1519551'],
	ciudadGuru['hotel-don-sebastian/tulua/15714858'],
	turismoTulua['3384/hotel-don-sebastian'],
	"14",
	"19",
	imgur
)

alojamientos(
	facebook['pages/HOTEL-EL-DESCANSO-DEL-VISITANTE/229134903821536'],
	"Hotel El Descanso Del Visitante",
	"No disponible",
	"2244518, 3184395202, 2249604",
	"fabeca_23@hotmail.com",
	"Carrera 20 # 25 - 71",
	maps['UDBYyZndMkG2'],
	"""Número de empleados 2, WIFI.""",
	alcaldiaTulua['1519563'],
	ciudadGuru['hotel-el-descanso-del-visitante/tulua/16252288'],
	hoteles['hotel-el-descanso-del-visitante/'],
	"10",
	"12",
	imgur
)

alojamientos(
	facebook['pages/Jardin-del-Ed%C3%A9n/515577135188478'],
	"Hotel El Jardín Del Edén De La 26",
	"No disponible",
	"2254777, 3154889594",
	"eledenhosteria@hotmail.com",
	"Calle 26 # 26 - 39",
	maps['M7J3dFxZA6x'],
	"""Número de empleados 2.""",
	alcaldiaTulua['1475486'],
	ciudadGuru['hotel-el-jardin-del-eden-de-la-26/tulua/30248090'],
	turismoTulua['994/hotel-el-jardin-del-eden-de-la-26'],
	"13",
	"15",
	imgur
)

alojamientos(
	facebook['pages/Hotel-El-Para%C3%ADso-Ideal/155040651352392'],
	"Hotel El Paraíso Ideal",
	"No disponible",
	"2248111, 3177424939",
	"hotelparaiso13@gmail.com",
	"Carrera 22 # 25 - 90",
	maps['GPnRmH5o2QA2'],
	"""Número de empleados 2.""",
	alcaldiaTulua['1475496'],
	hoteles['hotel-el-paraiso-ideal/'],
	turismoTulua['8251/hotel-el-paraiso-ideal'],
	"20",
	"27",
	imgur
)

alojamientos(
	facebook['maricel.pupiales/about'],
	"Hotel Escalinata Pupi",
	"No disponible",
	"2241782, 3207561454",
	"hotelescalinata@hotmail.com",
	"Carrera 27A # 34 - 30",
	maps['Mww8hkjwZ1m'],
	""""Número de empleados 2, WIFI.""",
	turismoTulua['12913/hotel-escalinata-pupi'],
	ciudadGuru['hotel-escalinata/tulua/15718640'],
	hoteles['hotel-escalinata-pupi/'],
	"15",
	"26",
	imgur
)

alojamientos(
	facebook['Hotel-Juan-Maria-1458858754370044/?fref=ts'],
	"Hotel Juan María",
	"http://hoteljuanmaria.com/",
	"2244562, 3154902380",
	"administracion@hoteljuanmaria.com",
	"Carrera 28 # 27 - 10",
	maps['3jAuXwvcpk52'],
	"""Mejor ubicación, tradición y experiencia; 37 años al servicio del sector hotelero y turístico. 
	Número de empleados 20, aire acondicionado, restaurante, piscina (club privado), WIFI, parqueadero.""",
	alcaldiaTulua['1475479'],
	ciudadGuru['hotel-juan-maria/tulua/6784774'],
	turismoTulua['2193/hotel-juan-maria-ltda'],
	"50",
	"113",
	imgur
)

alojamientos(
	twitter['702168954102530048'],
	"Hotel La Estrella De La Mañana",
	"No disponible",
	"2244639, 2240452, 3103725051",
	"leonelly.7@hotmail.com",
	"Calle 25 # 20 - 49",
	maps['u9S9qu62uTE2'],
	"""Número de empleados 3.""",
	alcaldiaTulua['1519561'],
	ciudadGuru['hotel-la-estrella-de-la-manana/tulua/30246128'] ,
	turismoTulua['4404/hotel-la-estrella'],
	"18",
	"25",
	imgur
)

alojamientos(
	facebook['pages/Hotel-La-Mancion-del-Sol/248019025357779?rf=820075471383988'],
	"Hotel La Mansión Del Sol",
	"http://www.lamansiondelsol.amawebs.com/",
	"22320809, 3113378579",
	"hotel_lamansiondelsol@hotmail.com",
	"Calle 26 # 22 - 17 PISO 2",
	maps['3RQ7a3xogmG2'],
	"""La amabilidad y atención harán de su estadía en Tuluá, su mejor experiencia. Ambiente familiar, WIFI, 
	aire acondicionado, ventilador, número de empleados 1. Descuentos especiales para grupos.""",
	turismoTulua['44588/hotel-la-mansion-del-sol-4'],
	ciudadGuru['hotel-la-mansion-del-sol/tulua/15726567'],
	hoteles['hotel-la-mansion-del-sol/'],
	"15",
	"20",
	imgur
)

alojamientos(
	twitter['702169670200201216'],
	"Hotel La Siesta",
	"No disponible",
	"2256828, 3207090919",
	"valensan_15@hotmail.com",
	"Carrera 20 # 25 - 95",
	maps['GUhkY9BWrct'],
	"""Número de empleados 3, WIFI.""",
	alcaldiaTulua['1475495'],
	ciudadGuru['hotel-la-siesta/tulua/15724653'],
	hoteles['hotel-la-siesta-de-la-20/'],
	"12",
	"12",
	imgur
)

alojamientos(
	twitter['702170175773270019'],
	"Hotel Los Corales Del Corazón Del Valle",
	"No disponible",
	"2261771, 3155753404",
	"gerencia@hotelcorales.com",
	"Carrera 21 # 25 - 59",
	maps['DxD4mvd25x12'],
	"""Número de empleados 4, WIFI, aire acondicionado.""",
	alcaldiaTulua['1475489'],
	ciudadGuru['hotel-los-corales-del-corazon-del-valle/tulua/30246268'],
	turismoTulua['4564/hotel-los-corales-del-corazon-del-valle'],
	"31",
	"42",
	imgur
)

alojamientos(
	facebook['hotelloscristales.detulua?ref=br_rs'],
	"Hotel Los Cristales",
	"http://www.loscristales-hotel.com/",
	"2258463, 2246499, 3153520902",
	"administracion@loscristales-hotel.com",
	"Calle 27 # 26 - 50",
	maps['o15uZkFJj6y'],
	"""Prestación del servicio de hospedaje a clientes nacionales e internacionales que deseen disfrutar de un 
	ambiente acogedor con comodidad, seguridad, salubridad y de un servicio con calidad. Número de empleados 3, WIFI, 
	aire acondicionado, minibar, TV por cable.""",
	alcaldiaTulua['1475490'],
	ciudadGuru['hotel-los-cristales/tulua/15384126'],
	turismoTulua['3063/hotel-los-cristales-12'],
	"19",
	"27",
	imgur
)

alojamientos(
	twitter['702170493336612864'],
	"Hotel Mariscal Sucre D.F.G",
	"No disponible",
	"2244065, 3174296588",
	"g.amta78@hotmail.com",
	"Carrera 24 # 27 - 76",
	maps['C6nSDynZr2E2'],
	"""Número de empleados 2, WIFI.""",
	alcaldiaTulua['1519549'],
	ciudadGuru['hotel-mariscal-sucre-dfg/tulua/30236628'],
	turismoTulua['3448/hotel-mariscal-sucre-dfg'],
	"18",
	"23",
	imgur
)

alojamientos(
	facebook['hotelmorfeo/timeline?ref=page_internal'],
	"Hotel Morfeo",
	"No disponible",
	"2242520, 2248383, 3156304788",
	"centrocomerciallascolmenas@hotmail.com",
	"Calle 25 # 22 - 33",
	maps['5Dmqh5co6gS2'],
	"""Número de empleados 5.""",
	alcaldiaTulua['1519559'],
	ciudadGuru['hotel-morfeo/tulua/15724942'],
	turismoTulua['34260/hotel-morfeo'],
	"40",
	"50",
	imgur
)

alojamientos(
	twitter['702170787411787782'],
	"Hotel Plaza AM",
	"No disponible",
	"2248895, 3138748347",
	"sandy-monik@hotmail.com",
	"Carrera 26 # 25 - 47",
	maps['9iibiYeufQC2'],
	"""Número de empleados 2.""",
	alcaldiaTulua['1519556'],
	ciudadGuru['hotel-plaza-am/tulua/30231147'],
	turismoTulua['39900/hotel-plaza-a-m'],
	"10",
	"10",
	imgur
)

alojamientos(
	facebook['principehotel'],
	"Hotel Principe",
	"http://principeh.com/",
	"2258111, 2258766, 3155635275",
	"info@principeh.com",
	"Carrera 24 # 26 - 46",
	maps['X7PuzjEPnHo'],
	"""Convenientemente ubicado en la zona comercial de la ciudad de Tuluá, lo que hará de la estadía una 
	experiencia inigualable, donde tulueños y visitantes se encuentran en un ambiente amable y seguro. Número de 
	empleados 13, restaurante, WIFI, parqueadero, lavandería, aire acondicionado, minibar.""",
	alcaldiaTulua['1475478'],
	ciudadGuru['hotel-principe/tulua/2735840'],
	turismoTulua['2524/hotel-principe'],
	"35",
	"56",
	imgur
)

alojamientos(
	facebook['pages/Hotel-Real-Calima/182751915110513'],
	"Hotel Real Calima del Centro",
	"No disponible",
	"2242543, 2249142, 3117469296",
	"linita-agudelo@hotmail.com",
	"Carrera 20 # 27 - 13",
	maps['HReA4aNXqBy'],
	"""Número de empleados 3, WIFI.""",
	alcaldiaTulua['1475482'],
	ciudadGuru['hotel-real-calima-del-centro/tulua/30254701'],
	turismoTulua['25514/calima-hotel'],
	"18",
	"18",
	imgur
)

alojamientos(
	twitter['702171106770345985'],
	"Hotel Real Lina María del Centro",
	"No disponible",
	"2256406, 3113631094",
	"linita-agudelo@hotmail.com",
	"Calle 27 # 20 - 39",
	maps['r922xissVJm'],
	"""Número de empleados 3, WIFI.""",
	alcaldiaTulua['1475497'],
	ciudadGuru['hotel-real-lina-maria-del-centro/tulua/30246576'],
	turismoTulua['5481/hotel-lina-maria'],
	"18",
	"18",
	imgur
)

alojamientos(
	twitter['702171354318184449'],
	"Hotel Real San Diego",
	"No disponible",
	"2242220, 3122138349",
	"valensan_15@hotmail.com",
	"Calle 26 # 21 - 59",
	maps['zKvaE1yyFiF2'],
	"""Número de empleados 2, WIFI.""",
	alcaldiaTulua['1519564'],
	ciudadGuru['hotel-real-san-diego/tulua/25090476'],
	turismoTulua['8526/hotel-real-san-diego'] ,
	"11",
	"10",
	imgur
)

alojamientos(
	facebook['pages/Hotel-San-Gil/136459539876626?fref=ts'],
	"Hotel San Gil A.S.G",
	"http://www.hotelsangiltulua.com/",
	"2246542, 3164732789",
	"astridserna@hotmail.com",
	"Calle 26 # 23 - 78",
	maps['mnvccgyH36k'],
	"""Número de empleados 4, parqueadero, WIFI, aire acondicionado, restaurante, bar.""",
	alcaldiaTulua['1519560'],
	ciudadGuru['hotel-san-gil/tulua/16501236'],
	turismoTulua['1053/hotel-san-gil-a-s-g'],
	"31",
	"42",
	imgur
)

alojamientos(
	twitter['749977352231329792'],
	"Hotel Sueño Real H.S.R",
	"No disponible",
	"3127694711",
	"alejosantatoro@yahoo.es",
	"Carrera 40 # 28 - 151",
	maps['tkxxU1hWMoB2'],
	"""Número de empleados 2.""",
	alcaldiaTulua['1519557'],
	ciudadGuru['hotel-sueno-real-hsr/tulua/30230751'],
	turismoTulua['40121/hotel-sueno-real-h-s-r'],
	"10",
	"10",
	imgur
)

alojamientos(
	facebook['hotelwespedes/'],
	"Wespedes Hotel",
	"http://wespedes.wix.com/hotelwespedes",
	"2252828, 2248465, 2259817, 3503044956",
	"hotelwespedes@hotmail.com",
	"Calle 25 No. 23 - 35",
	maps['5kzFwhAvxv92'],
	""""Ubicado estratégicamente a pocos metros de la alcadía municipal y la terminal de transporte. Número de 
	empleados 6, WIFI, parqueadero, aire acondicionado, cafetería.""",
	alcaldiaTulua['1475494'],
	ciudadGuru['hotel-wespedes/tulua/15729012'],
	turismoTulua['7597/hotel-wespedes'],
	"21",
	"33",
	imgur
)

alojamientos(
	facebook['pages/Hotel-Santa-Maria/591387947617132'],
	"Santa María Hotel",
	"No disponible",
	"2248470 ,  2254887,  3104744456",
	"gustavo.lopez19@yahoo.com",
	"Calle 25 No. 23 - 11",
	maps['2cmCsxtyYgK2'],
	""""Número de empleados  4, WIFI.""",
	alcaldiaTulua['1475491'],
	ciudadGuru['hotel-santa-maria/tulua/25204643'],
	turismoTulua['4329/santa-maria-hotel'],
	"8",
	"17",
	imgur
)

alojamientos(
	twitter['703082931703697408'],
	"Finca Villa Genia",
	"No disponible",
	"2240659, 3136399699, 3187276652",
	"mivalledecompras.com@gmail.com",
	"A 15 minutos de Tuluá vía Campoalegre - Andalucia",
	maps['WL3vdXHMcp52'],
	"""Alquiler por días para que disfrute de sus eventos familiares y empresariales.""",
	"https://www.youtube.com/watch?v=jio4GjdYjjU",
	"http://www.amarillascolombia.co/colombia/tulua-valle/alquiler-de-fincas/chalet-villa-genia-398164",
	"http://www.paginasamarillasdecolombia.com//imagenes/20eae3_290620121948.jpg",
	"4",
	"16",
	imgur
)

alojamientos(
	twitter['703084961021235200'],
	"Finca Villa Andrea",
	"No disponible",
	"3157400134",
	"No disponible",
	"Transversal 12 Callejon el mandarino Casa 49",
	maps['4oyzXJAM7xk'],
	"""Con capacidad de ocupación para 36 personas, salón para 30 pax, piscina recreativa y amplia zona verde. 
	En la cual se puede disfrutar de la naturaleza y es un espectacular contraste entre lo moderno y natural.""",
	alcaldiaTulua['1515768'],
	facebook['pages/Finca-Villa-Andrea/1613195678819015'],
	"http://www.tulua.gov.co/apc-aa-files/63373337616336646361623532613064/fotos_casa_campestre_villa_andrea1.jpg",
	"",
	"36",
	imgur
)

alojamientos(
	twitter['703087399254020096'],
	"Hacienda Campoalegre (Hacienda tipica vallecaucana)",
	"No disponible",
	"2242449, 2315857",
	"No disponible",
	"Entrada Corregimiento Campoalegre Callejón Ingenio San Carlos contiguo carrilera",
	maps['e3kSoVt9nvr'],
	"""Ofrece pasadías y hospedaje.  Zona para camping, piscina, kiosco, senderos ecológicos, cultivos de caña, 
	casa hermosamente amueblada y decorada con elementos típicos vallecaucanos.""",
	"http://tulua.gov.co/sitio.shtml?apc=B1-1--&x=1475501",
	"http://www.tulua.gov.co/apc-aa-files/63373337616336646361623532613064/Hacienda_Campoalegre.jpg",
	"http://www.tulua-valle.gov.co/sitio.shtml?apc=m-u-1481397-1481397&x=1475501",
	"7",
	"19",
	imgur
)
#print(g.serialize(format='pretty-xml'))