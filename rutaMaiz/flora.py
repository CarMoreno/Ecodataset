# -*- coding: utf-8 -*-

from rdflib import Namespace
from rdflib import URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from ontologias import WILDLIFE, CRUZAR, UMBEL
from fauna import g, rutaMaiz

dbpedia = Namespace('http://dbpedia.org/resource/')
wikidata = Namespace('http://www.wikidata.org/entity/')
ruta = URIRef('http://190.14.254.237/dataseteco/Maiz/')
floraRuta = URIRef('http://190.14.254.237/dataseteco/Maiz/Flora/')

def flora(uri, nombre_comun, nombre_cientifico, descripcion, imagen):
    g.add( (URIRef(uri), RDF.type, WILDLIFE.TaxonName) )
    g.add( (URIRef(uri), WILDLIFE.commonName, Literal(nombre_comun) ) )
    g.add( (URIRef(uri), WILDLIFE.scientificName, Literal(nombre_cientifico)) )
    g.add( (URIRef(uri), WILDLIFE.shortDescription, Literal(descripcion)) )
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
    g.add( (URIRef(uri), WILDLIFE.kingdomName, Literal('Vegetal')) )
    g.add( (URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaMaiz.Flora)) )

flora(
    dbpedia['Citrus_nobilis'],
    "Mandarina",
    "Citrus Nobilis",
    """El árbol es un frutal espinoso, con ramas delgadas, con las hojas tanto amplias como delgadas. 
    Las flores nacen simples o en grupos en las axilas de las hojas.""",
    "http://i.imgur.com/P0rzCMB.jpg"
)

flora(
    dbpedia['Citrus_sinensis'],
    "Naranja",
    "Citrus Sinensis",
    """El naranjo es un frutal de hasta 10 m de altura con la copa muy redondeada. Tallos ligeramente espinosos, 
    hojas coriaceas, flores de color blanco muy perfumadas.""",
    "http://i.imgur.com/aKWeHJj.jpg"
)

flora(
    dbpedia['Citrus_limon'],
    "Limón",
    "Citrus Limon",
    """El limonero es un frutal de porte mediano que puede llegar a vivir 70 años. De tronco leñoso, amarillento 
    y muy ramificado, sus grandes y ovaladas hojas de color verde brillante son muy aromáticas al igual que 
    sus flores.""",
    "http://i.imgur.com/JsCNYfk.jpg"
)

flora(
    dbpedia['Theobroma_cacao'],
    "Cacao",
    "Theobroma Cacao L.",
    """Arbusto pequeño de hasta 10 m. Tallo leñoso, recto, con brotes, corteza delgada de color café. Hojas perennes 
    grandes, alternas, colgantes. Flores casi permanentes pequeñas blancas a rosadas, nacen sobre el tallo. El 
    fruto nace en el tronco es una baya grande de hasta 30 x 12 cm.""",
    "http://i.imgur.com/CDEeJVu.jpg"
)

flora(
    dbpedia['Persea_americana'],
    "Aguacate",
    "Persea Americana",
    """Árbol de unos 10 m de altura. Tallo leñoso. Perennifolio, hojas alternas, pedunculadas, de color verde 
    brillante. Flores perfectas en racimos. Su fruto es una drupa de color verde y piel o cáscara delgada, rico 
    en proteínas y aceite vegetal.""",
    "http://i.imgur.com/R3mtPr3.jpg"
)

flora(
    dbpedia['Passiflora_edulis'],
    "Maracuyá",
    "Passiflora Edulis",
    """Planta perenne de hasta 9 m de longitud. Tallos trepadores, leñosos. Hojas alternas, trilobadas, verde 
    oscuras; brotes tiernos rojizos. Flores cremosas con tintes rosa palidos. Frutos comestibles.""",
    "http://i.imgur.com/QoGoZpf.jpg"
)

