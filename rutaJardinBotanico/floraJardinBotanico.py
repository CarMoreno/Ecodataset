# -*- coding: utf-8 -*-

from rdflib import Namespace
from rdflib import URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from ontologias import WILDLIFE, CRUZAR, UMBEL

dbpedia = Namespace('http://dbpedia.org/resource/')
wikidata = Namespace('http://www.wikidata.org/entity/')
imgur = Namespace('http://i.imgur.com/')
rutaJardinFlora = URIRef('http://190.14.254.237/dataseteco/RutaDelJardinBotanico/Flora/')
gJardinFlora = Graph()


def flora(uri, nombre_comun, nombre_cientifico, descripcion, imagen):
    gJardinFlora.add( (URIRef(uri), RDF.type, WILDLIFE.TaxonName) )
    gJardinFlora.add( (URIRef(uri), WILDLIFE.commonName, Literal(nombre_comun) ) )
    gJardinFlora.add( (URIRef(uri), WILDLIFE.scientificName, Literal(nombre_cientifico)) )
    gJardinFlora.add( (URIRef(uri), WILDLIFE.shortDescription, Literal(descripcion)) )
    gJardinFlora.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
    gJardinFlora.add( (URIRef(uri), WILDLIFE.kingdomName, Literal('Vegetal')) )
    gJardinFlora.add( (URIRef(uri), UMBEL.isRelatedTo, rutaJardinFlora) )

flora(
	dbpedia['Piper_marginatum'],
	'Anicillo',
	'Piper anisatum',
	"""Arbusto pequeño de 1-4 m de alto. Con aroma a anís, tallos verde pálidos a amarillento.
	Hojas acorazonadas, de color verde pálido y color verde oscuro cuando secas de consistencia fuerte.""",
	imgur['AKS0cjO.jpg']
)

flora(
	'http://www.biodiversidad.co/fichas/2011',
	'Anturio blanco',
	'Anthurium mimphaerfolium',
	"""Es una planta tropical, originaria de la selva de Colombia. Debe ubicarse en un lugar de buena luz pero no de sol directo. Por lo que es ideal para interiores""",
	imgur['MSqrylr.jpg']
)

flora(
	dbpedia['Vachellia_farnesiana'],
	'Aromo',
	'Acacia farnesiana',
	"""Arbusto o  árbol espinoso de 1  hasta  8   m de altura, subcaducifolio,  de copa redondeada; hojas bipinnadas,
	alternas  y con 2 a 7 pares de foliolos  primarios opuestos y 10 a 15 foliolos secundarios.""",
	imgur['Jf7Cn0L.jpg']
)

flora(
	dbpedia.Anthurium,
	'Arrayán colorado',
	'Myrcia popayanensis',
	"""Árbol con una altura promedio de 18 m, con ramificación abundante, copa redonda de mediana amplitud y profundidad.
	Madera de color crema rojizo, brillo mediano y olor aromático.
	""",
	imgur['h4ZhXxd.jpg']
)

flora(
	wikidata['Q15357705'],
	'Arrayán',
	'Eugenia biflora',
	"""""",
	imgur['WrnyL0m.jpg']
)

flora(
	wikidata['Q15323512'],
	'Bihao',
	'Calathea lutea',
	"""Plantas grandes, llegan a medir 2 metros de altura o menos, crecen en bósques húmedos y tropicales de América central
	y el norte de Sudamérica, hasta el Perú""",
	imgur['WEWw56T.jpg']
)

flora(
	dbpedia['Theobroma_cacao'],
	'Cacao',
	'Theobroma cacao',
	"""Arbol de pequeña talla, de 4 a 7 m de altura (cultivado). El cacao silvestre puede crecer hasta 20 m o más.  Se presentan muchas
	flores en racimos a lo largo del tronco y de las ramas.""",
	imgur['sjIayyV.jpg']
)

flora(
	wikidata['Q15521956'],
	'Carrizo',
	'Rhipidocladum racemiflorum',
	"""Tallos 10 a 15 m de largo y de 5 a 10 mm de ancho, rectos en la base, arqueándose arriba, se encuentra en América del norte, México
	y en el norte de Suramérica.""",
	imgur['RmapkWd.jpg']
)

flora(
	dbpedia.Guarea,
	'Cedro macho',
	'Guarea guidonia',
	"""Árbol de hasta 25 metros de altura y con diámetro de hasta 1 m. Follaje denso y tronco recto con flores blanco-verdosas, la madera tiene
	un peso moderado y un peso específico de 0.51 g por cm3.""",
	imgur['EPWPLRN.jpg']
)

flora(
	wikidata['Q6035263'],
	'Chagualo',
	'Myrsine guianensis',
	""" Su crecimiento es rápido y se desarrolla bien en suelos pobres y erosionados. Resiste bien podas fuertes y sus hojas son duras. Las flores y los frutos
	crecen agrupados en bolitas apretadas a lo largo de las ramas""",
	imgur['JgmDwhV.jpg']
)

flora(
	dbpedia['Sapindus_saponaria'],
	'Chambimbe',
	'Sapindus saponaria',
	"""Árbol pequeño que alcanza de 16 m a 25 m de altura. La hojas son alternas y miden de 9 a 50 cm de largo. Los frutos son bayas redondas de 15 mm de diámetro,
	color café lustroso, que contienen una pulpa pegajosa y una semilla de 1 cm de diámetro, redonda y negra. Tanto la pulpa como la semilla son venenosas.""",
	imgur['GAeX0Cw.jpg']
)

flora(
	dbpedia['Pithecellobium_dulce'],
	'Chiminango',
	'Pithecellobium dulce',
	"""Árbol espinoso de 15 a 20 m de altura, con ramas provistas de espinas. Copa piramidal o alargada, ancha y extendida (diámetro de 30 m), muy frondosa.
	Hojas en espiral aglomeradas de 2 a 7 cm de largo, su fruto son vainas delgadas de hasta 20 cm largo por 10 a 15 mm de ancho.
""",
	imgur['t3dWiLh.jpg']
)

