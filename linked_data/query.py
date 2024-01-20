import rdflib


def get_devices_of_buildings_query(building):
    return f"""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    PREFIX s4blg: <https://saref.etsi.org/saref4bldg/> 
    PREFIX ex: <http://example.org/> 

    SELECT ?device ?deviceType
    WHERE {{
        {building}  rdf:type s4blg:Building;
                    s4blg:contains ?device .
        ?device rdf:type s4blg:Device;
                ex:tipus ?deviceType .
    }}
    """


def get_all_type_buildings_query(type):
    return f"""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    PREFIX s4blg: <https://saref.etsi.org/saref4bldg/> 
    PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
    PREFIX ex: <http://example.org/> 

    SELECT ?building
    WHERE {{
        ?x  rdf:type s4blg:Building;
            ex:tipus "{type}" ;
            foaf:name ?building .
    }}
    """


def get_all_buildings_query():
    return """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    PREFIX s4blg: <https://saref.etsi.org/saref4bldg/> 
    PREFIX foaf: <http://xmlns.com/foaf/0.1/> 

    SELECT ?building
    WHERE {
        ?x  rdf:type s4blg:Building;
            foaf:name ?building .
    }
    """


if __name__ == '__main__':
    g = rdflib.graph.Graph()
    g.parse("linked_data/data.ttl")
    print("ALL BUILDING URI")
    for resp in g.query(get_all_buildings_query()):
        print(resp)

    print("ALL OFFICE BUILDINGS")
    for resp in g.query(get_all_type_buildings_query("Oficina")):
        print(resp)

    print("DEVICES AND TYPE OF BUILDING B3")
    for resp in g.query(get_devices_of_buildings_query("ex:b3")):
        print(resp)