flora(
    dbpedia['Musa_paradisiaca'],
    "Plátano",
    "Musa × Paradisiaca L.",
    """Planta con el tallo bien desarrollado. Hojas grandes, oblongas, lámina con la vena media bien desarrollada 
    y numerosas venas paralelas, perpendiculares a la vena media.""",
    "http://i.imgur.com/3bfoEk5.jpg"
)

flora(
    dbpedia['Saccharum_officinarum_L'],
    "Caña de azúcar",
    "Saccharum Officinarum L.",
    """Es una planta perenne con un tallo macizo, de hasta 6 m de altura y 2 a 8 cm de diametro; aparece por lo 
    general deshojado en la parte inferior, está lleno de un tejido esponjoso y dulce del que se extrae el azúcar. 
    Sus hojas son largas y puntiagudas.""",
    "http://i.imgur.com/7K7gpog.jpg"
)

flora(
    dbpedia['Gynerium_sagittatum'],
    "Caña Brava",
    "Gynerium Sagittatum",
    """Es una planta silvestre de hasta 4 m de alto. Posee tallos gruesos, sólidos y muy resistentes que le han 
    permitido sobrevivir al tiempo. Las hojas son lineales y aserradas, dispuestas en dos filas.""",
    "http://i.imgur.com/R9UjZNK.jpg"
)

flora(
    dbpedia['Zea_Mays'],
    "Maíz",
    "Zea Mays",
    """Planta herbáceae que puede alcanzar hasta los 2,5 m de altura. El tallo internamente tiene una médula 
    de tejido esponjoso y blanco donde almacena reservas alimenticias, en especial azúcares. Las hojas son alargadas 
    arrolladas al tallo, del cual nacen las espigas o mazorcas.""",
    "http://i.imgur.com/6Ywbfgs.jpg"
)

flora(
    dbpedia['Heliconia_bihai'],
    "Heliconia",
    "Heliconia Bihai",
    """Es una planta muy llamativa por la inflorescencia que tiene en forma de espiga caracterizada por una serie de 
    espatas de color rojo-verde y amarillo. Puede llegar a alcanzar entre los 4 y 6 m de altura y las hojas 
    tienen forma de abanico.""",
    "http://i.imgur.com/wZ0GLbc.jpg"
)

flora(
    dbpedia.Cassava,
    "Yuca",
    "Manihot Sculenta",
    """Es un arbusto perenne, que alcanza los dos metros de altura. Su raíz es cilíndrica y oblonga, y alcanza 
    el metro de largo y los 10 cm de diámetro. La cáscara es dura e incomestible. La pulpa es muy rica en hidratos 
    de carbono y azúcares.""",
    "http://i.imgur.com/VYm4XpF.jpg"
)

flora(
    dbpedia['Carica_papaya'],
    "Papaya",
    "Carica Papaya",
    """Planta herbácea, de hasta 8m de altura; con látex lechoso. Tallos cilindrico, simple, sin ramificar, termina 
    en un penacho de hojas, de hasta 30 cm de diámetro. Flor de color amarillo, pétalos y sépalos del mismo color, 
    blanco amarilloso, nacen en el extremo del tallo, debajo de las hojas.""",
    "http://i.imgur.com/oAa8tSA.jpg"
)

flora(
    dbpedia['Solanum_pimpinellifolium'],
    "Tomate Cherri",
    "Lycopersicum Pimpinellifolium",
    """Planta anual de porte arbustivo o rastrero. Las hojas son sencillas, pecioladas y de limbo hendido. Toda 
    la parte verde de la planta está compuesta por pelos glandulares que al rozarse emiten un líquido con olor 
    característico. Las flores aparecen en racimos siendo el número de estas variable.""",
    "http://i.imgur.com/viCbqpn.jpg"
)

