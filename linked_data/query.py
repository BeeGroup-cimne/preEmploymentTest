from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery

s4blg = Namespace("https://saref.etsi.org/saref4bldg/")
foaf = Namespace("http://xmlns.com/foaf/0.1/")
ex = Namespace("http://example.org/")


def get_devices_of_buildings_query(building):
    
    return prepareQuery("""
            SELECT ?device ?type
            WHERE {{
                    {0} s4blg:contains ?device .
                    ?device rdf:type s4blg:Device ;
                        ex:tipus ?type .
                }}""".format(building), initNs={"ex": ex, "s4blg": s4blg})
                        

def get_all_type_buildings_query(type):
    
    return prepareQuery("""
            SELECT ?type ?name
            WHERE {{
                ?building rdf:type s4blg:Building;
                        ex:tipus ?type ;
                        foaf:name ?name .
                FILTER(?type = "{0}")
            }}
            """.format(type), initNs={"foaf": foaf, "ex": ex, "s4blg": s4blg})



def get_all_buildings_query():

    return prepareQuery("""
            SELECT ?uri
            WHERE {
                ?uri rdf:type s4blg:Building .
            }
            """, initNs={"s4blg": s4blg})


    #prepareQuery("""
    #PREFIX s4blg: <https://saref.etsi.org/saref4bldg/>
    #PREFIX foaf: <http://xmlns.com/foaf/0.1/>

    #   QUERY
    #""")



if __name__ == '__main__':
    g = Graph()
    g.parse("linked_data/data.ttl")

    print("ALL BUILDING URI")
    for resp in g.query(get_all_buildings_query()):
        print(resp)

    print("ALL OFFICE BUILDINGS")
    for resp in g.query(get_all_type_buildings_query("Oficina")):
        print(resp)

    print("DEVICES AND TYPE OF BUILDING B2")
    for resp in g.query(get_devices_of_buildings_query("ex:b2")):   #modified
        print(resp)
