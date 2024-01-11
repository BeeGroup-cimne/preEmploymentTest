# PRE-EMPLOYMENT TEST
To participate in this test, fork the project and solve the different problems. Upload the 
solution in a pull request to this project.

### Problem 1: Architecture (discussion)
In a project, we need to gather electricity consumption and weather data time series  continuously from some very slow api,
and store them in a database. The data we are gathering at certain points can be more than the data 
that can be processed by the system. 

Also, the api is very slow and the process to gather it has to be parallelized.

Propose an architecture to be able to gather and store this data. Propose the different protocols, databases to use,
technologies, etc).


### Problem 2: Data management
In the data_management folder you will find an [Excel file](data_management/data_2019.xls) containing data 
for 1 year of electricity consumption collected by billing information.

We need to transform this data, by creating a time-series with regular daily frequency. If gaps are detected,
they must appear as NaN values. You can use any
python library like pandas to transform this data.

### Problem 3: Linked data

Linked Data is a set of design principles for sharing machine-readable interlinked data on the Web. 

To store data in linked data, we use [RDF](https://ca.wikipedia.org/wiki/Resource_Description_Framework) where every
piece of information can be specified using a triple: 
(Subject, Predicate, Object).

[Turtle](https://ca.wikipedia.org/wiki/Turtle_(sintaxi)) (Terse RDF Triple Language) is a common way to represent 
semantic data in RDF format.

In the linked_data test, you will find [data.ttl](linked_data/data.ttl) where some buildings are defined using turtle. 
Additionally, in [query.py](linked_data/query.py) you will find a piece of code that uses 
[rdflib](https://rdflib.readthedocs.io/en/stable/) to load this data and prepare to execute some queries.

Your assignment is to generate the sparql queries required to obtain the following information:
    - List of all buildings in the file
    - List of all buildings of a type
    - List of all devices linked to a building

### Problem 4: REST api
With the daily time-series generated with the data in Problem2, build a rest API to retrieve this information by placing a GET request.
You can chose any database to store the previous time-series.

Use docker containers to create the database and the API with your implementation

provide a docker-compose.yaml file to build and run the application using the `docker-compose up` command and set
the API documentation.