flora(
    dbpedia['Ananas_comosus'],
    "Piña",
    "Ananas Comosus",
    """Planta perenne terrestre, con forma de roseta abierta que produce uno de los frutos tropicales más consumidos. 
    Hojas en forma de espadas con diminutas y afiladas espinas en sus bordes.""",
    "http://i.imgur.com/yvXykAn.jpg"
)

flora(
    dbpedia['Psidium_guajava'],
    "Guayaba",
    "Psidium Guajava",
    """Arbolito de follaje persistente que puede alcanzar 4-6 ms de altura, con el tronco corto y algo tortuoso. Hojas 
    opuestas de 5-10 cms de longitud. Flores blancas, solitarias o en pequeños grupos, que aparecen en las axilas de las 
    hojas. Fruto en baya redondeada con el cáliz de la flor persistiendo.""",
    "http://i.imgur.com/e55G5DZ.jpg"
)

flora(
    dbpedia['Handroanthus_guayacan'],
    "Guayacán",
    "Tabebuia guayacan (Seem.) Hemsl.",
    """Es un árbol grande de hasta 40 ms de alto y 100 cms de diámetro con tronco recto, cilíndrico y raramente irregular 
    cuya base es ligeramente alargada. Produce una madera muy pesada y resistente a la pudrición.""",
    "http://i.imgur.com/9CmiV7U.jpg"
)

flora(
    dbpedia['Ceiba_pentandra'],
    "Ceiba",
    "Ceiba Pentandra (L.) Gaertn",
    """Árbol de 50 ms de altura, tallo de 2 ms de diámetro, abombado, corteza gris clara y anillada, copa 
    semihemisférica, follaje denso verde oscuro. Hojas compuestas y alternas, flores blancas.""",
    "http://i.imgur.com/V9Rfjpq.jpg"
)

flora(
    dbpedia['Cassia_fistula'],
    "Ébano Falso",
    "Cassia Fistula",
    """Árbol de 10-15 ms de alto; ramas de tendencia ascendente. Hojas grandes, caducas, ovadas, acuminadas y péndulas. 
    Flores dispuestas en grandes racimos pendulares, muy vistosas de color amarillo.""",
    "http://i.imgur.com/aUZVMJ4.jpg"
)

flora(
    dbpedia.Guadua,
    "Guadua",
    "Guadua Angustifolia",
    """La raíz es un rizoma que almacena los nutrimentos, estos rizomas producen raicillas adventicias, el tallo de 
    forma cilíndrica y con nudos, ramas solitarias y muy espinosas en los nudos basales y con presencia o no de hojas; 
    hojas lanceoladas verdes lustrosas.""",
    "http://i.imgur.com/WLLO9uD.jpg"
)

flora(
    dbpedia['Narcissus_primigenius'],
    "Narciso",
    "Narcissus Pseudonarcissus",
    """Es una planta de hojas estrechas y alargadas. Sus flores son de color blanco, amarillo o rosa y de forma simple. 
    La floración se produce en primavera. El fruto es una cápsula.""",
    "http://i.imgur.com/GcRveZA.jpg"
)

flora(
    dbpedia['Pelargonium_zonale'],
    "Geranio",
    "Pelargonium Zonale",
    """Hojas en forma generalmente acorazonada y de diferentes tonalidades de verde , de floración prolongada, 
    las flores se encuentran agrupadas de formas diversas y el colorido es muy variado, desde el blanco al rojo 
    pasando por el rosado.""",
    "http://i.imgur.com/RssuVMe.jpg"
)

flora(
    dbpedia['Viola_odorata'],
    "Violeta",
    "Viola Odorata",
    """Planta perenne rizomatosa que se expande mediante estalones y puede formar una buena cubierta de suelo, 
    sus hojas son radicales ligeramente festoneadas y acorazonadas en la base. Las flores son muy perfumadas; el 
    fruto es una cápsula que se abre en la madurez, su es color violeta y blanco.""",
    "http://i.imgur.com/rKrLqRo.jpg"
)

