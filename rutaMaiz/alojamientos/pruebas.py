from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from ontologias import ACCO, ORG, GR, S
import blank_nodes

homepage_cafeplaza = URIRef('http://hotelcafeplaza.com/')
facebook = Namespace('https://www.facebook.com/')
gm = Graph()

gm.add( (facebook['hotelcafeplaza'], GR.name, Literal("Hotel Cafe Plaza - C.C. Del Parque")) )
gm.add( (facebook['hotelcafeplaza'], S.telephone, Literal("2246486, 2246488, 3113546020")) )
gm.add( (facebook['hotelcafeplaza'], S.streetAddress, Literal("Calle 27 # 26-60 ofi 401")) )
gm.add( (facebook['hotelcafeplaza'], S.email, Literal("centrocomercialdelparque@hotmail.com")) )
gm.add( (facebook['hotelcafeplaza'], S.sameAs, homepage_cafeplaza))
gm.add( (facebook['hotelcafeplaza'], ACCO.feature, ACCO.AccommodationFeature) )
gm.add( (facebook['hotelcafeplaza'], RDF.type, ACCO.Hotel) )
gm.add( (ACCO.AccommodationFeature, ACCO.availabilityTimes, Literal("24 Horas")) )
gm.add( (facebook['hotelcafeplaza'], ACCO.includedFeature, blank_nodes.NB_parqueadero) )
gm.add( (blank_nodes.NB_parqueadero, RDF.type, ACCO.AccommodationFeature) )
gm.add( (blank_nodes.NB_parqueadero, GR.name, Literal("Parqueadero")) )
gm.add( (blank_nodes.NB_parqueadero, ACCO.value, Literal("Disponible")) )
gm.add( (facebook['hotelcafeplaza'], ACCO.optionalFeature, blank_nodes.NB_salon_eventos) )
gm.add( (blank_nodes.NB_salon_eventos, RDF.type, ACCO.AccommodationFeature) )
gm.add( (blank_nodes.NB_salon_eventos, GR.name, Literal("Salon de eventos")) )
gm.add( (blank_nodes.NB_salon_eventos, ACCO.value, Literal("Disponible")) )

print (gm.serialize(format="pretty-xml"))