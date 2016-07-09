#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from ontologias import GR, VCARD, UMBEL
from alojamientos import gRutaMaiz, rutaMaiz

#Namespace necesarios
facebook = Namespace('https://www.facebook.com/')
twitter = Namespace('https://www.twitter.com/')
dbr = Namespace('http://dbpedia.org/resource/')
maps = Namespace('https://goo.gl/maps/')
camaraTulua = Namespace('http://camaratulua.org/afiliados/')
ciudadGuru = Namespace('http://www.ciudadguru.com.co/empresas/')

# Esquema del grafo para empresas de la ruta del maíz.
def empresas(uri, nombre, tel, imagen, descripcion, direcc, email, webpage, mapa, uriatencion, abre, cierra):
    if webpage == "No disponible":
        gRutaMaiz.add( (URIRef(uri), FOAF.homepage, Literal('No disponible')) )
    else:
        gRutaMaiz.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)) )
    
    gRutaMaiz.add( (URIRef(uri), FOAF.image, URIRef(imagen)) )      
    gRutaMaiz.add( (URIRef(uri), RDF.type, GR.Location) )
    gRutaMaiz.add( (URIRef(uri), GR.name, Literal(nombre)) )
    gRutaMaiz.add( (URIRef(uri), GR.description, Literal(descripcion)))
    gRutaMaiz.add( (URIRef(uri), VCARD.tel, Literal(tel)) )
    gRutaMaiz.add( (URIRef(uri), VCARD.email, Literal(email)) ) 
    
    gRutaMaiz.add( (URIRef(uri), VCARD.adr, URIRef(mapa)) )
    gRutaMaiz.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    gRutaMaiz.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia')) )
    gRutaMaiz.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá')) )
    gRutaMaiz.add( (URIRef(mapa), VCARD['street-address'], Literal(direcc)) )

    gRutaMaiz.add( (URIRef(uri), GR.hasOpeningHoursSpecification, URIRef(uriatencion)))
    gRutaMaiz.add( (URIRef(uriatencion), RDF.type, GR.OpeningHoursSpecification) )
    gRutaMaiz.add( (URIRef(uriatencion), GR.opens, Literal(abre, datatype=XSD.time)) )#Se especifica el tipo de dato
    gRutaMaiz.add( (URIRef(uriatencion), GR.closes, Literal(cierra, datatype=XSD.time)) )
    gRutaMaiz.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Monday) )
    gRutaMaiz.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Tuesday) )
    gRutaMaiz.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Wednesday) )
    gRutaMaiz.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Thursday) )
    gRutaMaiz.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Friday) )
    
    gRutaMaiz.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaMaiz.Empresas)))

empresas(
    facebook['AGROCORVALLE'],
    'Agroindustria Oleaginosa Corazón del Valle',
    '314 854 1375, 316 274 2948, 317 624 7417',
    'http://i.imgur.com/iVHRK2g.jpg',
    """Dedicada al cultivo y transformación de 
    frutos de plantas oleaginosas principalmente la SACHA INCHI
    con cadenas productivas 100% orgánicas.""",
    'Corregimiento Campoalegre',
    'sicorazondelvalle@gmail.com',
    'https://www.agrocorvalle.com',
    maps['5bcFmGU8gpx'],
    "http://www.eltabloide.com.co/el-aceite-de-los-incas/",
    "08:00:00",
    "18:00:00"
)

empresas(
    facebook['pages/Ingenio-Sancarlos-SA/624707384217059'],
    'Ingenio San Carlos',
    '57 (2) 2311515',
    'http://i.imgur.com/IwXka7i.png',
    """Empresa agroindustrial dedicada al cultivo de caña
    y su transformación en azúcares, mieles, energía limpia y otros derivados.""",
    'Vía Riofrio Km. 7 Palomestizo',
    'https://mail1.ingeniosancarlos.com.co/owa/',
    'http://www.ingeniosancarlos.com.co/',
    maps['z12DarMykcr'],
    camaraTulua['ingenio-sancarlos-s-a/'],
    "05:00:00",
    "16:00:00" 
)

empresas(
    facebook['ViveroElRosaltulua'],
    'Vivero El Rosal',
    '225 71 51, 231 34 40, 231 97 19, 316 554 2035',
    'http://i.imgur.com/OicbmG7.jpg',
    'Empresa dedicada a la producción, comercialización y distribución de plantas ornamentales.',
    'Calle 27 No. 3 Oeste 52 Vía Tuluá - Riofrio',
    'No disponible',
    'http://www.viveroelrosal.com/',
    maps['ZWqu9cCVnqy'],
    ciudadGuru['vivero-el-rosal/tulua/15406229'],
    "07:00:00",
    "18:00:00"
)