flora(
	wikidata['Q15387993'],
	'Ciprés de Estacón',
	'Amyris pinnata',
	"""Árbol que crece hasta 10 m de altura. En Colombia se encuentra en los departamentos de Cundinamarca, Pereira,
	Valle del Cauca, Huila y Risaralda.""",
	imgur['rmqwFAR.jpg']
)

flora(
	wikidata['Q15379800'],
	'Coca montañera',
	'Erythroxylum ulei',
	"""Arbusto de 2.50 metros de alto. Hojas simples, alternas, elípticas u ovado-elípticas. Hasta 17 cm de longitud por 7 cm de ancho,
	su habitat natural es el bosque primario""",
	imgur['Yx5O3JU.jpg']
)

flora(
	dbpedia['Piper_aduncum'],
	'Cordoncillo',
	'Piper aduncum',
	"""Es un árbol pequeño de 2 a 6 m de alto. Con tallos verde pálidos, amarillentos o de color marrón y hojas verde oscuras en el haz.
	Fruto redondeado de 1,2 mm de longitud.""",
	imgur['4XNDIOZ.jpg']
)

flora(
	dbpedia.Clusia,
	'Cucharo',
	'Clusia sp.',
	"""Este árbol se propaga por semillas y por estacas. Los frutos se recolectan cuando toman un color verde amarillento
	o de color purpurina, generalmente a mediados y finales de cada año. Mide de 5 a 18 cm de altura""",
	imgur['hUG5ltd.jpg']
)

flora(
	'www.biolib.cz/cz/taxon/id1135636/',
	'Cuerno venado',
	'Xylosma prunifolia',
	"""El tronco es Ramificado desde la base, mide 1 m de alto y su corteza es fisurada y con espinas,
	las hojas son elípticas y las flores son pequeñas de amarillo cremoso, los frutos inicialmente son amarillos verdosos luego son rojizos y luego negro purpúreo.""",
	imgur['jAdLvLN.jpg']
)

flora(
	dbpedia.Zanthoxylum,
	'Doncel',
	'Zanthoxylum verrucosa',
	"""Árboles con espinas en forma de cono,  gruesas en los trocos y ramas delgadas en las partes terminales. Se encuentran en los bosques secundarios de Colombia y Ecuador.
	""",
	imgur['PDNWAAp.jpg']
)

flora(
	wikidata['Q15459116'],
	'Espino de mono',
	'Pithecellobium lanceolatum',
	"""Son Arbustos de 0.75 a 12 m de altura. Crece cerca de ríos, manglares, ciénagas y en áreas de selva abierta y muy húmeda.
	Se encuentra a lo largo de las tres cordilleras, en la zona Andina, en la costa atlántica y cerca de la Sierra Nevada de Sta. Marta.""",
	imgur['FcEWszo.jpg']
)

flora(
	dbpedia['Agave_americana'],
	'Fique',
	'Agave americana',
	"""Alcanza los 15 m de altura. Sus hojas son largas y rectas en la mayoría de los casos con espinas alrededor de las mismas,
	sus flores tienen pétalos amarillos, crece en regiones secas.""",
	imgur['u1q118R.jpg']
)

flora(
	dbpedia['Senna_spectabilis'],
	'Flor amarillo',
	'Senna spectabilis',
	"""Árbol de 8 a 20 m con el tronco recto hasta los 4 m. Sus flores poseen un intenso color amarillo de 4cm de diámetro, están presentes
	desde México hasta Argentina""",
	imgur['UyJuArz.jpg']
)

flora(
	dbpedia['Guazuma_ulmifolia'],
	'Guácimo',
	'Guazuma ulmifolia',
	"""Arbusto de 2 a 20 m con un tallo de 45 cm de diámetro, sus flores poseen un tono amarillento con petalos de 3mm, habita en los bosques
	secos tropicales y bosques húmedos tropicales. Resiste sequías y suelos pobres y arcillosos """,
	imgur['IJR35cB.jpg']
)

flora(
	dbpedia['Psidium_guineense'],
	'Guayaba agria',
	'Psidium guíñense',
	"""Esta planta comúnmente mide menos de 1m. Sus frutos son conocidos como Guayaba agria, son de color amarillento cuando están maduras,
	miden 2 cm.""",
	imgur['wYAjYY5.jpg']
)

flora(
	dbpedia['Tabebuia_chrysantha'],
	'Guayacán amarillo',
	'Tabebuia chrysantha',
	"""EL árbol alcanza unos 35m de alto, tiene pocas ramas aunque son gruesas y ascendentes. En Colombia está presente en los
	departamentos de Amazonas, Bolívar, Cesar, Chocó, Córdoba, Guaviare, Magdalena y Tolima.""",
	imgur['NY4l9eB.jpg']
)

flora(
	dbpedia['Tabebuia_rosea'],
	'Guayacán rosado',
	'Tabebuia rosea',
	"""Se encuentra en Colombia en los climas cálidos y templados en ambiente secos y húmedos, en el departamento de Cundinamarca,
	en la región del Urabá antioqueño, en la Sierra Nevada de Santa Marta y en la Amazonia.""",
	imgur['MnsUlJY.jpg']
)

flora(
	dbpedia['Malpighia_glabra'],
	'Huesito',
	'Malpighia glabra',
	"""Es una planta que alcanza los 8 m de altura. El tronco es bajo casi siempre. Las hojas son pequeñas y sus flores de color rosado.
	Se usa para fines ornamentales y medicinales. El fruto se consume en jugos, helados, jaleas y vinos. """,
	imgur['LwoZv14.jpg']
)

flora(
	dbpedia['Carludovica_palmata'],
	'Iraca',
	'Carludovica palmata',
	"""Es parecida a una plama, con sus hojas en forma de abanico. Las flores de color rosado claro y miden entre 15 y 20 cm
	Los frutos constituyen una masa que al madurar se vuelve de color rojizo, por dentro son carnosos.""",
	imgur['OpMLCpE.jpg']
)