flora(
    dbpedia['Camellia_japonica'],
    "Camelia",
    "Camellia Japonica",
    """Arbusto ramificado de 2 metros de altura, hojas anchas elípticas con filo aserrado, haz de color verde oscuro 
    reluciente y el envés más pálido y coriáceo. Se adapta perfectamente a su cultivo en jardinera. Flores solitarias 
    de color variado rojo sangre, cereza, con rayas blancas o rosadas.""",
    "http://i.imgur.com/VUACRGI.jpg"
)

flora(
    dbpedia['Leucanthemum_vulgare'],
    "Margarita común",
    "Chrysanthemun Leucanthemum",
    """Es una planta herbácea con hojas hendidas. Las flores están siempre reunidas en una inflorescencia llamada 
    cabezuela o capítulo, que parece una única flor y funciona como tal.""",
    "http://i.imgur.com/A1j5930.jpg"
)

flora(
    wikidata.Q130918,
    "Dalia",
    "Dahlia spp.",
    """Planta herbácea o arbustiva anual, raíz tuberosa, hojas opuestas o verticiladas. Flores dispuestas en 
    inflorescencias compuestas o capítulo (rodeada por brácteas), de diferentes colores. Hay 30 especies y 
    20000 variedades.""",
    "http://i.imgur.com/Th4Plgi.jpg"
)

flora(
    dbpedia['Iris_germanica'],
    "Lirio común",
    "Iris germánica",
    """Tallo terminal con hojas en la base, 35 a 45 cms de largo; herbácea perenne de rizoma vistoso y grueso. 
    Hojas acintadas, erguidas, de borde liso, color verde oscuro a grisáceo. Flores de poca duración.""",
    "http://i.imgur.com/NDTPe0l.jpg"
)

flora(
    dbpedia['Hydrangea_macrophylla'],
    "Hortensia",
    "Hydrangea Macrophylla",
    """Planta semiarbustiva, caducifolia, puede llegar a medir 1,5 ms. Tallos ramosos, gruesos, derechos, 
    terminados por las flores agrupadas. Hojas grandes, verdes, opuestas, ovaladas con borde dentado.""",
    "http://i.imgur.com/VLAuVL6.jpg"
)

flora(
    dbpedia['Papaver_rhoeas'],
    "Amapola",
    "Papaver rhoeas",
    """Hierba anual, cubierta de pelos perpendiculares. Hojas simples en la base, alargadas y lobuladas. flores 
    solitarias con pétalos arrugados en botones florales, mostrando al abrirse un bello color rojo intenso, 
    por lo general presentan una mancha negruzca en la porción basal. El fruto de la amapola es una cápsula, 
    llena de semillas.""",
    "http://i.imgur.com/9RgVwBE.jpg"
)

flora(
    dbpedia['Murraya_paniculata'],
    "Jazmín Naranja",
    "Murraya Paniculata",
    """Planta con hojas compuestas, alternas, imparipinnadas; los foliolos de 1 a 4 cms de largo, verdes muy oscuros 
    y brillantes. Las flores blancas, pequeñas y fragantes.""",
    "http://i.imgur.com/6PuZR2z.jpg"
)

flora(
    wikidata.Q843363,
    "Begonia",
    "Begonia Semperflorens",
    """Herbácea perenne o anual, altura aproximada entre 20-40 cms. Tallo carnoso y ramificado, hojas ovales y 
    redondeadas con coloraciones rojizas en múltiples tonalidades. Las flores reunidas en cimas exilares de colores 
    rosa, rojo o blanco.""",
    "http://i.imgur.com/9Pn2uWH.jpg"
)

flora(
    dbpedia['Viola_x_wittrockiana'],
    "Pensamientos",
    "Viola x wittrockiana",
    """Son plantas híbridas, cuyo ciclo de vida es de un año, y que son cultivadas por sus vistosas flores. 
    Tienen hojas simples con forma de corazón y margen dentado de cinco pétalos aterciopelados, y con diversas 
    gamas de colores. Su floración abarca los meses otoñales, pero continua hasta la entrada de la primavera.""",
    "http://i.imgur.com/u8YKOy7.jpg"
)

