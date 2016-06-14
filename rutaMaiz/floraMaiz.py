# -*- coding: utf-8 -*-

from rdflib import Namespace
from rdflib import URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from ontologias import WILDLIFE, CRUZAR

dbpedia = Namespace('http://dbpedia.org/resource/')
wikidata = Namespace('http://www.wikidata.org/entity/')
ruta = URIRef('http://190.14.254.237/dataseteco/Maiz/')
floraRuta = URIRef('http://190.14.254.237/dataseteco/Maiz/Flora/')
flora = Graph()

#flora.add( (ruta, RDF.type, CRUZAR['Ruta-turistica']) )
#flora.add( (floraRuta, RDF.type, CRUZAR['Recurso-turistico']) )


flora.add( (dbpedia.Citrus_nobilis, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Citrus_nobilis, WILDLIFE.commonName, Literal('Mandarina')) )
flora.add( (dbpedia.Citrus_nobilis, WILDLIFE.scientificName, Literal('Citrus Nobilis')) )
flora.add( (dbpedia.Citrus_nobilis, WILDLIFE.shortDescription, Literal('El árbol es un frutal espinoso, con ramas delgadas, con las hojas tanto amplias como delgadas. Las flores nacen simples o en grupos en las axilas de las hojas.')) )
flora.add( (dbpedia.Citrus_nobilis, FOAF.depiction, URIRef('http://i.imgur.com/P0rzCMB.jpg')) )

flora.add( (dbpedia['Citrus_sinensis'], RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia['Citrus_sinensis'], WILDLIFE.commonName, Literal('Naranja')) )
flora.add( (dbpedia['Citrus_sinensis'], WILDLIFE.scientificName, Literal('Citrus Sinensis')) )
flora.add( (dbpedia['Citrus_sinensis'], WILDLIFE.shortDescription, Literal('El naranjo es un frutal de hasta 10 m de altura con la copa muy redondeada. Tallos ligeramente espinosos, hojas coriaceas, flores de color blanco muy perfumadas.')) )
flora.add( (dbpedia['Citrus_sinensis'], FOAF.depiction, URIRef('http://i.imgur.com/aKWeHJj.jpg')) )

flora.add( (dbpedia.Citrus_limon, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Citrus_limon, WILDLIFE.commonName, Literal(('Limón'))) )
flora.add( (dbpedia.Citrus_limon, WILDLIFE.scientificName, Literal('Citrus Limon')) )
flora.add( (dbpedia.Citrus_limon, WILDLIFE.shortDescription, Literal('El limonero es un frutal de porte mediano que puede llegar a vivir 70 años. De tronco leñoso, amarillento y muy ramificado, sus grandes y ovaladas hojas de color verde brillante son muy aromáticas al igual que sus flores.')) )
flora.add( (dbpedia.Citrus_limon, FOAF.depiction, URIRef('http://i.imgur.com/JsCNYfk.jpg')) )

flora.add( (dbpedia.Theobroma_cacao, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Theobroma_cacao, WILDLIFE.commonName, Literal(('Cacao'))) )
flora.add( (dbpedia.Theobroma_cacao, WILDLIFE.scientificName, Literal('Theobroma Cacao L.')) )
flora.add( (dbpedia.Theobroma_cacao, WILDLIFE.shortDescription, Literal('Arbusto pequeño de hasta 10 m. Tallo leñoso, recto, con brotes, corteza delgada de color café. Hojas perennes grandes, alternas, colgantes. Flores casi permanentes pequeñas blancas a rosadas, nacen sobre el tallo. El fruto nace en el tronco es una baya grande de hasta 30 x 12 cm.')) )
flora.add( (dbpedia.Theobroma_cacao, FOAF.depiction, URIRef('http://i.imgur.com/CDEeJVu.jpg')) )

flora.add( (dbpedia.Persea_americana, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Persea_americana, WILDLIFE.commonName, Literal(('Aguacate'))))
flora.add( (dbpedia.Persea_americana, WILDLIFE.scientificName, Literal('Persea Americana')) )
flora.add( (dbpedia.Persea_americana, WILDLIFE.shortDescription, Literal('Árbol de unos 10 m de altura. Tallo leñoso. Perennifolio, hojas alternas, pedunculadas, de color verde brillante. Flores perfectas en racimos. Su fruto es una drupa de color verde y piel o cáscara delgada, rico en proteínas y aceite vegetal.')) )
flora.add( (dbpedia.Persea_americana, FOAF.depiction, URIRef('http://i.imgur.com/R3mtPr3.jpg')) )

