#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rdflib import Namespace, URIRef, Literal, Graph, BNode
from rdflib.namespace import RDF, RDFS, FOAF
from ontologias import GR, VCARD, WILDLIFE

gf = Graph()
#Namespace necesarios
dbr = Namespace('http://dbpedia.org/resource/')

def fauna(uri, nombre_comun, nombre_cientifico, descripcion, imagen):
	gf.add( (URIRef(uri), WILDLIFE.commonName, Literal(nombre_comun) ) )
	gf.add( (URIRef(uri), WILDLIFE.scientificName, Literal(nombre_cientifico)))
	gf.add( (URIRef(uri), RDF.type, WILDLIFE.TaxonName) )
	gf.add( (URIRef(uri), WILDLIFE.shortDescription, Literal(descripcion)) )
	gf.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))

fauna(
	dbr['Grey-headed_dove'],
	"Paloma montaraz cabecigrís",
	"Leptotila plumbeiceps",
	"""La paloma montaraz cabecigrís Tienen un tamaño de 25 cm de largo y pesa 155g. el adulto tiene
	una corona gris. El dorso y las alas son de color marrón oliva, y las partes inferiores son de color
	sombreado en blanco en el vientre. La cola es amplia con punta de color blanco. Las aves jóvenes
	carecen de color gris en la cabeza.""",
	"http://i.imgur.com/0ViaN29.jpg"
)

fauna(
	dbr['http://dbpedia.org/page/Ruby-topaz_hummingbird'],
	"Tucusito rubí",
	"Chrysolampis mosquitus",
	"""Es un colibrí pequeño. De pico corto. Sus colores van desde el negro en su mayor parte, 
	con un distintivo color rojo en la parte de la coronilla. También posee tonalidades naranja
	y café oliva oscuro. Se lo halla en la Cordillera Occidental y otros lugares con tierras áridas.""",
	"http://i.imgur.com/ZefaXVe.jpg"
)

fauna(
	dbr['Greyish_piculet'],
	"Carpintero punteado",
	"Picumnus granadensis",
	"""""",
	"http://i.imgur.com/WiMJbSs.jpg"
)

fauna(
	dbr['Bar-crested_antshrike'],
	"Batará crestibarrado",
	"Thamnophilus multistriatus",
	"""Esta especie es Endémica de Colombia y presenta una distribución restringida a valles
	interandinos. Su distribución comprende desde Panamá hasta las Guayanas y Bolivia, de longitud
	logra unos 20 cm. """,
	"http://i.imgur.com/ZTiTTvy.jpg"
)

fauna(
	dbr['Flame-rumped_tanager'],
	"Sangretoro lomo de fuego",
	"Ramphocelus flammigerus",
	"""es una especie de ave de la familia Thraupidae, que se encuentra en bosques y zonas arboladas
	en Panamá, el occidente y centro de Colombia y noroccidente de Ecuador. Mide en promedio 19 cm
	de longitud.""",
	"http://i.imgur.com/udtsGTS.jpg"
)

fauna(
	dbr['Large-billed_seed_finch'],
	"Semillero piquigrande",
	"Oryzoborus crassirostris",
	"""""",
	"http://i.imgur.com/maOVQKf.jpg"
)

fauna(
	dbr['Cinnamon_teal'],
	"Pato colorado",
	"Anas cyanoptera",
	"""Su nombre viene del latín Anas que significa pato y del griego kuanopterus que significa de alas azules.  Las subespecies
	residentes de Colombia se encuentran en peligro, debido principalmente a la desecación de humedales.""",
	"http://i.imgur.com/w8vAGpk.jpg"
)

fauna(
	dbr['Great_egret'],
	"Garza blanca",
	"Ardea alba",
	"""Ésta es una de las garzas grandes. De longitud mide entre 88 y 104 cm, el peso es de unos 900 gramos,
	alcanzando algunas el kilogramo. En promedio, los machos son ligeramente más grandes que las hembras.""",
	"http://i.imgur.com/XcvcXho.jpg"
)

fauna(
	dbr['Yellow-headed_gecko'],
	"Geco cabeza amarilla",
	"Gonatodes albogularis",
	"""Los adultos tienen una longitud total de sólo 6 cm. Es activo durante el día. Los machos son muy visibles,
	con la cabeza amarilla y el cuerpo de color azul oscuro a negro. A temperaturas más frías durante la noche,
	sus colores se desvanecen, a una coloración gris o azul-verdosa (machos). Las hembras son lagartos moteados grises,
	 a menudo con una línea clara en el cuello. """,
	"http://i.imgur.com/puGypO1.jpg"
)

