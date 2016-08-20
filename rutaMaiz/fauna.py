#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rdflib import Namespace, URIRef, Literal, Graph, BNode
from rdflib.namespace import RDF, RDFS, FOAF
from ontologias import GR, VCARD, WILDLIFE, UMBEL
from eventos import g, rutaMaiz


#Namespace necesarios
dbr = Namespace('http://dbpedia.org/resource/')
wiki = Namespace('https://www.wikidata.org/wiki/')

def fauna(uri, nombre_comun, nombre_cientifico, descripcion, imagen):
	g.add( (URIRef(uri), RDF.type, WILDLIFE.TaxonName) )
	g.add( (URIRef(uri), WILDLIFE.commonName, Literal(nombre_comun) ) )
	g.add( (URIRef(uri), WILDLIFE.scientificName, Literal(nombre_cientifico)) )
	g.add( (URIRef(uri), WILDLIFE.shortDescription, Literal(descripcion)) )
	g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
	g.add( (URIRef(uri), WILDLIFE.kingdomName, Literal('Animal')) )
	g.add( ( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaMaiz.Fauna)) )

fauna(
	dbr['Grey-headed_dove'],
	"Paloma montaraz cabecigrís",
	"Leptotila plumbeiceps",
	"""La paloma montaraz cabecigrís tiene un tamaño de 25 cm de largo y pesa 155g. El dorso y las alas son de color 
	marrón oliva, y las partes inferiores son de color sombreado en blanco. La cola es amplia con punta de color blanco.
	Las aves jóvenes carecen de color gris en la cabeza.""",
	"http://i.imgur.com/0ViaN29.jpg"
)

fauna(
	dbr['http://dbpedia.org/page/Ruby-topaz_hummingbird'],
	"Tucusito rubí",
	"Chrysolampis mosquitus",
	"""Es un colibrí pequeño, de pico corto. Sus colores van desde el negro en su mayor parte, 
	con un distintivo color rojo en la parte de la coronilla. También posee tonalidades naranja
	y café oliva oscuro. Se lo halla en la Cordillera Occidental y otros lugares con tierras áridas.""",
	"http://i.imgur.com/ZefaXVe.jpg"
)

fauna(
	dbr['Greyish_piculet'],
	"Carpintero punteado",
	"Picumnus granadensis",
	"""Mide de 8 a 10 cm y pesa de 12 a 13 g. Presenta pico negro y corto. Tiene cuello café grisáceo y partes 
	superiores teñidas de oliva. La superficie superior de su cola es café oscura con estrías en los márgenes 
	internos del par central de plumas. Mejillas, barbilla y garganta blanquecinos con puntos negros. 
	La hembra se distingue porque presenta puntos blancos en la cabeza.""",
	"http://i.imgur.com/WiMJbSs.jpg"
)

fauna(
	dbr['Bar-crested_antshrike'],
	"Batará crestibarrado",
	"Thamnophilus multistriatus",
	"""Mide 15,7cm. Tiene los ojos amarillos. El macho tiene la coronilla blanca y negra. La hembra es castaña 
	por encima, lados de la cabeza y collar nucal estriado blanco y negro, partes inferiores en negro y blanco.""",
	"http://i.imgur.com/ZTiTTvy.jpg"
)

fauna(
	dbr['Flame-rumped_tanager'],
	"Sangretoro lomo de fuego",
	"Ramphocelus flammigerus",
	"""Mide en promedio 19 cm de longitud. El macho es negro con una mancha en la espalda de color
	rojo escarlata; el pecho anaranjado a rojo y el vientre amarillo intenso. El pico es azul 
	cobalto o blancuzco con punta negra. La hembra tiene el dorso marrón oliváceo con pintas oscuras; 
	pecho y vientre amarillo claro.""",
	"http://i.imgur.com/udtsGTS.jpg"
)

fauna(
	dbr['Large-billed_seed_finch'],
	"Semillero piquigrande",
	"Oryzoborus crassirostris",
	"""Mide 13,5 cm de largo. Se caracteriza por su pico robusto y ancho en la base aunque relativamente corto 
	de color gris. Los machos tienen el plumaje totalmente negro, a excepción de una pequeña 
	mancha blanca en las alas, mientras que las hembras son de color pardo grisáceo.""",
	"http://i.imgur.com/maOVQKf.jpg"
)

