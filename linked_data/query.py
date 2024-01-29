import rdflib


def get_devices_of_buildings_query(building):
    return """
    SELECT ?devices
    WHERE{
    ?uri s4blg:contains ?devices;
    FILTER (?uri=%s)
    }
        """ %(building)


def get_all_type_buildings_query(type):
    return """
    SELECT ?uri
    WHERE{
    ?uri rdf:type s4blg:Building;
        ex:tipus '%s'
    }
    """ %(type)


def get_all_buildings_query():
    return """
    SELECT ?uri
    WHERE{
    ?uri rdf:type s4blg:Building
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