flora(
    wikidata.Q93201,
    "Tulipán",
    "Tulipa spp",
    """Hierba perenn con bulbos o rizomas. Las hojas son alternas y espiraladas, se disponen a lo largo del tallo 
    o en una roseta basal. Flores erguidas muy llamativas, de numerosos colores, tardan hasta tres semanas en 
    marchitarse. El fruto es una cápsula, ocasionalmente una baya. Las semillas son planas y con forma de disco 
    o globosas.""",
    "http://i.imgur.com/JmDuDLg.gif"
)

flora(
    dbpedia['Chrysanthemum_morifolium'],
    "Crisantemo",
    "Chrysanthemum Morifolium",
    """Planta de tallo herbáceo y delgado, con hojas alternas suaves al tacto, palmeado, divididas, con bordes 
    dentados, nervaduras principal y secundarias, a la cabeza floral se le denomina capítulo.""",
    "http://i.imgur.com/w4aGjbg.jpg"
)

flora(
    dbpedia['Magnolia_grandiflora'],
    "Magnolia",
    "Magnolia Grandiflora L.",
    """Es un árbol de tamaño medio a grande de 20-30 ms de altura. Las hojas son perennes, simples o ampliamente 
    ovadas de 12-20 cms de longitud y 6-12 cms de ancho con los márgenes dentados, son de color verde oscuro y 
    se vuelven color marrón cuando llega el invierno.""",
    "http://i.imgur.com/p3tLqzX.jpg"
)

flora(
    dbpedia['Cattleya_trianae'],
    "Flor de mayo",
    "Cattleya Trianae",
    """Planta epífita, con pseudobulbos de largo variable que llevan a su extremidad una o a dos hojas sin pecíolo. 
    Flores vistosas que se desarrollan en el tallo.""",
    "http://i.imgur.com/A4H9iz7.jpg"
)

flora(
    wikidata.Q959222,
    "Pasto estrella",
    "Cynodon Plectostachium",
    """Es una gramínea perenne, de vida larga, frondosa y rastrera, produce estolones de rápido crecimiento, con 
    largos entrenudos y sus tallos pueden alcanzar hasta 3 ms de longitud. Posee hojas exuberantes con vellos en 
    forma de lanza. La inflorescencia presenta de 2 a 5 espiguillas solitarias de 2 a 3 mms.""",
    "http://i.imgur.com/biYwa69.jpg"
)

flora(
    dbpedia['Coffea_arabica'],
    "Café",
    "Caffea Arabica",
    """El cafeto es un arbusto o árbol pequeño, perennifolio, de fuste recto que puede alcanzar los 10 ms en 
    estado silvestre.""",
    "http://i.imgur.com/H2ZM3sf.jpg"
)

flora(
    dbpedia['Mangifera_indica'],
    "Mango",
    "Mangifera Indica",
    """El mango típico constituye un árbol de tamaño mediano, de 10-30 ms de altura. El tronco es más o menos recto, 
    cilíndrico y de 75-100 cms de diámetro, cuya corteza de color gris - café tiene grietas.""",
    "http://i.imgur.com/GtxlZkC.jpg"
)

flora(
    dbpedia['Allium_fistulosum'],
    "Cebolla larga",
    "Allium Fistulosum",
    """Las raíces se producen en la base del tallo, son fasciculadas y poco abundantes. Cada hoja tiene una base 
    larga y carnosa, que se une estrechamente con la base de las demás hojas. Las hojas son tubulares de 25-35 cms 
    de largo y 5-7 mms de diámetro. El tallo es un disco comprimido, de donde parten las raíces y la base de 
    las hojas.""",
    "http://i.imgur.com/u1nPyiR.jpg"
)