flora.add( (dbpedia.Passiflora_edulis, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Passiflora_edulis , WILDLIFE.commonName, Literal(('Maracuyá'))) )
flora.add( (dbpedia.Passiflora_edulis, WILDLIFE.scientificName, Literal('Passiflora Edulis')) )
flora.add( (dbpedia.Passiflora_edulis, WILDLIFE.shortDescription, Literal('Planta perenne de hasta 9 m de longitud. Tallos trepadores, leñosos. Hojas alternas, trilobadas, verde oscuras; brotes tiernos rojizos. Flores cremosas con tintes rosa palidos. Frutos comestibles.')) )
flora.add( (dbpedia.Passiflora_edulis, FOAF.depiction, URIRef('http://i.imgur.com/QoGoZpf.jpg')) )

flora.add( (dbpedia.Musa_paradisiaca, RDF.type, WILDLIFE.TaxonName) )
flora.add((dbpedia.Musa_paradisiaca, WILDLIFE.commonName, Literal(('Plátano'))))
flora.add( (dbpedia.Musa_paradisiaca, WILDLIFE.scientificName, Literal('Musa × Paradisiaca L.')) )
flora.add( (dbpedia.Musa_paradisiaca, WILDLIFE.shortDescription, Literal('Planta con el tallo bien desarrollado. Hojas grandes, oblongas, lámina con la vena media bien desarrollada y numerosas venas paralelas, perpendiculares a la vena media.')) )
flora.add( (dbpedia.Musa_paradisiaca, FOAF.depiction, URIRef('http://i.imgur.com/3bfoEk5.jpg')) )

flora.add( (dbpedia.Saccharum_officinarum_L, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Saccharum_officinarum_L, WILDLIFE.commonName, Literal(('Caña de azúcar'))) )
flora.add( (dbpedia.Saccharum_officinarum_L, WILDLIFE.scientificName, Literal('Saccharum Officinarum L.')) )
flora.add( (dbpedia.Saccharum_officinarum_L, WILDLIFE.shortDescription, Literal('Es una planta perenne con un tallo macizo, de hasta 6 m de altura y 2 a 8 cm de diametro; aparece por lo general deshojado en la parte inferior, está lleno de un tejido esponjoso y dulce del que se extrae el azúcar. Sus hojas son largas y puntiagudas.')) )
flora.add( (dbpedia.Saccharum_officinarum_L, FOAF.depiction, URIRef('http://i.imgur.com/7K7gpog.jpg')) )

flora.add( (dbpedia.Gynerium_sagittatum, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Gynerium_sagittatum, WILDLIFE.commonName, Literal(('Caña Brava'))) )
flora.add( (dbpedia.Gynerium_sagittatum, WILDLIFE.scientificName, Literal('Gynerium Sagittatum')) )
flora.add( (dbpedia.Gynerium_sagittatum, WILDLIFE.shortDescription, Literal('Es una planta silvestre de hasta 4 m de alto. Posee tallos gruesos, sólidos y muy resistentes que le han permitido sobrevivir al tiempo. Las hojas son lineales y aserradas, dispuestas en dos filas.')) )
flora.add( (dbpedia.Gynerium_sagittatum, FOAF.depiction, URIRef('http://i.imgur.com/R9UjZNK.jpg')) )

flora.add( (dbpedia.Zea_Mays, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Zea_Mays, WILDLIFE.commonName, Literal(('Maíz'))))
flora.add( (dbpedia.Zea_Mays, WILDLIFE.scientificName, Literal('Zea Mays')) )
flora.add( (dbpedia.Zea_Mays, WILDLIFE.shortDescription, Literal('Planta herbáceae que puede alcanzar hasta los 2,5 m de altura. El tallo internamente tiene una médula de tejido esponjoso y blanco donde almacena reservas alimenticias, en especial azúcares. Las hojas son alargadas arrolladas al tallo, del cual nacen las espigas o mazorcas.')) )
flora.add( (dbpedia.Zea_Mays, FOAF.depiction, URIRef('http://i.imgur.com/6Ywbfgs.jpg')) )

flora.add( (dbpedia.Heliconia_bihai, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Heliconia_bihai, WILDLIFE.commonName, Literal(('Heliconia'))))
flora.add( (dbpedia.Heliconia_bihai, WILDLIFE.scientificName, Literal('Heliconia Bihai')) )
flora.add( (dbpedia.Heliconia_bihai, WILDLIFE.shortDescription, Literal('Es una planta muy llamativa por la inflorescencia que tiene en forma de espiga caracterizada por una serie de espatas de color rojo-verde y amarillo. Puede llegar a alcanzar ente los 4 y 6 m de altura y las hojas que tiene tienen forma de abanico.')) )
flora.add( (dbpedia.Heliconia_bihai, FOAF.depiction, URIRef('http://i.imgur.com/wZ0GLbc.jpg')) )

flora.add( (dbpedia.Cassava, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Cassava, WILDLIFE.commonName, Literal(('Yuca'))) )
flora.add( (dbpedia.Cassava, WILDLIFE.scientificName, Literal('Manihot Sculenta')) )
flora.add( (dbpedia.Cassava, WILDLIFE.shortDescription, Literal('Es un arbusto perenne, que alcanza los dos metros de altura. Su raíz es cilíndrica y oblonga, y alcanza el metro de largo y los 10 cm de diámetro. La cáscara es dura e incomestible. La pulpa es muy rica en hidratos de carbono y azúcares.')) )
flora.add( (dbpedia.Cassava, FOAF.depiction, URIRef('http://i.imgur.com/VYm4XpF.jpg')) )