flora(
	dbpedia['Genipa_americana'],
	'Jagua',
	'Genipa americana',
	"""Puede alcanzar de 15 a 20 m de altura y hasta 60 cm de diámetro. Sus frutos son bayas, toscos al tacto y con un aroma pentrante. 
	Se desarrolla bien en potreros y áreas de cultivo. Pero el mejor habitat para este arbusto es el suelo arcilloso.""",
	imgur['ZSkBpAq.jpg']
)

flora(
	dbpedia['Cinnamomum_verum'],
	'Jigua',
	'Cinnamomum sp.',
	"""La planta alcanza hasta de 15 m de altura, su ramaje está recubierto de una corteza de color amarillo. Las flores son blancas
	amarillosas y están puestas en racimos terminales. El fruto es una baya de color azul.""",
	imgur['UhZi2ZU.jpg']
)

flora(
	wikidata['Q6170902'],
	'Justarrazon',
	'Zanthoxylum monophyllum',
	"""Árbol que alcanza los 10 m de altura y los 25 cm de diámetro en su tronco, posee aguijones grandes por lo que se debe tener cuidado al manipularlo. 
	Se pueden encontrar en los bósques secos tropicales y bósques húmedos tropicales.
	""",
	imgur['Uj94xDa.jpg']
)

flora(
	dbpedia['Euphorbia_cotinifolia'],
	'Lechero',
	'Euphorbia cotinifolia',
	"""Este arbusto alcanza los 10 m de alto y su tronco los 20 cm de diámetro, posee un color verde rojizo, sus ramas segregan una sustancia blanca al igual que sus frutos.
	Las flores son de color blanco y estan ubicadas en los terminales.""",
	imgur['hkkuB3R.jpg']
)

flora(
	'http://www.theplantlist.org/tpl1.1/record/kew-2810881?ref=tpl1',
	'Matapalos',
	'Ficus involuta',
	"""Puede alcanzar de 10 a 35 m de altura, habita en los bosques húmedos y secos. Se los encuentra desde México hasta Perú
	""",
	imgur['ghmAv4a.jpg']
)

flora(
	dbpedia['Gliricidia_sepium'],
	'Matarraton',
	'Gliricidia sepium',
	"""Es un arbol con flores de color lila claro, con el centro de color amarillo de 1.8 a 2cm de diámetro,
	sus frutos son aplanados de un color verde amarillento. Es una especie orignaria de Centroamérica.""",
	imgur['JThQSWI.jpg']
)

flora(
	wikidata['Q15547475'],
	'Mestizo',
	'Cupania cinerea',
	"""Árbol que alcanza los 20 m de altura y 60 cm de diámetro en su tronco, de corteza lisa. Sus flore son blancas de 7 mm de diámetro y
	sus frutos son redondos de color café. Se encuentran en bosques húmedos tropicales y bosques húmedos.""",
	imgur['pspeS8s.jpg']
)

flora(
	dbpedia['Trichanthera'],
	'Nacedero',
	'Trichanthera gigantea',
	"""Crece en lugares con precipitaciones y temperaturas de 19 a 23.5 grados centígrados. Requiere de suelos profundos, aireados y de buen drenaje
	sus flores tienen estambres que sobresalen y su fruto mide de 1.5 a 2 cm de largo.""",
	imgur['obKicXb.jpg']
)

flora(
	dbpedia['Cordia_alliodora'],
	'Nogal',
	'Cordia alliodora',
	"""Aparece en suelos calcáreos preferiblemente, y que estén bien drenados, rara vez en suelos arenosos. También
	viven en suelos arcillosos y roca, pero evitan los suelos pantanosos. Invaden los terrenos agricolas abandonados.""",
	imgur['lnLWReS.jpg']
)

flora(
	wikidata['Q21302707'],
	'Olivón',
	'Vernonia brasiliana',
	"""En Colombia se encuentra en los departamentos de Tolima y Valle del Cauca, llega a medir 3 m de altura aproximadamente.""",
	imgur['sxCf0zV.jpg']
)

flora(
	dbpedia['Urera_baccifera'],
	'Ortiga',
	'Urera baccifera',
	"""Arbusto de 1 a 6 m de altura con hojas anchas y ovaladas, tallo con pelos urticantes. La infusión de la raíz es usada medicinalmente 
	para la inflamación y la diabetes.""",
	imgur['e2v1rr9.jpg']
)

flora(
	dbpedia['Sabal_mauritiiformis'],
	'Palmicha',
	'Sabal mauritiiformis',
	"""Es una palma solitaria y sin espinas que alcanza 20 m. de altura,  en su estado juvenil es de color verde, sus flores son de color verde amarillento
	o blancuzco en algunos casos,  requiere de sombra en su estado juvenil y al madurar, abundante luz solar.""",
	imgur['trwCYPv.jpg']
)

flora(
	wikidata['Q15493663'],
	'Palo blanco',
	'Citharexylum kunthianum',
	"""Crece desde las cercanías de los cursos de agua hasta terrenos secos, es un árbol que puede alcanzar de 5 a 8 m. de altura, crece rápidamente
	pero su tiempo de vida es corto.""",
	imgur['vtSDfEG.jpg']
)

flora(
	wikidata['Q5837321'],
	'Pisamo',
	'Erythrina poeppigiana',
	"""Árbol de 20 a 30 m de altura y 70 cm de diámetro en su tronco, presenta protuberancias que parecen espinas y posee ramas gruesas.
	Sus frutos miden 12 cm de largo, alargados y de color café.""",
	imgur['nJD9sAG.jpg']
)

flora(
	dbpedia['Heliconia_latispatha'],
	'Platanillo',
	'Heliconia latispatha',
	"""La planta completa mide alrededor de 1.5 a 2.5 cm de altura, Las hojas son simples, envainadoras hacia la base. La flor es tubular y
	miden entre 35 y 40 mm de largo, con tres sépalos y tres pétalos fusionados, sin pelos y amarilla o anaranjada con márgenes verdes.""",
	imgur['uzHIEPB.jpg']
)