fauna(
	dbr['Anolis_fuscoauratus'],
	"Camaleón sabanero",
	"Anolis auratus",
	"""""",
	"http://i.imgur.com/GmRbMrK.jpg"
)

fauna(
	dbr['Rainbow_whiptail'],
	"Cotejos o lagartijas azules",
	"Cnemidophorus lemniscatus",
	"""Se encuentra en los paises de Colombia, Venezuela, Ecuador, Panamá, Guyana y Brasil. Pertenece
	a la familia Dactyloidae""",
	"http://i.imgur.com/SwAA6fV.jpg"
)

fauna(
	dbr['White-lipped_mud_turtle'],
	"Tortuga del fango de boca blanca",
	"Kinosternon leucostomum",
	"""Tienen el caparazón de color marrón oscuro. No tienen ni dibujos ni casi
	se les marcan los escudos de crecimiento. El plastrón es amarillo o amarillo con manchas oscuras.
	La cabeza es oscura, con la mandíbula de color amarillo claro y una mancha amarilla en ambos
	lados de la cabeza.""",
	"http://i.imgur.com/dTOXhTA.jpg"
)

fauna(
	dbr['Colostethus_fraterdanieli'],
	"Rana silbadora",
	"Colostethus fraterdanieli",
	"""Especie de rana de la famila Dendrobatidae, es endémica en los Andes de Colombia (Coordillera central
	y Occidental). Vive en el suelo cerca de los arroyos en los bosques de niebla y en los bosques tropicales secos""",
	"http://i.imgur.com/f9GcVuo.jpg"
)

fauna(
	dbr['Typhlonectes_natans'],
	"Culebra ciega",
	"Typhlonectes natans",
	"""Es un reptil escamoso adaptado a la vida en el subsuelo, a la vista son parecidos a las lombrices de
	tierra. El cuerpo es de forma cilíndrica, es anillado y no tiene patas. La cabeza tiene forma 
	trapezoidal y está separada del cuerpo por un surco. Pasan por una sola muda de piel.""",
	"http://i.imgur.com/kquFtEi.jpg"
)

fauna(
	dbr['Leptodactylus_colombiensis'],
	"Rana criolla",
	"Leptodactylus colombiensis",
	"""Amplia distribución en la región Andina y cuenca del Orinoco en los departamentos de Amazonas,
	Casanare, Antioquia, Boyacá, Valle del Cauca, entre otros. Los machos presentan dos espinas medianas en cada pulgar y hendiduras bucales bien desarrolladas. La superficie dorsal es lisa y de color marrón a oliva,
	mientras el vientre presenta un patrón moteado y puntos claros en la región gular.""",
	"http://i.imgur.com/AHG1ELR.jpg"
)

fauna(
	'https://www.wikidata.org/wiki/Q5546624',
	"Besudo",
	"Ichthyoelephas longirostris",
	"""Muy similar al bocachico, pero se distingue por su boca más prominente, con el labio superior mucho más  grueso, los ojos relativamente pequeños
	y por la ausencia de la espina predorsal, característica de  los bocachicos.""",
	"http://i.imgur.com/lagzgEh.jpg"
)

fauna(
	dbr['Prochilodus_magdalenae'],
	"Bocachico",
	"Prochilodus magdalenae",
	"""El bocachico es un pez migratorio de agua dulce, su tamaño es mediano, los ejemplares más grandes pueden alcanzar los 60 cms de longitud,
	su boca es pequeña, carnosa y prominente lo cual da origen a su nombre común.""",
	"http://i.imgur.com/HnMP0Yw.jpg"
)

fauna(
	dbr['Red_junglefowl'],
	"Pollo de engorde",
	"Gallus gallus",
	"""""",
	"http://i.imgur.com/4GG3jmG.jpg"
)

fauna(
	dbr.Chicken,
	"Gallinas ponedoras",
	"Gallus domesticus",
	"""Las gallinas denominadas ponedoras provienen de cruces a tres vías de razas puras (Leghor, Rhode Island, New Hampshire, Ply Mouth rock, Wyandontte y Sussex Armiñada)
	y más recientemente con razas sintéticas recesivas para obtener pollitos autoxesados. """,
	"http://i.imgur.com/XYrd1QJ.jpg"
)

