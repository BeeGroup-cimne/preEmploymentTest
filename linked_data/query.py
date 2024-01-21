import rdflib


def get_devices_of_buildings_query(building):

    return(f"""
        SELECT ?device ?deviceName
        WHERE {{
            {building} rdf:type s4blg:Building ;
                        s4blg:contains ?device .
            ?device rdf:type s4blg:Device ;
                        ex:tipus ?deviceName .
        }}
    """)


def get_all_type_buildings_query(type):
    return (f"""
        SELECT ?building
        WHERE {{
            ?building rdf:type s4blg:Building;
            ex:tipus "{type}".
        }}
    """)


def get_all_buildings_query():
    return ("""
    SELECT ?building
    WHERE {
        ?building rdf:type s4blg:Building.
    }
    """)

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