flora(
	'http://www.biodiversidad.co/fichas/984',
	'Platanillo',
	'Heliconia platystachys',
	"""Es una planta de uso ornamental, como flor de corte y empleada para la decoración de jardines o en macetas. Se halla en Costa Rica,
	Panamá y Venezuela. En Colombia está presente en todas las regiones bajas, excepto en la planicie amazónica y en la Orinoquía. """,
	imgur['gD6Tlvd.jpg']
)

flora(
	dbpedia['Heliconia_rostrata'],
	'Platanillo',
	'Heliconia rostrata',
	"""""",
	imgur['5UfQkpf.jpg']
)

flora(
	wikidata['Q311933'],
	'Platanillo',
	'Heliconia wagneriana',
	"""Se localiza con frecuencia en el sector occidental de la planicie amazónica, la Serranía de la Macarena y
	la vertiente oriental andina, llega amedir de 3 a 6 m de altura.""",
	imgur['a50fa9j.jpg']
)

flora(
	wikidata['Q6136704'],
	'Sancona',
	'Syagrus sancona',
	"""Es una plama que crece hasta 30 metros de alto y de 25 a 30 cm de diámetro, crece en zonas de bosque seco y
	de bosque húmedo tropical. Está distribuida en toda la región andina y en algunas aledañas.""",
	imgur['rbMDbe3.jpg']
)

flora(
	wikidata['Q3004383'],
	'Sangregao',
	'Croton gossypiifolius',
	"""Es un árbol mediano con hojas de hasta 25 cm de longitud. Se puede apreciar en bosques secos, los frutos que procude son consumidos
	por loros.""",
	imgur['Dx16ZjU.jpg']
)

flora(
	wikidata['Q15455303'],
	'Siete cueros',
	'Machaerium capote',
	"""Puede alcanzar los 20 m de altura y 1 metro de diámetro en su tronco, produce latex de color rojizo. Requiere de abundante luz y su crecimiento es lento,
	además de Marzo a Abril produce frutos. Se encuentra en Colombia, Ecuador y Panamá.""",
	imgur['FAA0s4V.jpg']
)

flora(
	dbpedia['Zanthoxylum_rhoifolium'],
	'Tachuelo',
	'Zanthoxylum rhoifolium',
	"""Árbol de hasta 15 m de altura, con tallos y ramas espinosos. Es usada para leña y elaboración de cercados.""",
	imgur['mhd5XZF.jpg']
)

flora(
	wikidata['Q14830734'],
	'Totocal',
	'Achatocarpus nigricans',
	"""Puede alcanzar los 12 m de altura y los 20 cm de diámetro, sus ramas tienen espinas y es de color verdoso, sus hojas miden 10 cm de largo por 4.5 cm de ancho y sus frutos 
	son bayas con forma de globo, carnosos y posen de una dos semillas.""",
	imgur['ngqQnc8.jpg']
)

flora(
	wikidata['Q15526615'],
	'Trompillo',
	'Trichilia pallida',
	"""Puede llegar a medir hasta 20 m de altura y 35 cm de diámetro en el tronco, su corteza viva es quebradiza, fibrosa y delgada. Sus hojas
	llegan a medir 15 cm de largo por 10 cm de ancho. Está presente en los departamentos de Cundinamarca, Risaralda y Quindío.""",
	imgur['2X2dTHN.jpg']
)

flora(
	dbpedia['Lantana_camara'],
	'Venturosa',
	'Lantana camara',
	"""Arbusto de 1 a 3 m de altura con flores de color amarillo, anaranjadas o rojas. Sus frutos son carnosos, redondos de color azul a negro brillante.
	Se usa medicinalmente ya que el zumo de sus hojas con algunas gotas de limón puede curar el vómito.""",
	imgur['Z0E5BdL.jpg']
)

flora(
	dbpedia['Trema_micrantha'],
	'Zurrumbo',
	'Trema micrantha',
	"""Puede medir hasta 20 m de altura y 40 cm de diámetro en el tronco, sus hojas son simples y miden de 4 a 14 cm de largo. EN cuanto a sus flores, son pequeñas y de color verde
	con frutos pequeños amarillos o naranjas.""",
	imgur['Z0E5BdL.jpg']
)

flora(
	dbpedia['Leucaena_leucocephala'],
	'Leucaena',
	'Leucaena glauca',
	"""Es una especie que se adapta a una gran variedad de suelos siempre y cuando estén bien drenados y no tengan un nivel de acidez exagerado.
	Es nativa de México, pero se puede encontrar hasta Nicaragua, Guatemala, Honduras y El Salvador.
	""",
	imgur['NdKc3qr.jpg']
)

flora(
	wikidata['Q2713013'],
	'Guaimaro',
	'Brosimum utile',
	"""El árbol puede medir de 35 a 40 m de altura y 75 a 150 cm de diámetro, segrega un látex cremoso blanquecino, abundante y pegajoso. Produce 
	flores de color blanco y algunos frutos pequeños.""",
	imgur['XJDondS.jpg']
)

# flora(
# 	wikidata['Q15329296'],
# 	'Platanillo',
# 	'Heliconia caquetensis',
# 	"""Es una especie endémica en la vertiente oriental de los Andes Colombianos (Caquetá), produce flores de color amarillo, puede alcanzar de 2 a 2.5 m de altura.""",
# 	imgur['']
# )

flora(
	wikidata['Q15330199'],
	'Platanillo',
	'Heliconia combinata',
	"""Es un a especie endémica de las veritnetes Occidental y Andina en Colombia. Presente en los dpartamentos de Antioquia, Risaralda, Chocó y Valle del Cauca, puede llegar 
	a medir de 4 a 7 m de altura, produce flores de color amarillo.""",
	imgur['zjeNZ2i.jpg']
)