flora.add( (dbpedia.Carica_papaya, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Carica_papaya, WILDLIFE.commonName, Literal(('Papaya'))) )
flora.add( (dbpedia.Carica_papaya, WILDLIFE.scientificName, Literal('Carica Papaya')) )
flora.add( (dbpedia.Carica_papaya, WILDLIFE.shortDescription, Literal('Planta herbácea, de hasta 8m de altura; con látex lechoso. Tallos cilindrico, simple, sin ramificar, termina en un penacho de hojas, de hasta 30 cm de diámetro. Flor de color amarillo, pétalos y sépalos del mismo color, blanco amarilloso, nacen en el extremo del tallo, debajo de las hojas.')) )
flora.add( (dbpedia.Carica_papaya, FOAF.depiction, URIRef('http://i.imgur.com/oAa8tSA.jpg')) )

flora.add( (dbpedia.Solanum_pimpinellifolium, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Solanum_pimpinellifolium, WILDLIFE.commonName, Literal(('Tomate Cherri'))) )
flora.add( (dbpedia.Solanum_pimpinellifolium, WILDLIFE.scientificName, Literal('Lycopersicum Pimpinellifolium')) )
flora.add( (dbpedia.Solanum_pimpinellifolium, WILDLIFE.shortDescription, Literal('Planta anual de porte porte arbustivo o rastrero. Las hojas son sencillas, pecioladas y de limbo hendido. Toda la parte verde de la planta está compuesta por pelos glandulares que al rozarse emite un líquido con olor característico. Las flores aparecen en racimos siendo el número de estas variables.')) )
flora.add( (dbpedia.Solanum_pimpinellifolium, FOAF.depiction, URIRef('http://i.imgur.com/viCbqpn.jpg')) )

flora.add( (dbpedia.Ananas_comosus, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Ananas_comosus, WILDLIFE.commonName, Literal(('Piña'))) )
flora.add( (dbpedia.Ananas_comosus, WILDLIFE.scientificName, Literal('Ananas Comosus')) )
flora.add( (dbpedia.Ananas_comosus, WILDLIFE.shortDescription, Literal('Planta perenne terrestre, con forma de roseta abierta que produce uno de los frutos tropicales más consumidos. Hojas en forma de espadas con diminutas y afiladas espinas en sus bordes.')) )
flora.add( (dbpedia.Ananas_comosus, FOAF.depiction, URIRef('http://i.imgur.com/yvXykAn.jpg')) )

flora.add( (dbpedia.Psidium_guajava, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Psidium_guajava, WILDLIFE.commonName, Literal(('Guayaba'))) )
flora.add( (dbpedia.Psidium_guajava, WILDLIFE.scientificName, Literal('Psidium Guajava')) )
flora.add( (dbpedia.Psidium_guajava, WILDLIFE.shortDescription, Literal('Arbolito de follaje persistente que puede alcanzar 4-6 m de altura, con el tronco corto y algo tortuoso. Hojas opuestas de 5-10 cm de longitud. Flores blancas, solitarias o en pequeños grupos, que aparecen en las axilas de las hojas. Fruto en baya redondeada con el cáliz de la flor persistiendo.')) )
flora.add( (dbpedia.Psidium_guajava, FOAF.depiction, URIRef('http://i.imgur.com/e55G5DZ.jpg')) )

flora.add( (dbpedia.Handroanthus_guayacan, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Handroanthus_guayacan, WILDLIFE.commonName, Literal(('Guayacán'))))
flora.add( (dbpedia.Handroanthus_guayacan, WILDLIFE.scientificName, Literal('Tabebuia guayacan (Seem.) Hemsl.')) )
flora.add( (dbpedia.Handroanthus_guayacan, WILDLIFE.shortDescription, Literal('Es un árbol grande de hasta 40 m de alto y 100 cm de diámetro con tronco recto, cilíndrico y raramente irregular cuya base es ligeramente alargada. Produce una madera muy pesada y resistente a la pudrición.')) )
flora.add( (dbpedia.Handroanthus_guayacan, FOAF.depiction, URIRef('http://i.imgur.com/9CmiV7U.jpg')) )

flora.add( (dbpedia.Ceiba_pentandra, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Ceiba_pentandra, WILDLIFE.commonName, Literal(('Ceiba'))) )
flora.add( (dbpedia.Ceiba_pentandra, WILDLIFE.scientificName, Literal('Ceiba Pentandra (L.) Gaertn')) )
flora.add( (dbpedia.Ceiba_pentandra, WILDLIFE.shortDescription, Literal('Árbol de 50 m de altura, tallo de 2 m de diámetro, abombado, corteza gris clara y anillada, copa semihemisférica, follaje denso verde oscuro. Hojas compuestas y alternas, flores blancas.')) )
flora.add( (dbpedia.Ceiba_pentandra, FOAF.depiction, URIRef('http://i.imgur.com/V9Rfjpq.jpg')) )