fauna(
	dbr['Banded_pig'],
	"Cerdo",
	"Sus scrofa",
	"""Se trata de un cuadrúpedo con patas cortas y pezuñas, un cuerpo pesado, hocico flexible y cola corta.
	 Cabe señalar que el término cerdo proviene de cerda, lo que hace referencia a su pelo grueso.""",
	"http://i.imgur.com/tAAqVR5.jpg"
)

fauna(
	dbr['Taurine_cattle'],
	"Vacas",
	"Bos taurus",
	"""Las vacas pesan más de media tonelada y pueden medir hasta un metro y medio de altura.
	Se cree que su domesticación comenzó en Medio Oriente hace cerca de 10.000 años.
	La cría y el uso de la vaca forman parte de la ganadería bovina.""",
	"http://i.imgur.com/jisqkqN.jpg"
)

fauna(
	dbr.Goat,
	"Cabra",
	"Capra aegagrus hircus",
	"""La cabra doméstica proviene de la forma salvaje Capra aegragus cretica, originaria de la cuenca mediterránea.
	Las cabras son poco exigentes en su alimentación, pueden comer cualquier materia vegetal: hierba, hojas, brotes. 
	Se pueden levantar sobre las patas traseras para llegar a las hojas o frutos de los árboles. """,
	"http://i.imgur.com/r3z36ib.jpg"
)

fauna(
	dbr['Cane_toad'],
	"Sapo neotropical",
	"Rhinella marina",
	"""También conocido como Sapo de caña, es un animal que destaca por su grandeza física
	y por ser uno de los más antiguos que se hayan descubierto.  Mide usualmente de 10 a 15 centímetros,
	pero se han encontrado algunos ejemplares más grandes.""",
	"http://i.imgur.com/p9v212l.jpg"
)

fauna(
	dbr['Dendropsophus_columbianus'],
	"Rana común",
	"Dendropsophus columbianus",
	"""la longitud rostro-cloacal del macho varía entre los 25,8 – 29,3 mm y en las hembras varía entre
	los 30,6 – 35,4 mm; hocico corto y redondeado; tímpano visible; piel del dorso de textura granular
	fina y vientre granular; ojos grandes con pupila negra e iris de color bronce a cobre rojizo.""",
	"http://i.imgur.com/p9v212l.jpg"

)

fauna(
	dbr['Leptodactylus_fragilis'],
	"Rana de bigotes",
	"Leptodactylus fragilis",
	"""Leptodactylus fragilis es una especie de anfibio anuro de la familia Leptodactylidae.
	Es nativo del sur de Norteamérica, América Central y el norte de América del Sur.""",
	"http://i.imgur.com/MlgLngs.jpg"
)

fauna(
	dbr['American_bullfrog'],
	"Rana toro",
	"Lithobates catesbeianus",
	"""Es un anfibio de gran tamaño de entre 10 y 20 cm de longitud hocico-cloaca y un peso entre 60 y 900 gr. 
	Sus larvas son excepcionalmente grandes, pudiendo medir entre 15 y 18 cm. Su cabeza es ancha y plana y
	presenta un pliegue de piel a cada lado que corre desde detrás del ojo hasta el tímpano, bordeándolo.""",
	"http://i.imgur.com/inUup4b.jpg"
)

fauna(
	dbr['South_American_snapping_turtle'],
	"Tortuga mordedora",
	"Chelydra acutirostris",
	"""Pesa de 4,5 a 16 kg. Su caparazón  mide de 20 a 47cm. y una cola tan larga como el caparazón. La cola tiene escamas en forma de sierra.
	La piel es gris bronce con algunas manchas amarillas o blancas. """,
	"http://i.imgur.com/JCOlQxj.jpg"
)

fauna(
	dbr['White-lipped_mud_turtle'],
	"Morrocoy",
	"Chelonoidis carbonaria",
	"""La tortuga Morrocoy es terrestre y vive durante muchos años, puede alcanzar una longitud de hasta 51 cm y su caparazón es alto con forma de cúpula,
	éste tiene el fondo de color negro y centros de las escamas amarillo-naranjas o naranja-rojizos.""",
	"http://i.imgur.com/u9TOI9Z.jpg"
)

fauna(
	dbr['Black_vulture'],
	"Gallinazo",
	"Coragyps atratus",
	"""Miden aproxiamdamente entre 56 y 66 cm, tiene un peso en la hembra de 1940 g y en el macho un peso de 1180 g. Es un ave compacta de cola corta cuadrada
	y de alas anchas. """,
	"http://i.imgur.com/zU1wL0J.jpg"
)
print (gf.serialize(format="pretty-xml")) 