flora(
	wikidata['Q15330315'],
	'Platanillo',
	'Heliconia cordata',
	"""Se encuentra en el valle medio del río Magdalena, en el macizo antioqueño y en las vertientes occidental andina y magdalenense.
	Produce flores verdes o blancas hacia la base y verdes hacia el ápice.""",
	imgur['']
)

flora(
	dbpedia['Heliconia_episcopalis'],
	'Platanillo',
	'Heliconia episcopalis',
	"""Puede llegar a medir de 2 a 4 m de altura con flores blancas hacia la base, amarillas a verdes o anaranjadas hacia el ápice, está
	distribuida ampliamente en Ecuador, Perú, Surinam y Venezuela. En Colombia se encuentra en la llanura del Caribe, valle medio del río Magdalena, Amazonia y Orinoquía. """,
	imgur['gWPoBBU.jpg']
)

flora(
	wikidata['Q15330243'],
	'Platanillo',
	'Heliconia huilensis',
	"""Puede llegar a medir hasta 4.5 m de altura, posee flores amarillas y parabólicas, es una especie endémica de la vertiente magdalenense y del Macizo Colombiano (Cundinamarca y Huila).
	En Colombia se encuentra en peligro crítico.""",
	imgur['LiBgkDl.jpg']
)

flora(
	wikidata['Q15330807'],
	'Platanillo',
	'Heliconia intermedia',
	"""Puede llegar a medir hasta 3.5 m de altura y es endémica de la vertiente occidental andina de Colombia (Valle del Cauca y Chocó).
	Posee flores blancas hacia la base y amarillas hacia el ápice.""",
	imgur['Lf3s4Gd.jpg']
)

flora(
	wikidata['Q15329752'],
	'Platanilla',
	'Heliconia mariae',
	"""Puede llegar a medir de 4 a 7.5 m de altura, tiene una vida larga. Se usa para la decoración de jardínes o macetas y se puede encuentrar en Belice,
	Costa Rica, Guatemala, Honduras, Nicaragua, Panamá y Venezuela. En Colombia está presente en el valle del río Atrato y la planicie del Caribe.""",
	imgur['rpgKTTD.jpg']
)

flora(
	'http://www.biodiversidad.co/fichas/993',
	'Platanillo',
	'Heliconia venusta',
	"""Llega a medir de 2 a 3 m de altura, con flores amarillas, verdes hacia el ápice. Se usa mayormente para fines ornamentales y de decoración de jardínes.
	Se distribuye ampliamente en la región Andina, en las vertientes caucana, del magadalena y occidental andina y en el peniplano de Popayán.""",
	imgur['5U3hoix.jpg']
)

flora(
	wikidata['Q15330572'],
	'Platanillo',
	'Heliconia mutisiana',
	"""Puede tener una altura de 2.5 a 4 m con flores amarillas y parabólicas, es una especie nativa de Colombia según el Jardín Botánico del Quindío, se la puede encontrar
	en las vertientes andinas que miran hacia los valles de los ríos Cauca y Magdalena.
	""",
	imgur['j03E84S.jpg']
)

flora(
	'http://www.biodiversidad.co/fichas/982',
	'Heliconia',
	'Heliconia orthotricha',
	"""Se halla en Ecuador y Perú, llega a medir de 2.5 a 3.5 m de altura, Esta planta es usada como flor de corte,
	y tambien para la decoración de jardines y macetas. En Colombia está presente en la vertiente oriental andina y en la planicie amazónica.""",
	imgur['NBz56ct.jpg']
)


flora(
	dbpedia['Heliconia_psittacorum'],
	'Platanillo',
	'Heliconia psittacorum',
	"""Puede llegar a medir de 0.5 a 1.5 m de altura, sus flores son anaranjadas, rojas o amarillas. En Colombia se encuentra en los Llanos Orientales
	y en las serranías dispersas de Arauca, Casanare, Meta y Vichada, en algunas localidades de la selva amazónica (Guaviare) y en la vertiente oriental andina.""",
	imgur['sB1RGFR.jpg']
)

flora(
	dbpedia['Heliconia_stricta'],
	'Platanillo',
	'Heliconia stricta',
	"""Mide entre 1,5 a 3 m de altura, las hojas son simples y envainadoras hacia la base. Las flores se encuentran agrupadas, miden entre 30 y 45 cm de largo y 15 y 25 cm de diámetro,
	de color verde hacia el ápice y la punta es blanca. """,
	imgur['PHAYprq.jpg']
)

flora(
	dbpedia['Acrocomia_aculeata'],
	'Corozo grande',
	'Acrocomia sclerocarpa',
	"""Palma solitaria que alcanza los 11 m de altura. Su tallo mide hasta 30 cm de diámetro, es de color gris y está cubierto de espinas negras dispuestas en filas horizontales.
	Se encuentra desde México y las Antillas hasta Bolivia, Argentina y Paraguay. """,
	imgur['CkB8hMl.jpg']
)

flora(
	dbpedia['Aiphanes_horrida'],
	'Corozo',
	'Aiphanes caryotifolia',
	"""El tronco de esta palma alcanza entre 5 y 10 m de alto y entre 15 y 20 cm de diámetro, y está densamente cubierto por espinas negras.
	Es medicinal pues se emplea como en los niños para tratar retorcijones, flatulencia y cólicos.""",
	imgur['TWWaeyu.jpg']
)

flora(
	dbpedia['Astrocaryum_chambira'],
	'Chambira',
	'Astrocaryum chambira',
	"""Palma solitaria, puede llegar a medir 3.5 a 22 m de altura y 19 a 35 cm de diámetro, cubierto con espinas planas negras, produce frutos de color verde
	o  amarillo verdoso cuando están maduros, tiene una amplia distribución en el oeste de la Amazonía.""",
	imgur['wQvNiw2.jpg']
)

flora(
	wikidata['Q15457764'],
	'Guerregue',
	'Astrocaryum malybo',
	"""Es una palma solitaria y espinosa. Sus hojas crecen unos 5 m de largo. Esta en peligro a nivel global y 
	sus hojas se usan como fuente de fibras para la elaboración de esteras y de una amplia gama de artesanías""",
	imgur['f4pzDA8.jpg']
)

