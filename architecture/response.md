# Architecture Proposal

## Data Gathering

 As we have a slow response from the API, we should parallelize the requests.
 This can be done using multithreading, allowing us to make multiple requests at the same time instead of waiting for one response at a time.

 In Python, we could use [asyncio](https://docs.python.org/3/librarythreading.html) or [theading](https://docs.python.org/3/librarythreading.html) for multithreading.

## Data Processing

 We're aware that we can receive more data than we can process. This is an indicator to decouple the gathering and the processing pipeline using a streaming queue.

  Doing so, we can handle better all data received and obtein better scalability. Some options could be KAFKA or AWS SQS, depending on the type of service we are looking for.

 Once we have the data in the queue, we can consume it. Based on the type of data we receive, we could create different services to clean and process the data.

## Data storage

 When data is cleaned and ready to be saved, we should consider databases for timeseries, some good options could be influxDB, TimescaleDB or AWS Timestream.

## Management of the system

 We should monitor our system in order to see its performance and its health. A good option for LOGs could be the ELK stack (ElasticSearch), this would allow us to seehow it's performing and if we have to scale our system to handle all the data.

## Protocols & Technologies

 For the communications, JSON is a good standard to send the information due its high compatibility and easy to work with.

 As I mentioned before, there are different databases that could be used, depending on the goal we are aiming for and the knowlege we have of each type of database.

 All the process could be containerized using Docker for consistency across different environments. Kubernetes could be included for container orchestration to manage and scale the system.

# Workflow

 1. The Data gathering service retrieves the data from the API and sends it to the messaging queue.
 2. The Data processing service consumes the messages from the queue, processes this information and saves it to the database.
 3. Check the monitoring of the system in order to see if a load balancer or scaling is needed.