flora(
    dbpedia['Capsicum_annuum_var._minimum'],
    "Ají",
    "Capsicum Annuum",
    """Planta anual, que puede alcanzar hasta 1 m de altura, de tallos empinados y ramosos, con las hojas aovadas 
    y lanceoladas de bordes enteros o apenas sinuados en la base. Es especialmente productiva en zonas cálidas 
    y climas secos. Es una planta de huerta y de diversas variedades.""",
    "http://i.imgur.com/EBqG6Ox.jpg"
)

flora(
    dbpedia['Urtica_dioica'],
    "Ortiga",
    "Urtica Dioica",
    """Es una planta arbustiva perenne que puede alcanzar hasta 1,5 ms de altura. Tallos erectos cuadrangulares, 
    hojas verdes aserradas, puntiagudas, provistas al igual que el tallo de pelos urticantes. Flores en forma de 
    raíces, con flores unisexuales. Posee unos pelos urticantes que tienen la forma de pequeñisimas ampollas.""",
    "http://i.imgur.com/oVjUyH1.jpg"
)

flora(
    dbpedia['Rosmarinus_officinalis'],
    "Romero",
    "Rosmarinus Officinalis",
    """Arbusto perenne, verde, leñoso y muy aromático de hasta 2 ms de altura que crece espontáneamente o en cultivo. 
    Sus tallos ramificados con hojas rígidas, lineales, lanceoladas, en forma de aguja y de aspecto coriáceas las 
    recubre una capa de diminutos pelos.""",
    "http://i.imgur.com/umcF7Ne.jpg"
)

flora(
    dbpedia['Coriandrum_sativum'],
    "Cilantro",
    "Coriandrum Sativum",
    """Es una hierba anual de hasta 60 cms, sin pelos y brillante. Los tallos del cilantro son erectos y delgados. 
    Las hojas de un verde vivo tienen forma de abanico.""",
    "http://i.imgur.com/Wzf5egG.jpg"
)

flora(
    dbpedia['Allium_cepa'],
    "Cebolla",
    "Allium Cepa",
    """Planta bienal cultivada como anual. Hojas semicilíndricas que nacen de un bulbo subterráneo provisto de 
    raíces poco profundas. Tallo erecto que lleva en su extremo una inflorescencia en forma de umbela de flores 
    blancas o rosadas.""",
    "http://i.imgur.com/avBZpBw.jpg"
)

flora(
    dbpedia['Allium_sativum'],
    "Ajo",
    "Allium Sativum",
    """Alcanza entre 30 y 40 cms de altura, sus hojas son macizas, radicales y largas. Sus flores son blancas y 
    rosadas y cada una puede presentar 6 pétalos, 6 estambres y un pistilo. Su raíz es bulbosa, compuesta de 6 a 12 
    bulbillos ("dientes de ajo").""",
    "http://i.imgur.com/bziWfgl.jpg"
)

flora(
    dbpedia['Aloe_Vera'],
    "Sábila",
    "Aloe Vera",
    """Es una planta perenne, con hojas gruesas organizadas en rosetas, alcanza 50 cms de largo y 7 cms de grosor. 
    Las hojas son alargadas y las flores son pequeñas.""",
    "http://i.imgur.com/cTlCh8V.jpg"
)

flora(
    dbpedia['Plukenetia_volubilis'],
    "Sacha Inchi",
    "Plukenetia Volubilis",
    """Es una planta voluble, trepadora y semileñosa, de abundantes hojas y ramas; de una altura aproximada de 2 ms; 
    hojas alternas, acorazonadas; flores pequeñas blanquecinas en racimo; fruto de color marrón al madurar; 
    semillas marrón oscuro con un alto contenido de ácidos grasos insaturados Omega 3, 6 y 9.""",
    "http://i.imgur.com/1pvbezV.jpg"
)

#print(g.serialize(format='pretty-xml'))



