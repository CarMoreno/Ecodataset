#Ontologias definidas para modelar el ambuto del ecoturismo y geografia
from rdflib import Namespace

#Turismo
CRUZAR = Namespace('http://idi.fundacionctic.org/cruzar/turismo#')
ACCO = Namespace('http://purl.org/acco/ns#') #Alojamientos
FOOD = Namespace('http://purl.org/ontology/fo/Collection#')
WILDLIFE = Namespace('http://purl.org/ontology/wo/')

#Geografia
GEONAMES = Namespace('http://www.geonames.org/ontology#')
GEOPOS = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
GEOES = Namespace('http://geo.linkeddata.es/ontology/') #

#Otros
GR = Namespace('http://purl.org/goodrelations/v1#')#ontologia del e-comerce
VCARD = Namespace('http://www.w3.org/2006/vcard/ns#')
EVENT = Namespace('http://linkedevents.org/ontology/')
UMBEL = Namespace('http://umbel.org/umbel#')