import rdflib


def get_devices_of_buildings_query(building):
    return f"""
    SELECT ?device ?deviceType
        WHERE {{
        {building} s4blg:contains ?device.
        ?device rdf:type s4blg:Device ;
                ex:tipus ?deviceType.
        }}
    """


def get_all_type_buildings_query(type):
    return f"""
    SELECT ?building ?buildingName ?buildingType
    WHERE {{
        ?building rdf:type s4blg:Building ;
            foaf:name ?buildingName ;
            ex:tipus ?buildingType.
    FILTER (?buildingType = "{type}")
    }}
    """


def get_all_buildings_query():
    return """
    SELECT ?building ?buildingName
    WHERE {
        ?building rdf:type s4blg:Building ;
        foaf:name ?buildingName.
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
