import rdflib


def get_devices_of_buildings_query(building):
    return """
    PREFIX ex: <http://example.org/>
    PREFIX s4blg: <https://saref.etsi.org/saref4bldg/>
    SELECT ?device
    WHERE {
        """ + building + """ s4blg:contains ?device .
    }
    """


def get_all_type_buildings_query(type):
    return f"""
    PREFIX ex: <http://example.org/>
    PREFIX s4blg: <https://saref.etsi.org/saref4bldg/>
    SELECT ?building
    WHERE {{
        ?building rdf:type s4blg:Building ;
                  ex:tipus "{type}" .
    }}
    """


def get_all_buildings_query():
    return """
    PREFIX s4blg: <https://saref.etsi.org/saref4bldg/>
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

    print("ALL OFFICE BUILDINGS")
    for resp in g.query(get_all_type_buildings_query("Oficina")):
        print(resp)

    print("DEVICES AND TYPE OF BUILDING B2")
    for resp in g.query(get_devices_of_buildings_query("ex:b3")):
        print(resp)