empresas(
    facebook['pages/La-Herradura/10401777341'],
    'Centro Comercial La Herradura',
    '2249507',
    'http://i.imgur.com/yXlawlm.png',
    """Centro comercial del Corazón de Valle del Cauca donde encuentras plazoleta de comidas,
    bares, tiendas, cine, eventos y más.""",
    'Carrera 19 No. 28 - 76',
    'No disponible',
    'http://www.laherradura.com.co/',
    maps['eWUvQ3seeqs'],
    ciudadGuru['centro-comercial-la-herradura/tulua/15722833'],
    "09:00:00",
    "23:00:00"
)

empresas(
    facebook['centrocomercialtuluala14'],
    'Centro Comercial Tuluá La 14',
    '2308640',
    'http://i.imgur.com/d6zxnQe.jpg',
    """Centro empresarial, comercial y de negocios, epicentro de una permanente actividad social
    y el lugar de encuentro favorito de las familias centro vallecaucanas.""",
    'Carrera. 40 No. 37-51',
    'No disponible',
    'http://centrocomercialtulua.com/',
    maps['khz8XnXuAHQ2'],
    ciudadGuru['centro-comercial-tulua-la-14/tulua/16750145'],
    "09:30:00",
    "23:30:00"
)

empresas(
    facebook['pages/Projugos-Tulua/403454439767813'],
    'Productora de Jugos S.A.S',
    '235 6100, 225 3153',
    'http://i.imgur.com/68cCsff.jpg',
    """Empresa especializada en el procesamiento de pulpas, jugos de frutas naturales
    y concentrados.""",
    'Calle 48 No. 21 - 100',
    'info@projugos.com',
    'http://www.projugos.com/',
    maps['Lb5DsP437dP2'],
    camaraTulua['productora-de-jugos-s-a-s/'],
    "07:00:00",
    "18:00:00"
)

empresas(
    facebook['pages/Levapan-Tulua/481467405286461'],
    'Levapan S.A',
    '2241688',
    'http://i.imgur.com/x9N7Moc.jpg',
    """Moderna y tecnificada planta de producción de levadura.""",
    'Carrera 27 A No. 40-470',
    'impuesto@levapan.com',
    'http://www.levapan.com/',
    maps['f3S8nRTWMdC2'],
    camaraTulua['compania-nacional-de-levaduras-levapan-s-a/'],
    "07:30:00",
    "18:00:00"
)

empresas(
    facebook['Agregar-centro-aguas-tulua/446894565390492'],
    'Centroaguas S.A . E.S.P',
    '2317070',
    'http://i.imgur.com/Dqh8Z8Y.jpg',
    """Purificación y distribución de agua, para uso doméstico y comercial.""",
    'Calle 25 No. 32A - 31',
    'info@centroaguas.com',
    'http://www.centroaguas.com/',
    maps['maps/xhhhcTiNAK12'],
    camaraTulua['centroaguas-s-a-e-s-p/'],
    "07:00:00",
    "16:00:00"
)

empresas(
    facebook['pages/Compa%C3%B1ia-de-Electricidad-de-Tulua-CETSA/109217362434941'],
    'Compañía de Electricidad de Tuluá S.A. E.S.P.',
    '2339000',
    'http://i.imgur.com/4KSaIUz.jpg',
    """Comercialización de energía eléctrica.""",
    'Calle 29 No. 23 - 45',
    'mlasso@cetsa.com.co',
    'http://www.cetsa.com.co',
    maps['CwfJVDVaH1m'],
    camaraTulua['compania-de-electricidad-de-tulua-s-a-e-s-p/'],
    "08:00:00",
    "16:00:00"
)

empresas(
    facebook['pages/trans-tobar-tulua/127752540643366'],
    'Empresa de Transportes Tobar Limitada "Transtobar"',
    '2242199',
    'http://i.imgur.com/HbJ0Oh2.jpg',
    """Transporte metropolitano colectivo regular de pasajeros.""",
    'Carrera 18 No. 26 B - 01',
    'transtobartulua@gmail.com',
    'No disponible',
    maps['zkRFEQ2E2W72'],
    camaraTulua['empresa-de-transportes-tobar-limitada-transtobar/'],
    "05:00:00",
    "19:00:00"
)