flora(
	dbpedia['Astrocaryum_standleyanum'],
	'Chunga',
	'Astrocaryum standleyanum',
	"""Palma alta y robusta que alcanza alturas hasta de 22 m con una tallo erguido de 16 a 22 cm de diámetro,
	con abundantes espinas largas de color negro. Presenta de 11 a 18 hojas grandes hasta de 4 m de largo.""",
	imgur['m0s4dFo.jpg']
)

flora(
	dbpedia['Attalea_osmantha'],
	'Palma de cuesco',
	'Attalea butyracea',
	"""Es una palma de crecimiento lento que tarda entre 4 y 6 meses en germinar, puede alcanzar hasta 20 metros de altura y 45 cm de diámetro en su tronco
	Se puede encontrar desde México hasta Bolivia. """,
	imgur['2EdeO1o.jpg']
)

flora(
	wikidata['Q5711222'],
	'Táparo',
	'Attalea allenii',
	"""Palma solitaria, se cree que tiene una longevidad entre 65 y 102 años. Sus semillas son comestibles, tienen un sabor similar al coco y son comercializadas
	a nivel local en los Andes antioqueños. """,
	imgur['e0tHbON.jpg']
)

# flora(
# 	wikidata['Q15458251'],
# 	'Yagua',
# 	'Attalea insignis',
# 	"""Tiene un tallo corto cubierto por bases de hojas persistentes que miden de 5 a7 m de largo. Sus frutos, uno por rama, son de color anaranjado, tienen una punta
# 	aguda y miden de 7 a 8 cm de largo.""",
# 	imgur['']
# )

flora(
	wikidata['Q15457188'],
	'Almendrón',
	'Attalea nucifera',
	"""Palma de tallo subterráneo y grandes hojas de hasta 8 m de largo, sus frutos miden de 5 a 7 cm de largo y son de color café, de sabor parecido al coco. 
	Es exclusiva de los bosques húmedos del Magdalena medio en Colombia y se encuentra en peligro de extinción por la destrucción de su hábitat.""",
	imgur['qxni3iT.jpg']
)

flora(
	dbpedia['Bactris_gasipaes'],
	'Chontaduro',
	'Bactris gasipaes',
	"""El tallo alcanza aproximadamente alturas mayores a 20 m, frecuentemente las plantas tienen alturas de 12 a 15 cm y un diámetro de entre 15 y 30 cm. Su fruto es de color
	verde cuando están inmaduros, rojos o anaranjados cuando están maduros; son comestibles al igual que la pulpa, la semilla y los tallos.""",
	imgur['FnkMwjx.jpg']
)

flora(
	dbpedia['Bentinckia_nicobarica'],
	'Palmera de Lord Bentick',
	'Bentinckia nicobarica',
	"""Se encuentran en el borde oriental de la Bahía de Bengala, en la isla de Nicobar. Es originaria del continente asiático y una palma solitaria. Los tallos
	de esta plama son usados por las población local para la construccion de casas y cercas.""",
	imgur['200mfte.jpg']
)

flora(
	dbpedia['Caryota_mitis'],
	'Cola de pescado',
	'Caryota mitis',
	"""Esta palma presenta tallos agrupados de hasta 15 cm de diámetro. Sus hojas miden de 2 a 3 m de largo. Es una especie ornamental y se puede encontrar en ambientes húmedos y suelos orgánicos.""",
	imgur['5gLq21x.jpg']
)

flora(
	wikidata['Q5764286'],
	'Palma bambú',
	'Chamaedorea pinnatifrons',
	"""Es una palma de tallo solitario de color verde, de hasta 2.5 metros de alto y entre 1 y 2 cm de diámetro. Sus frutos son de forma elipsoide y miden menos de 0,6 cm de diámetro, son de color naranja a negro
	dependiendo de su madurez.""",
	imgur['J9fcvxG.jpg']
)

flora(
	dbpedia['Dypsis_lutescens'],
	'Palma Areca',
	'Dypsis lutescens',
	"""Esta palma tiene un tallo cilíndrico de color gris, que alcanza los 5 m de altura y los 15 cm de diámetro. Su fruto es una baya de color amarillo oscuro a negro que mide hasta 1,5 cm de largo.
	Además sirve de alimento para la avifauna y para la apicultura ya que es una especie melífera. """,
	imgur['mXJPnm1.jpg']
)

flora(
	'http://www.arbolesornamentales.es/Dypsismadagascariensis.htm',
	'Palma de Madagascar',
	'Dypsis madagascariensis',
	"""Es una especie útil en la decoración de interiores. Puede medir de 7 a 8 m. de altura y 25 cm. de grosor, con el tronco liso y anillado, la hoja de esta especie tiene un aspecto plumoso.
	Se multiplica por semillas que tardan casi 2 meses en germinar. Requiere buen suelo y humedad.
	""",
	imgur['pe9C4rl.jpg']
)

flora(
	dbpedia['Corypha_umbraculifera'],
	'Palma de Ceilán',
	'Corypha umbraculifera',
	"""Es una especie endémica de la India, aunque también se puede encontrar en Sri Lanka, Tailandia y China. Fue traida a Surinam por inmigrantes del este de India. Es una de las palmas más grandes
	del mundo ya que pueden alcanzar los 34 m de altura con un tronco de 1.4 m de diámetro.""",
	imgur['Ba9bJSi.jpg']
)

flora(
	dbpedia['Elaeis_guineensis'],
	'Palma aceitera',
	'Elaeis guineensis',
	"""Es una especie nativa del continente africano, que se caracteriza por su grueso tronco cubierto con fragmentos de las hojas ya caídas y por sus grandes racimos de frutos que presentan alto contenido de aceite.
	 Es una palma de rápido crecimiento con alta variabilidad genética, alto potencial reproductivo y larga expectativa de vida.""",
	imgur['DAOyYW7.jpg']
)

