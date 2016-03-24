from urllib import urlopen, quote_plus
from json import loads


#Representa una conexion a Sesame
class Conectar:
    def __init__(self,url):
        self.baseurl=url
        self.sparql_prefix=""
    
    #/**
    # * Permite adicionar un namespace 
    # */
    def addnamespace(self,id,ns):
        self.sparql_prefix+='PREFIX %s:<%s>\n' % (id,ns) 
    

    #/**
    # * Retorna el resultado de una consulta
    # */
    def __getsparql__(self,method):
        #print self.baseurl+method
        data=urlopen(self.baseurl+method).read()
        try:
            result=loads(data)['results']['bindings']
            #result=loads(data)
            return result
        except:
            return data
    
    
    #/**
    # * Permite obtener una lista de los repositorios que existen en el servidor
    # */
    def repositories(self):
        return self.__getsparql__('repositories')
      

    #/**
    # * Define el repositorio que sera usado para guardar o consultar
    # */
    def use_repository(self,r):
        self.repository=r
    
 
    #/**
    # * Permite hacer consultas SPARQL
    # */
    def query(self,q):
        q='repositories/'+self.repository+'?query='+quote_plus(self.sparql_prefix+q)
        return self.__getsparql__(q)
     

    #/**
    # *  Permite realizar aquellas consultas en SPARQL que retornan grafos
    # */
    def construct_query(self,q):
        q='repositories/'+self.repository+'?query='+quote_plus(self.sparql_prefix+q)
        data=urlopen(self.baseurl+q).read()
        return data
    
    
    #/**
    # * Permite guardar tripletas en el servidor
    # */
    def postdata(self,data):
        #/openrdf-sesame/repositories/mem-rdf/statements
        host=baseurl+'/repositories/'+self.repository+'/statements'
        res=urlopen(host,data)
        return res
        
        
#if __name__=='__main__':

#    c=connection('http://localhost:8080/openrdf-sesame/')
#    c.use_repository('maiz')
#    c.addnamespace('WILDLIFE','http://purl.org/ontology/wo/')

    
#    res = c.query("""SELECT ?commonName ?scientificName
#                       WHERE
#                            {?x WILDLIFE:commonName ?commonName.
#                             ?x WILDLIFE:scientificName ?scientificName}""")

    #for r in res:
    #    print r
    #print res