flora.add( (dbpedia.Cassia_fistula, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Cassia_fistula, WILDLIFE.commonName, Literal(('Ébano Falso'))) )
flora.add( (dbpedia.Cassia_fistula, WILDLIFE.scientificName, Literal('Cassia Fistula')) )
flora.add( (dbpedia.Cassia_fistula, WILDLIFE.shortDescription, Literal('Arbol de 10-15 m de alto; ramas de tendencia ascendente. Hojas grandes, caducas, ovadas, acuminadas y péndulas. Flores dispuestas en grandes racimos pendulares, muy vistosas de color amarillo.')) )
flora.add( (dbpedia.Cassia_fistula, FOAF.depiction, URIRef('http://i.imgur.com/aUZVMJ4.jpg')) )

flora.add( (dbpedia.Guadua, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Guadua, WILDLIFE.commonName, Literal(('Guadua'))) )
flora.add( (dbpedia.Guadua, WILDLIFE.scientificName, Literal('Guadua Angustifolia')) )
flora.add( (dbpedia.Guadua, WILDLIFE.shortDescription, Literal('La raíz es un rizoma que almacena los nutrimentos, estos rizomas producen raicillas adventicias, el tallo de forma cilíndrica y con nudos, ramas solitarias y muy espinosas en los nudos basales y con presencia o no de hojas, hojas lanceoladas verdes lustrosas.')) )
flora.add( (dbpedia.Guadua, FOAF.depiction, URIRef('http://i.imgur.com/WLLO9uD.jpg')) )

flora.add( (dbpedia.Narcissus_primigenius, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Narcissus_primigenius, WILDLIFE.commonName, Literal(('Narciso'))) )
flora.add( (dbpedia.Narcissus_primigenius, WILDLIFE.scientificName, Literal('Narcissus Pseudonarcissus')) )
flora.add( (dbpedia.Narcissus_primigenius, WILDLIFE.shortDescription, Literal('Es una planta de hojas estrechas y alargadas. Sus flores de color blancas, amarillas, rosa y de formas simples. La floración se produce en primavera. El fruto es una cápsula.')) )
flora.add( (dbpedia.Narcissus_primigenius, FOAF.depiction, URIRef('http://i.imgur.com/GcRveZA.jpg')) )

flora.add( (dbpedia.Pelargonium_zonale, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Pelargonium_zonale, WILDLIFE.commonName, Literal(('Geranio'))) )
flora.add( (dbpedia.Pelargonium_zonale, WILDLIFE.scientificName, Literal('Pelargonium Zonale')) )
flora.add( (dbpedia.Pelargonium_zonale, WILDLIFE.shortDescription, Literal('Hojas en forma generalmente acorazonada y de tonalidades de verde diferentes, de floración prolongada, las flores se encuentran agrupadas de formas diversas y el colorido es muy variado, desde el blanco al rojo pasando por el rosado.')) )
flora.add( (dbpedia.Pelargonium_zonale, FOAF.depiction, URIRef('http://i.imgur.com/RssuVMe.jpg')) )

flora.add( (dbpedia.Viola_odorata, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Viola_odorata, WILDLIFE.commonName, Literal(('Violeta'))) )
flora.add( (dbpedia.Viola_odorata, WILDLIFE.scientificName, Literal('Viola Odorata')) )
flora.add( (dbpedia.Viola_odorata, WILDLIFE.shortDescription, Literal('Planta perenne rizomatosa que se expande mediante estalones y puede formar una buena cubierta de suelo, sus hojas son radicales ligeramente festoneadas y acorazonadas en la base. Las flores son muy perfumadas; el fruto es una capsula que se abre en la madurez, su es color violeta y blanco.')) )
flora.add( (dbpedia.Viola_odorata, FOAF.depiction, URIRef('http://i.imgur.com/rKrLqRo.jpg')) )

flora.add( (dbpedia.Camellia_japonica, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Camellia_japonica, WILDLIFE.commonName, Literal(('Camelia'))) )
flora.add( (dbpedia.Camellia_japonica, WILDLIFE.scientificName, Literal('Camellia Japonica')) )
flora.add( (dbpedia.Camellia_japonica, WILDLIFE.shortDescription, Literal('Arbusto ramificado de 2 metros de altura, hojas anchas elípticas con filo aserrado, haz de color verde oscuro reluciente y el envés más pálido y coriáceo. Se adapta perfectamente a su cultivo en jardinera. Flores solitarias de color variado rojo sangre, cereza, con rayas blancas o rosadas.')) )
flora.add( (dbpedia.Camellia_japonica, FOAF.depiction, URIRef('http://i.imgur.com/VUACRGI.jpg')) )