empresas(
    facebook['pages/Terminal-de-transportes-Tulu%C3%A1/413459778666424'],
    'Central de Transportes de Tuluá S.A.',
    '2245779, 2251477',
    'http://i.imgur.com/aKdj3Oq.jpg',
    """Transporte intermunicipal.""",
    'Carrera 20 No. 26 - 32',
    'contabilidad@terminaltulua.com',
    'http://www.terminaltulua.com/',
    maps['SBfKsSqoAx52'],
    camaraTulua['central-de-transportes-de-tulua-s-a/'],
    "04:30:00",
    "20:00:00"
)

empresas(
    facebook['Industria-de-Harinas-Tulua-limitada-133301366750011/'],
    'Industria de Harinas Tuluá Limitada',
    '(57) 2245815, (57) 2251477',
    'http://i.imgur.com/bszGL3B.png',
    """Industria dedicada a la elaboración de harina de trigo fortificada
    y sus derivados como la sémola, semolatto, salvado, mogolla, harina de
    tercera y harina integral.""",
    'Carrera 28 No 32-54',
    'contabilidad@harinastulua.com',
    'http://harinastulua.com/',
    maps['3yvUxvApjC32'],
    camaraTulua['industria-de-harinas-de-tulua-ltda/'],
    "08:00:00",
    "16:00:00"
)

empresas(
    dbr['Banco_Popular_(Colombia)'],
    'Banco Popular agencia Tuluá',
    '2243997',
    'http://i.imgur.com/bszGL3B.png',
    """Sede del Banco Poupular de la ciudad de Tuluá.""",
    'Carrera 25 No. 27 - 92',
    'tulua@bancopopular.com.co',
    'http://www.bancopopular.com.co/',
    maps['eRwDwfodkFM2'],
    camaraTulua['banco-popular/'],
    "08:00:00",
    "16:00:00"
)

empresas(
    dbr['Banco_de_Bogotá'.decode('utf8')],
    'Banco de Bogotá agencia Tuluá',
    '2244222',
    'http://i.imgur.com/byJtPab.jpg',
    """Sede del Banco de Bogotá de la ciudad de Tuluá.""",
    'Carrera 26  No. 27 - 32',
    'jds612@bancodebogota.com',
    'http://www.bancodebogota.com/',
    maps['C3uT9unrXJG2'],
    camaraTulua['banco-de-bogota-agencia-tulua/'],
    "08:00:00",
    "16:00:00"
)

empresas(
    dbr['Banco_de_Occidente_Credencial'],
    'Banco de Occidente agencia Tuluá',
    '2243997',
    'http://i.imgur.com/bBw3z7f.png',
    """Sede del Banco de Occidente de la ciudad de Tuluá.""",
    'Carrera 25 No. 27 - 92',
    'tulua@bancopopular.com.co',
    'http://www.bancopopular.com.co/',
    maps['bappoWJg44y'],
    camaraTulua['banco-de-occidente-agencia-tulua/'],
    "08:00:00",
    "16:00:00"
)

empresas(
    dbr['Bancolombia'],
    'Bancolombia Tulua',
    '2319905',
    'http://i.imgur.com/TOTbhR5.jpg',
    """Sede de Bancolombia de la ciudad de Tuluá.""",
    'Carrera 26 No. 26 - 20',
    'No disponible',
    'http://www.grupobancolombia.com/',
    maps['maB4rWdiNLU2'],
    camaraTulua['bancolombia-tulua/'],
    "08:00:00",
    "16:30:00"
)

empresas(
    twitter['Ecodataset/status/707056997326311424'],
    'Artesanías y Vivero El Jazmín',
    '2321193',
    'http://i.imgur.com/9OiB5aZ.png',
    """Comercialización de plantas y artesanías.""",
    'Calle 31 Nro. 38-45',
    'viverojazmin@gmail.com',
    'http://www.viveroeljazmin.com/',
    maps['iSaQ88pygck'],
    ciudadGuru['artesanias-y-vivero-el-jazmin/tulua/15724710'],
    "07:00:00",
    "18:00:00"
)

empresas(
    twitter['Ecodataset/status/707060058031595520'],
    'Bioverti',
    '3133000914',
    'http://i.imgur.com/IMbLvj6.jpg',
    """Cultivo de hortalizas, raíces y tubérculos.""",
    'Calle 26 No. 36-32 Apto 201',
    'anyel176@hotmail.com',
    'www.bioverti.com',
    maps['aE9d6FjHjUD2'],
    camaraTulua['bioverti/'],
    "09:00:00",
    "16:00:00" 
)

#print (gRutaMaiz.serialize(format="pretty-xml"))