import rdflib
from rdflib import Namespace

def get_devices_of_buildings_query(building):
    return """
    SELECT ?device ?type
    WHERE {
    ?device rdf:type s4blg:Device;
            ex:tipus ?type .

    %s s4blg:contains ?device .
    }
    """ % building

def get_all_type_buildings_query(type):
    return """
    SELECT ?buildingName
    WHERE {
    ?building rdf:type s4blg:Building ;
              ex:tipus "%s" ;
              foaf:name ?buildingName .
    }
    """ % type



def get_all_buildings_query():
    return """
    SELECT ?building
    WHERE {
    ?building rdf:type s4blg:Building .
    }
    """


if __name__ == '__main__':
    g = rdflib.graph.Graph()
    g.parse("linked_data/data.ttl")
    print("ALL BUILDING URI")
    for resp in g.query(get_all_buildings_query()):
        print(resp)
    print()

    print("ALL OFFICE BUILDINGS")
    for resp in g.query(get_all_type_buildings_query("Oficina")):
        print(resp)
    print()

    print("DEVICES AND TYPE OF BUILDING B2")
    for resp in g.query(get_devices_of_buildings_query("ex:b2")):
        print(resp)