flora.add( (dbpedia.Leucanthemum_vulgare, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Leucanthemum_vulgare, WILDLIFE.commonName, Literal(('Margarita común'))))
flora.add( (dbpedia.Leucanthemum_vulgare, WILDLIFE.scientificName, Literal('Chrysanthemun Leucanthemum')) )
flora.add( (dbpedia.Leucanthemum_vulgare, WILDLIFE.shortDescription, Literal('Es una planta herbácea con hojas hendidas. Las flores están siempre reunidas en una inflorescencia llamada cabezuela o capítulo, que parece una única flor y funciona como tal.')) )
flora.add( (dbpedia.Leucanthemum_vulgare, FOAF.depiction, URIRef('http://i.imgur.com/A1j5930.jpg')) )

flora.add( (wikidata.Q130918, RDF.type, WILDLIFE.TaxonName) )
flora.add( (wikidata.Q130918, WILDLIFE.commonName, Literal(('Dalia'))) )
flora.add( (wikidata.Q130918, WILDLIFE.scientificName, Literal('Dahlia spp.')) )
flora.add( (wikidata.Q130918, WILDLIFE.shortDescription, Literal('Planta herbácea o arbustiva anual, raiz tuberosa, hojas opuestas o verticiladas. Flores dispuestas en inflorescencias compuestas o capítulo (rodeada por brácteas), de diferentes colores. Hay 30 especies y 20000 variedades.')) )
flora.add( (wikidata.Q130918, FOAF.depiction, URIRef('http://i.imgur.com/Th4Plgi.jpg')) )

flora.add( (dbpedia.Iris_germanica, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Iris_germanica, WILDLIFE.commonName, Literal(('Lirio común'))) )
flora.add( (dbpedia.Iris_germanica, WILDLIFE.scientificName, Literal('Iris germánica')) )
flora.add( (dbpedia.Iris_germanica, WILDLIFE.shortDescription, Literal('Tallo terminal con hojas en la base, herbácea perenne de rizoma vistoso y grueso. Hojas acintadas, erguidas, de borde liso, color verde oscuro a grisáceo, de 35 a 45 cm largo. Flores de poca duración.')) )
flora.add( (dbpedia.Iris_germanica, FOAF.depiction, URIRef('http://i.imgur.com/NDTPe0l.jpg')) )

flora.add( (dbpedia.Hydrangea_macrophylla, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Hydrangea_macrophylla, WILDLIFE.commonName, Literal(('Hortensia'))) )
flora.add( (dbpedia.Hydrangea_macrophylla, WILDLIFE.scientificName, Literal('Hydrangea Macrophylla')) )
flora.add( (dbpedia.Hydrangea_macrophylla, WILDLIFE.shortDescription, Literal('Planta semiarbustiva, caducifolia, puede llegar a medir 1,5 m. Tallos ramosos, gruesos, derechos, terminados por las flores agrupadas. Hojas grandes, verdes, opuestas, ovaladas con borde dentado.')) )
flora.add( (dbpedia.Hydrangea_macrophylla, FOAF.depiction, URIRef('http://i.imgur.com/VLAuVL6.jpg')) )

flora.add( (dbpedia.Papaver_rhoeas, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Papaver_rhoeas, WILDLIFE.commonName, Literal(('Amapola'))) )
flora.add( (dbpedia.Papaver_rhoeas, WILDLIFE.scientificName, Literal('Papaver rhoeas')) )
flora.add( (dbpedia.Papaver_rhoeas, WILDLIFE.shortDescription, Literal('Hierba anual, cubierta de pelos perpendiculares. Hojas simples en la base, alargadas y lobuladas. flores solitarias con pétalos arrugados en botones florales, mostrando al abrirse un bello color rojo intenso, por lo general presentan una mancha negruzca en la porción basal. El fruto de la amapola es una cápsula, llena de semillas.')) )
flora.add( (dbpedia.Papaver_rhoeas, FOAF.depiction, URIRef('http://i.imgur.com/9RgVwBE.jpg')) )

flora.add( (dbpedia.Murraya_paniculata, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Murraya_paniculata, WILDLIFE.commonName, Literal(('Jazmín Naranja'))))
flora.add( (dbpedia.Murraya_paniculata, WILDLIFE.scientificName, Literal('Murraya Paniculata')) )
flora.add( (dbpedia.Murraya_paniculata, WILDLIFE.shortDescription, Literal('Planta con hojas compuestas, alternas, imparipinnadas; los foliolos de 1 a 4 cm de largo, verdes muy oscuros y brillantes. Las flores blancas, pequeñas y fragantes.')) )
flora.add( (dbpedia.Murraya_paniculata, FOAF.depiction, URIRef('http://i.imgur.com/6PuZR2z.jpg')) )