fauna(
	dbr['Cinnamon_teal'],
	"Pato colorado",
	"Anas cyanoptera",
	"""Pato pequeño de 38-43 cm de longitud. El macho tiene ojos rojos, espalda 
	negruzca moteada, rabadilla y cola negras; la hembra tiene el color del cuerpo más oscuro, el pico más grande y 
	espatulado y la frente más pronunciada, sus ojos son de color avellana. En ambos sexos se observa un parche 
	azul pálido en las alas.""",
	"http://i.imgur.com/w8vAGpk.jpg"
)

fauna(
	dbr['Great_egret'],
	"Garza blanca",
	"Ardea alba",
	"""Mide entre 88 y 104 cm, pesa 900 gramos alcanzando algunas el kilogramo. En promedio, los machos son 
	ligeramente más grandes que las hembras.""",
	"http://i.imgur.com/XcvcXho.jpg"
)

fauna(
	dbr['Yellow-headed_gecko'],
	"Geco cabeza amarilla",
	"Gonatodes albogularis",
	"""Los adultos tienen una longitud total de sólo 6 cm. Es activo durante el día. Los machos son muy visibles,
	con la cabeza amarilla y el cuerpo de color azul oscuro a negro. A temperaturas más frías durante la noche,
	sus colores se desvanecen, a una coloración gris o azul-verdosa (machos). Las hembras son lagartos moteados grises,
	 a menudo con una línea clara en el cuello.""",
	"http://i.imgur.com/puGypO1.jpg"
)

fauna(
	dbr['Anolis_fuscoauratus'],
	"Camaleón sabanero",
	"Anolis auratus",
	"""Alcanza una longitud de entre 52 y 58 mm, es un lagarto pequeño con el cuerpo corto y comprimido; 
	las extremidades son largas; la cabeza es alargada y ligeramente deprimida en la parte frontal.
	La coloración es café-gris o café-chocolate con una raya amarilla brillante en ambos lados que va desde 
	la cabeza hasta las extremidades posteriores.""",
	"http://i.imgur.com/GmRbMrK.jpg"
)

fauna(
	dbr['Rainbow_whiptail'],
	"Cotejos o lagartijas azules",
	"Cnemidophorus lemniscatus",
	"""Se encuentra en los paises de Colombia, Venezuela, Ecuador, Panamá, Guyana y Brasil. 
	Es un lagarto de garganta azul y cuerpo de puntos blancos.""",
	"http://i.imgur.com/SwAA6fV.jpg"
)

fauna(
	dbr['White-lipped_mud_turtle'],
	"Tortuga del fango de boca blanca",
	"Kinosternon leucostomum",
	"""Tiene el caparazón de color marrón oscuro. No tiene ni dibujos ni casi
	se le marca los escudos de crecimiento. El plastrón es amarillo o amarillo con manchas oscuras.
	La cabeza es oscura, con la mandíbula de color amarillo claro y una mancha amarilla en ambos
	lados de la cabeza.""",
	"http://i.imgur.com/dTOXhTA.jpg"
)