flora(
	dbpedia['Elaeis_oleifera'],
	'Palma nolí',
	'Elaeis oleifera',
	"""Es una palma de tallo solitario que llega hasta los 3 metros de altura, se puede encontrar desde Nicaragua hasta el noroccidente de Colombia, aunque tambien exiten ejemplares en menor medida en Surinam, Guayana Francesa,
	Perú, Ecuador y Brasil.""",
	imgur['ZiYbeZn.jpg']
)

flora(
	dbpedia.Iriartea,
	'Bombona',
	'Iriartea deltoidea',
	"""Se encuentra en bosques primarios y bosques ribereños, puede alcanzar los 30 m de altura y hasta 30 cm de diámetro, tiene frutos de 2 a 3 cm de diámetro de color café amarillento al madurar, cáscara lisa, brillante y quebradiza.
	""",
	imgur['muCniYZ.jpg']
)

flora(
	dbpedia['Licuala_spinosa'],
	'Licuala de manglar',
	'Licuala spinosa',
	"""Es nativa de Indonesia, Filipinas, Península Malaya y Thailandia. Es una palma hermafrodita, sus troncos generalmente forman grupos, cada uno de 3 a 4 m de altura y 4 a 8 cm de grosor. Sus Frutos son esféricos u ovados y miden de 9 a 10 mm
	de longitud y son de color rojizo. Tolera suelos arenosos y sol o media sombra y necesita riegos abundantes.""",
	imgur['Iwvsknh.jpg']
)

flora(
	dbpedia['Mauritia_flexuosa'],
	'Palma de Moriche',
	'Mauritia flexuosa',
	"""Se encuentra en terrazas bajas, sobre terrenos inundados temporal o permanentemente, con drenaje muy deficiente. Fruto de 7 cm de largo y 5 cm de diámetro, rojo-anaranjado oscuro a café-rojizo cuando maduro. es muy rico en vitamina A,
	se consume fresco o en bebidas, paletas o refrescos.""",
	imgur['kPcLY4D.jpg']
)

flora(
	dbpedia['Oenocarpus_bataua'],
	'Palma Bataua',
	'Oenocarpus bataua',
	"""Palma solitaria, llega a medir de 4 a 26 m de alto y de 15 a 45 cm de diámetro. Se encuentra principalmente en zonas húmedas pantanosas con inundaciones periódicas, el fruto es de color violáceo, pero negro cuando madura, este mide de
	2.5 a 4.5 cm de longitud y de 2 a 3 cm de diámetro.""",
	imgur['Sn2doC9.jpg']
)

flora(
	dbpedia['Date_palm'],
	'Palma dátil',
	'Phoenix dactylifera',
	"""Esta palma solitaria alcanza 30 m de altura o más. Sus raíces son visibles en la base. Sus frutos de forma cilíndrica miden hasta 5 x 1,5 cm son de color café amarillento a café rojizo, son comestibles y carnosos. Sus hojas son útiles
	para la elaboración de una gran variedad de artículos como abanicos, recipientes y esteras. """,
	imgur['vkvSPL4.jpg']
)

flora(
	dbpedia['Rhapis_excelsa'],
	'Palma Rafis',
	'Rhapis excelsa',
	"""Esta palma alcanza de 90 a 120 cm de alto. La base de la hoja presenta una envoltura fibrosa café que cubre el tallo, sus flores son de color amarillento. Es de uso ornamental, útil para el embellecimiento del espacio público y
	para la decoración de exteriores e interiores.""",
	imgur['tIw7fa8.jpg']
)

flora(
	dbpedia['Roystonea_regia'],
	'Palma botella',
	'Roystonea regia',
	"""Puede llegar a medir 30 m de altura y a tener 60 cm de diámetro. Los frutos son  de color marrón rojizo o morado oscuro. Su tronco se emplea para obtener tablones, sus hojas para techar casas y sus frutos para la alimentación animal.
	La raíz en bebidas se usa como diurético para expulsar calculos por la orina""",
	imgur['ukBNjEu.jpg']
)

flora(
	dbpedia.Salak,
	'Salak',
	'Salacca edulis',
	"""Esta especie es nativa del continente oceánico y se encuentra en Borneo, Java, Malaya y Maluku. Reuqiere abundante agua durante la mayor parte del año. Es relativamente pequeña y espinosa, sus tallos están agrupados y se ramifican en la base.
	Las racies no se extienden a gran profundidad.""",
	imgur['1Lj38Y1.jpg']
)

flora(
	dbpedia['Syagrus_romanzoffiana'],
	'Gerivá',
	'Syagrus romanzoffiana',
	"""Esta palma de tallo largo y solitario alcanza de 10 a 15 m de altura, sus frutos son de color amarillo a anaranjado y comestibles, es una especie ornamental. El palmito también es comestible y sus hojas son de alimento para el ganado y las semillas
	trituradas son de alimento para las gallinas.""",
	imgur['uD8dqYu.jpg']
)


flora(
	wikidata['Q15470681'],
	'Falso Camedor',
	'Synechanthus fibrosus',
	"""Tallo solitario, delgado, liso, verde. Puede alcanzar de 5 a 6 m de altura t de 2 a 3 cm de diámetro. Está presente en Belice, Costa Rica, Guatemala, Honduras, golfo de México, sureste y suroeste de México y Nicaragua.""",
	imgur['fENpyrd.jpg']
)

flora(
	dbpedia['Washingtonia_filifera'],
	'Palma abanico',
	'Washingtonia filifera',
	"""Esta palma alcanza 24 m de alto y 120 cm de diámetro y la parte superior de su tallo está cubierto por hojas muertas. Sus flores son de color blanco. Sus frutos son pequeños y de color negro, es una especie ornamental. Se utiliza en las calles y parques de
	muchas ciudades tropicales y subtropicales como decoración. """,
	imgur['WGJzE6S.jpg']
)