flora.add( (wikidata.Q843363, RDF.type, WILDLIFE.TaxonName) )
flora.add( (wikidata.Q843363, WILDLIFE.commonName, Literal(('Begonia'))) )
flora.add( (wikidata.Q843363, WILDLIFE.scientificName, Literal('Begonia Semperflorens')) )
flora.add( (wikidata.Q843363, WILDLIFE.shortDescription, Literal('Herbácea perenne o anual, altura aproximada entre 20-40 cm. Tallo carnoso y ramificado, hojas ovales y redondeadas con coloraciones rojizas en múltiples tonalidades. Las flores reunidas en cimas exilares de color rosa, rojo, blanco.')) )
flora.add( (wikidata.Q843363, FOAF.depiction, URIRef('http://i.imgur.com/9Pn2uWH.jpg')) )

flora.add( (dbpedia.Viola_x_wittrockiana, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Viola_x_wittrockiana, WILDLIFE.commonName, Literal(('Pensamientos'))) )
flora.add( (dbpedia.Viola_x_wittrockiana, WILDLIFE.scientificName, Literal('Viola x wittrockiana')) )
flora.add( (dbpedia.Viola_x_wittrockiana, WILDLIFE.shortDescription, Literal('Son plantas híbridas, cuyo ciclo de vida es de un año, y que son cultivadas por sus vistosas flores. Tienen hojas simples con forma de corazón y margen dentado de cinco pétalos aterciopelados, y con diversas gamas de colores. Su floración abarca los meses otoñales, pero continua hasta la entrada de la primavera.')) )
flora.add( (dbpedia.Viola_x_wittrockiana, FOAF.depiction, URIRef('http://i.imgur.com/u8YKOy7.jpg')) )

flora.add( (wikidata.Q93201, RDF.type, WILDLIFE.TaxonName) )
flora.add( (wikidata.Q93201, WILDLIFE.commonName, Literal(('Tulipán'))) )
flora.add( (wikidata.Q93201, WILDLIFE.scientificName, Literal('Tulipa spp')) )
flora.add( (wikidata.Q93201, WILDLIFE.shortDescription, Literal('Hierbas perennes con bulbos o rizomas. Las hojas son alternas y espiraladas, se disponen a lo largo del tallo o en una roseta basal. Flores erguidas, muy llamativas, de numerosos colores, tardan hasta tres semanas en marchitarse. El fruto es una cápsula, ocasionalmente una baya. Las semillas son planas y con forma de disco o globosas.')) )
flora.add( (wikidata.Q93201, FOAF.depiction, URIRef('http://i.imgur.com/JmDuDLg.gif')) )

flora.add( (dbpedia.Chrysanthemum_morifolium, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Chrysanthemum_morifolium, WILDLIFE.commonName, Literal(('Crisantemo'))) )
flora.add( (dbpedia.Chrysanthemum_morifolium, WILDLIFE.scientificName, Literal('Chrysanthemum Morifolium')) )
flora.add( (dbpedia.Chrysanthemum_morifolium, WILDLIFE.shortDescription, Literal('Planta de tallo herbáceo y delgado, con hojas alternas suaves al tacto, palmeado, divididas, con bordes dentados, nervaduras principal y secundarias, a la cabeza floral se le denomina capítulo.')) )
flora.add( (dbpedia.Chrysanthemum_morifolium, FOAF.depiction, URIRef('http://i.imgur.com/w4aGjbg.jpg')) )

flora.add( (dbpedia.Magnolia_grandiflora, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Magnolia_grandiflora, WILDLIFE.commonName, Literal(('Magnolia'))) )
flora.add( (dbpedia.Magnolia_grandiflora, WILDLIFE.scientificName, Literal('Magnolia Grandiflora L.')) )
flora.add( (dbpedia.Magnolia_grandiflora, WILDLIFE.shortDescription, Literal('Es un árbol de tamaño medio a grande de 20-30 m de altura. Las hojas son perennes, simples o ampliamente ovadas de 12-20 cm de longitud y 6-12 cm de ancho con los márgenes dentados, son de color verde oscuro y textura coriácea que se vuelven color marrón cuando llega el invierno.')) )
flora.add( (dbpedia.Magnolia_grandiflora, FOAF.depiction, URIRef('http://i.imgur.com/p3tLqzX.jpg')) )

flora.add( (dbpedia.Cattleya_trianae, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Cattleya_trianae, WILDLIFE.commonName, Literal(('Flor de mayo'))) )
flora.add( (dbpedia.Cattleya_trianae, WILDLIFE.scientificName, Literal('Cattleya Trianae')) )
flora.add( (dbpedia.Cattleya_trianae, WILDLIFE.shortDescription, Literal('Planta epífita, con pseudobulbos de largo variable que llevan a su extremidad una o a dos hojas sin pecíolo. Flores vistosas que se desarrollan en el tallo.')) )
flora.add( (dbpedia.Cattleya_trianae, FOAF.depiction, URIRef('http://i.imgur.com/A4H9iz7.jpg')) )