fauna(
	dbr['Colostethus_fraterdanieli'],
	"Rana silbadora",
	"Colostethus fraterdanieli",
	"""Especie de rana de la famila Dendrobatidae, es endémica en los Andes de Colombia (Coordillera central
	y Occidental). Vive en el suelo cerca de los arroyos en los bosques de niebla y en los bosques tropicales secos.""",
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
	Casanare, Antioquia, Boyacá, Valle del Cauca, entre otros. Los machos presentan dos espinas medianas 
	en cada pulgar y hendiduras bucales bien desarrolladas. La superficie dorsal es lisa y de color marrón a oliva,
	mientras el vientre presenta un patrón moteado y puntos claros en la región gular.""",
	"http://i.imgur.com/AHG1ELR.jpg"
)

fauna(
	'https://www.wikidata.org/wiki/Q5546624',
	"Besudo",
	"Ichthyoelephas longirostris",
	"""Pez similar al bocachico, pero que se distingue por su boca más prominente, con el labio superior mucho más grueso, los ojos relativamente pequeños
	y por la ausencia de la espina predorsal, característica de los bocachicos.""",
	"http://i.imgur.com/lagzgEh.jpg"
)

fauna(
	dbr['Prochilodus_magdalenae'],
	"Bocachico",
	"Prochilodus magdalenae",
	"""El bocachico es un pez migratorio de agua dulce, su tamaño es mediano, los ejemplares más grandes pueden alcanzar 
	los 60 cms de longitud, su boca es pequeña, carnosa y prominente lo cual da origen a su nombre común.""",
	"http://i.imgur.com/HnMP0Yw.jpg"
)

fauna(
	dbr['Red_junglefowl'],
	"Pollo de engorde",
	"Gallus gallus",
	"""Posee dos tipos de protuberancias carunculares en la cabeza: una cresta en el píleo y unos lóbulos que cuelgan a ambos lados del pico.
	Los machos son más grandes, miden aproximadamente 50 cm de altura y llegan a pesar hasta 4 kgs. Las gallinas no suelen medir más de 40 cm de altura 
	y apenas llegan a 2 kg de peso. Poseen una coloración notablemente menos llamativa.""",
	"http://i.imgur.com/4GG3jmG.jpg"
)

fauna(
	dbr.Chicken,
	"Gallinas ponedoras",
	"Gallus domesticus",
	"""Las gallinas denominadas ponedoras provienen de cruces a tres vías de razas puras (Leghor, Rhode Island, New Hampshire, Ply Mouth rock, Wyandontte y Sussex Armiñada)
	y más recientemente con razas sintéticas recesivas para obtener pollitos autoxesados.""",
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
	Se pueden levantar sobre las patas traseras para llegar a las hojas o frutos de los árboles.""",
	"http://i.imgur.com/r3z36ib.jpg"
)

fauna(
	dbr['Cane_toad'],
	"Sapo neotropical",
	"Rhinella marina",
	"""También conocido como sapo de caña, es un animal que destaca por su grandeza física
	y por ser uno de los más antiguos que se hayan descubierto. Mide usualmente de 10 a 15 centímetros,
	pero se han encontrado algunos ejemplares más grandes.""",
	"http://i.imgur.com/p9v212l.jpg"
)