flora(
	wikidata['Q15508512'],
	'Bambú de beecheya',
	'Bambusa beecheyana',
	"""Es una especie tropical que crece mejor en caliente, a suelo húmedo y bien drenado, a pleno sol. No es invasivo, pero se puede convertir rápidamente en una planta densa de numerosos tallos.
	Es muy común en China.""",
	imgur['4q9HzLU.jpg']
)

# flora(
# 	wikidata['Q10937031'],
# 	'Lemon Bamboo',
# 	'Bambusa tuldoides',
# 	"""Cultivada en las orillas de los ríos, Esta especie es usada en la fabricación de herramientas, principalmente en el enclavado de herramientas largas de poca dureza pero que requieren flexibilidad como para la recolección de frutos de palmas.""",
# 	imgur['']
# )

flora(
	dbpedia['Bambusa_longispiculata'],
	'Mahal Bamboo',
	'Bambusa longispiculata',
	"""Puede alcanzar una altura de 10 a 15 m, con un diámetro de 7 a 10 cm, es de color verde con pelos blancos en algunas partes. Esta planta es empleada como ornamental. Se encuentra en Colombia, Costa Rica, Ecuador, Salvador, Guatemala, Honduras,
	Puerto Rico, Nicaragua, Panamá, Estados Unidos e India. """,
	imgur['rCRDVDp.jpg']
)

flora(
	dbpedia['Bambusa_oldhamii'],
	'Giant Timber bamboo',
	'Bambusa oldhamii',
	"""Es una de las especies con mayor adaptabilidad, es de rápido crecimiento y no es invasor. Puede alcanzar de 12 a 18 m de altura, cuando sus tallos se maduran son usados para la cosntrucción de herramientas y decoración de interiores""",
	imgur['fY9BDVa.jpg']
)

flora(
	dbpedia['Bambusa_tulda'],
	'Bambú Bengal',
	'Bambusa tulda',
	"""SUs tallos forman grupos de 6 a 20 m de altura. Es uno de los bambúes mas importantes en Asia, especialmente en India, Bangladesh y el norte de Tailandia, donde sirve como comida y materiales para la construcción. Lo ideal es que este bambú se mantenga en
	un ambiente de 40 grados Fahrenheit y 100 grados Fahrenheit de temperatura para su correcto crecimiento.""",
	imgur['eLa4VGS.jpg']
)

# flora(
# 	wikidata['Q135731'],
# 	'Bambú Punting Pole',
# 	'Bambusa tuldoides',
# 	"""Es una especie muy común en China, cultivada en las orillas de los ríos. Auqnue tambipen es cultivada en regiones tropicales de todo el mundo. En condiciones muy favorables este bambú puede alcanzar un tamaño de 15 a 18 m de altura, se adapta a cualquier tipo de ambiente
# 	excepto a temperaturas demasiado frías.""",
# 	imgur['']
# )

flora(
	dbpedia['Bambusa_ventricosa'],
	'Bambú de buda',
	'Bambusa ventricosa McClure',
	"""Este bambú en sus condiciones ideales puede alcanzar una altura de más de 15 metros, durante su crecimiento disminuir a los entrenudos y formar una protuberancia característica. El tallo principal, como la de todo el bambú es hueco entre los nodos. Las hojas son de color verde.""",
	imgur['6c11eLT.jpg']
)

flora(
	dbpedia['Bambusa_vulgaris'],
	'Bambú',
	'Bambusa vulgaris',
	"""Bambusa vulgaris es una especie de la familia de los pastos, y a su vez del grupo del bambú, presenta tallos muy gruesos en forma de caña que pueden superar los 10 m de altura y son huecos en su interior. Tiene múltiples usos artesanales, medicinales, en el ámbito religioso,
	como planta ornamental, proporciona sombra y protección al suelo.""",
	imgur['lXk87cJ.jpg']
)

flora(
	dbpedia['Dendrocalamus_asper'],
	'Bambú Gigante',
	'Dendrocalamus asper',
	"""Tiene grandes tallos leñosos entre 20 y 30 m de altura y de 8 a 20 cm de diámetro. Además sus paredes son relativamente gruesas y se vuelven más delgadas hacia la parte superior del tallo, su color es verde pálido y está cubierto de pelos cortos de color marrón. Crecen bien en diferentes tipos de suelo,
	incluso en suelos arenosos ácidos, pero es preferible suelos bien drenados pesados​. """,
	imgur['ZXwBB1E.jpg']
)

flora(
	wikidata['Q15517583'],
	'Bambú Cadena',
	'Gigantochloa apus',
	"""Es una especie nativa del Suereste asiático, es el bambú económicamente más importante en la isla de Java, especialmente en la industria de la artesanía y muebles. Puede alcanzar de 8  22 m de altura, con un  diámetro de 4 a 13 cm, sus tallos son de color verde brillante o verde amarillento cuando es joven.
	esta especie de bambú crece bien ya sea en suelo arenoso o suelo arcilloso.""",
	imgur['N10KkE3.jpg']
)

flora(
	wikidata['Q15245801'],
	'Bambú Gombong',
	'Gigantochloa verticillata',
	"""Este bambú puede crecer de 7 a 30 metros de altura y de 5 a 13 cm de diámetro, el centro de la planta se eleva de manera irregular sobre el suelo. En Indonesia, esta especie es la segunda mas importante después apus Gigantochloa y desempeña un papel destacado en la economía rural. A veces se usa con fines ornamentales
	y de decoración.""",
	imgur['M9PRqrO.jpg']
)

flora(
	dbpedia['Melocanna_baccifera'],
	'Bambú Muli',
	'Melocanna baccifera',
	"""Es el bambú que produce el furto mas grande de la familia de las gramíneas, es carnoso y en forma de pera. Es muy común en la India, existe un evento en este país donde se celebra el florecimento de este tipo de bambú. Pueden llegar a medir de 10 a 20 m de altura y de 3 a 7 cm de diámetro. De color verde cundo estpan jovenes y más opaco cuando están viejos.
	""",
	imgur['Xc8UXTu.jpg']
)

print(gJardinFlora.serialize(format='pretty-xml'))