flora.add( (wikidata.Q959222, RDF.type, WILDLIFE.TaxonName) )
flora.add( (wikidata.Q959222, WILDLIFE.commonName, Literal(('Pasto estrella'))) )
flora.add( (wikidata.Q959222, WILDLIFE.scientificName, Literal('Cynodon Plectostachium')) )
flora.add( (wikidata.Q959222, WILDLIFE.shortDescription, Literal('Es una gramínea perenne, de vida larga, frondosa y rastrera, produce estolones de rápido crecimiento, con largos entrenudos y sus tallos pueden alcanzar hasta 3 m de longitud. Posee hojas exuberantes con vellos en forma de lanza. La inflorescencia presenta de 2 a 5 espiguillas solitarias de 2 a 3 mm.')) )
flora.add( (wikidata.Q959222, FOAF.depiction, URIRef('http://i.imgur.com/biYwa69.jpg')) )

flora.add( (dbpedia.Coffea_arabica, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Coffea_arabica, WILDLIFE.commonName, Literal(('Café'))) )
flora.add( (dbpedia.Coffea_arabica, WILDLIFE.scientificName, Literal('Caffea Arabica')) )
flora.add( (dbpedia.Coffea_arabica, WILDLIFE.shortDescription, Literal('El cafeto es un arbusto o árbol pequeño, perennifolio, de fuste recto que puede alcanzar los 10 m en estado silvestre.')) )
flora.add( (dbpedia.Coffea_arabica, FOAF.depiction, URIRef('http://i.imgur.com/H2ZM3sf.jpg')) )

flora.add( (dbpedia.Mangifera_indica, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Mangifera_indica, WILDLIFE.commonName, Literal(('Mango'))) )
flora.add( (dbpedia.Mangifera_indica, WILDLIFE.scientificName, Literal('Mangifera Indica')) )
flora.add( (dbpedia.Mangifera_indica, WILDLIFE.shortDescription, Literal('El mango típico constituye un árbol de tamaño mediano, de 10-30 m de altura. El tronco es más o menos recto, cilíndrico y de 75-100 cm de diámetro, cuya corteza de color gris - café tiene grietas.')) )
flora.add( (dbpedia.Mangifera_indica, FOAF.depiction, URIRef('http://i.imgur.com/GtxlZkC.jpg')) )

flora.add( (dbpedia.Allium_fistulosum, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Allium_fistulosum, WILDLIFE.commonName, Literal(('Cebolla larga'))) )
flora.add( (dbpedia.Allium_fistulosum, WILDLIFE.scientificName, Literal('Allium Fistulosum')) )
flora.add( (dbpedia.Allium_fistulosum, WILDLIFE.shortDescription, Literal('Las raíces se producen en la base del tallo, son fasciculadas y poco abundantes. Cada hoja tiene una base larga y carnosa, que se une estrechamente con la base de las demás hojas. Las hojas son tubulares de 25-35 cm de largo y 5-7 mm de diámetro. El tallo es un disco comprimido, de donde parten las raíces y la base de las hojas.')) )
flora.add( (dbpedia.Allium_fistulosum, FOAF.depiction, URIRef('http://i.imgur.com/u1nPyiR.jpg')) )

flora.add( (dbpedia['Capsicum_annuum_var._minimum'], RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia['Capsicum_annuum_var._minimum'], WILDLIFE.commonName, Literal(('Ají'))) )
flora.add( (dbpedia['Capsicum_annuum_var._minimum'], WILDLIFE.scientificName, Literal('Capsicum Annuum')) )
flora.add( (dbpedia['Capsicum_annuum_var._minimum'], WILDLIFE.shortDescription, Literal('Planta anual, que puede alcanzar hasta 1 m de altura, de tallos empinados y ramosos, con las hojas aovadas y lanceoladas de bordes enteros o apenas sinuados en la base. Es especialmente productiva en zonas cálidas y climas secos. Es una planta de huerta y de diversas variedades.')) )
flora.add( (dbpedia['Capsicum_annuum_var._minimum'], FOAF.depiction, URIRef('http://i.imgur.com/EBqG6Ox.jpg')) )

flora.add( (dbpedia.Urtica_dioica, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Urtica_dioica, WILDLIFE.commonName, Literal(('Ortiga'))) )
flora.add( (dbpedia.Urtica_dioica, WILDLIFE.scientificName, Literal('Urtica Dioica')) )
flora.add( (dbpedia.Urtica_dioica, WILDLIFE.shortDescription, Literal('Es una planta arbustiva perenne que puede alcanzar hasta 1,5m de altura. Tallos erectos cuadrangulares, hojas verdes aserradas, puntiagudas, provistas al igual que el tallo de pelos urticantes. Flores en forma de raices, con flores unisexuales. Posee unos pelos urticantes que tienen la forma de pequeñisimas ampollas.')) )
flora.add( (dbpedia.Urtica_dioica, FOAF.depiction, URIRef('http://i.imgur.com/oVjUyH1.jpg')) )