fauna(
	dbr['Dendropsophus_columbianus'],
	"Rana común",
	"Dendropsophus columbianus",
	"""La longitud rostro-cloacal del macho varía entre los 25,8 – 29,3 mm y en las hembras varía entre
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
	"""Es un anfibio de gran tamaño de entre 10 y 20 cm de longitud hocico-cloaca y un peso entre 60 y 900 grs. 
	Sus larvas son excepcionalmente grandes, pudiendo medir entre 15 y 18 cm. Su cabeza es ancha y plana y
	presenta un pliegue de piel a cada lado que corre desde detrás del ojo hasta el tímpano, bordeándolo.""",
	"http://i.imgur.com/inUup4b.jpg"
)

fauna(
	dbr['South_American_snapping_turtle'],
	"Tortuga mordedora",
	"Chelydra acutirostris",
	"""Pesa de 4,5 a 16 kg. Su caparazón  mide de 20 a 47cm. y una cola tan larga como el caparazón. La cola tiene escamas en forma de sierra.
	La piel es gris bronce con algunas manchas amarillas o blancas.""",
	"http://i.imgur.com/JCOlQxj.jpg"
)

fauna(
	dbr['White-lipped_mud_turtle'],
	"Morrocoy",
	"Chelonoidis carbonaria",
	"""La tortuga Morrocoy es terrestre y vive durante muchos años, puede alcanzar una longitud de hasta 51 cm 
	y su caparazón es alto con forma de cúpula, éste tiene el fondo de color negro y centros de las escamas 
	amarillo-naranjas o naranja-rojizos.""",
	"http://i.imgur.com/u9TOI9Z.jpg"
)

fauna(
	dbr['Black_vulture'],
	"Gallinazo",
	"Coragyps atratus",
	"""Mide aproximadamente entre 56 y 66 cm, tiene un peso en la hembra de 1940 grs y en el macho un peso de 1180 grs.
	Es un ave compacta de cola corta cuadrada y de alas anchas.""",
	"http://i.imgur.com/zU1wL0J.jpg"
)

fauna(
	wiki.Q5074452,
	"Guardacaminos o esterilla",
	"Lyophis lineatus",
	"""Especie de serpiente no venenosa e inofensiva. Se caracteriza por tener el dorso amarillo brillante con 
	tres líneas longitudinales negras dorsales: una vertebral ancha y una lateral a cada lado; en la parte anterior 
	las laterales se transforman en hileras de manchas negras. La cabeza es gris olivácea con línea pre-postocular negra.""",
	"http://i.imgur.com/aaLMr6S.jpg"
)

fauna(
	wiki.Q5128682,
	"Esquinco espalda dorada",
	"Mabuya unimarginata",
	"""Es un scíncido grande, hasta 75 mm. Esta lagartija tiene cuerpo elongado, cilíndrico y con notoria 
	reducción en el tamaño de los miembros. El cuerpo está cubierto por escamas cicloides brillantes. 
	La coloración dorsal es café bronceado, tiene una franja lateral gris blancuzca que se origina en el hocico.""",
	"http://i.imgur.com/1tSW3yy.jpg"
)

fauna(
	dbr['Sciurus_granatensis'],
	"Ardilla",
	"Sciurus Granatensis",
	"""Las hembras adultas pesan aproximadamente 465grs, durante la temporada lluviosa 
	el color del pelaje es rojizo mientras que en tiempo seco cambia a un color más anaranjado, presentan el dorso 
	color ocre y el vientre varía de blanco a anaranjado. La cola es ocre con salpicaduras de negro.""",
	"http://i.imgur.com/oJFUM1y.jpg"
)

fauna(
	wiki.Q4672609,
	"Rana platanera",
	"Hypsiboas pugnax",
	"""Es una especie de anfibio de la familia Hylidae. Habita en gran parte de nuestro territorio, encontrándose 
	en los bosques, fincas, a la orilla de riachuelos, cultivos y hasta en los jardines de nuestras casas, 
	sin olvidar por supuesto los platanales.""",
	"http://i.imgur.com/Zc9L5br.jpg"
)

fauna(
	dbr['Iguana_iguana'],
	"Iguana",
	"Iguana iguana",
	"""Puede medir de 1,5 a 2 metros. El color verde de su piel le permite confundirse perfectamente con la vegetación.
	Su piel está recubierta de pequeñas escamas; tiene una cresta dorsal que recorre desde la cabeza 
	hasta la cola. Patas muy cortas y cinco dedos en cada pata, acabados en garras muy afiladas. Cola larga y 
	delgada bordeada por una hilera de afiladas escamas dorsales.""",
	"http://i.imgur.com/0hpaKMx.jpg"
)

fauna(
	dbr['Leptodactylus_insularum'],
	"Rana sapo boliviano",
	"Leptodactylus insularum",
	"""El macho es un poco más pequeño que la hembra y es de al menos 10 cms del hocico a la cloaca y la hembra hasta 12. 
	El dorso es de color marrón oscuro con manchas marrones grandes y oscuras. Una franja blanca está presente a lo 
	largo del labio superior. La superficie ventral es de color blanco a crema con un poco de pigmentación más oscura 
	acentuada en la garganta.""",
	"http://i.imgur.com/CnxC1e0.jpg"
)

fauna(
	dbr['Drymarchon_melanurus'],
	"Cazadora rabo negro",
	"Drymarchon melanurus",
	"""Especie de serpiente colubridae no venenosa. Puede tener una longitud de 180 a 240 cms. Tiene escamas suaves 
	predominantemente de color marrón claro, volviéndose negro hacia la cola. La parte inferior es a menudo de color 
	más claro.""",
	"http://i.imgur.com/kzLgBeT.jpg"
)

fauna(
	dbr['Hemidactylus_frenatus'],
	"Gecko casero común",
	"Hemidactylus frenatus",
	"""La cola es ligeramente más larga que la longitud hocico cloaca. La cabeza, garganta y cuerpo se encuentran 
	cubiertos por pequeñas escamas granulares. La coloración dorsal y ventral es blanco amarillento. No crece más de 6-15 cms, 
	y vive cinco años.""",
	"http://i.imgur.com/qJ5aRSn.jpg"
)

#print (g.serialize(format="pretty-xml")) 