flora.add( (dbpedia.Rosmarinus_officinalis, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Rosmarinus_officinalis, WILDLIFE.commonName, Literal(('Romero'))) )
flora.add( (dbpedia.Rosmarinus_officinalis, WILDLIFE.scientificName, Literal('Rosmarinus Officinalis')) )
flora.add( (dbpedia.Rosmarinus_officinalis, WILDLIFE.shortDescription, Literal('Arbusto perenne, verde, leñoso y muy aromático de hasta 2 m de altura que crece espontáneamente o en cultivo. Sus tallos ramificados con hojas rígidas, lineales, lanceoladas, en forma de aguja y de aspecto coriáceas las recubre una capa de diminutos pelos.')) )
flora.add( (dbpedia.Rosmarinus_officinalis, FOAF.depiction, URIRef('http://i.imgur.com/umcF7Ne.jpg')) )

flora.add( (dbpedia.Coriandrum_sativum, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Coriandrum_sativum, WILDLIFE.commonName, Literal(('Cilantro'))) )
flora.add( (dbpedia.Coriandrum_sativum, WILDLIFE.scientificName, Literal('Coriandrum Sativum')) )
flora.add( (dbpedia.Coriandrum_sativum, WILDLIFE.shortDescription, Literal('Es una hierba anual de hasta 60 cm, sin pelos y brillante. Los tallos del cilantro son erectos y delgados. Las hojas de un verde vivo tienen forma de abanico.')) )
flora.add( (dbpedia.Coriandrum_sativum, FOAF.depiction, URIRef('http://i.imgur.com/Wzf5egG.jpg')) )

flora.add( (dbpedia.Allium_cepa, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Allium_cepa, WILDLIFE.commonName, Literal(('Cebolla'))) )
flora.add( (dbpedia.Allium_cepa, WILDLIFE.scientificName, Literal('Allium Cepa')) )
flora.add( (dbpedia.Allium_cepa, WILDLIFE.shortDescription, Literal('Planta bienal cultivada como anual. Hojas semicilindricas que nacen de un bulbo subterráneo provisto de raices poco profundas. Tallo erecto que lleva en su extremo una inflorescencia en forma de umbela de flores blancas o rosadas.')) )
flora.add( (dbpedia.Allium_cepa, FOAF.depiction, URIRef('http://i.imgur.com/avBZpBw.jpg')) )

flora.add( (dbpedia.Allium_sativum, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Allium_sativum, WILDLIFE.commonName, Literal(('Ajo'))) )
flora.add( (dbpedia.Allium_sativum, WILDLIFE.scientificName, Literal('Allium Sativum')) )
flora.add( (dbpedia.Allium_sativum, WILDLIFE.shortDescription, Literal('Alcanza entre 30 y 40 cm de altura, sus hojas son macizas, radicales y largas. Sus flores son blancas y rosadas y cada una puede presentar 6 pétalos, 6 estambres y un pistilo. Su raíz es bulbosa, compuesta de 6 a 12 bulbillos ("dientes de ajo").')) )
flora.add( (dbpedia.Allium_sativum, FOAF.depiction, URIRef('http://i.imgur.com/bziWfgl.jpg')) )

flora.add( (dbpedia.Aloe_Vera, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Aloe_Vera, WILDLIFE.commonName, Literal(('Sábila'))) )
flora.add( (dbpedia.Aloe_Vera, WILDLIFE.scientificName, Literal('Aloe Vera')) )
flora.add( (dbpedia.Aloe_Vera, WILDLIFE.shortDescription, Literal('Es una planta perenne, con hojas gruesas organizadas en rosetas, alcanzan 50 cm de largo y los 7 de grosor. Las hojas son alargadas y las flores son pequeñas.')) )
flora.add( (dbpedia.Aloe_Vera, FOAF.depiction, URIRef('http://i.imgur.com/cTlCh8V.jpg')) )

flora.add( (dbpedia.Plukenetia_volubilis, RDF.type, WILDLIFE.TaxonName) )
flora.add( (dbpedia.Plukenetia_volubilis, WILDLIFE.commonName, Literal(('Sacha Inchi'))) )
flora.add( (dbpedia.Plukenetia_volubilis, WILDLIFE.scientificName, Literal('Plukenetia Volubilis')) )
flora.add( (dbpedia.Plukenetia_volubilis, WILDLIFE.shortDescription, Literal('Es una planta voluble, trepadora y semileñosa, de abundantes hojas y ramas; de una altura aproximada de 2 m; hojas alternas, acorazonadas; flores pequeñas blanquecinas en racimo; fruto de color marrón al madurar; semillas marrón oscuro con un alto contenido de ácidos grasos insaturados Omega 3, 6 y 9.')) )
flora.add( (dbpedia.Plukenetia_volubilis, FOAF.depiction, URIRef('http://i.imgur.com/1pvbezV.jpg')) )


print(flora.serialize(format='pretty-xml'))



