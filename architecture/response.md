## **ARCHITECTURE**

1. **Data Gathering Component:**

   - I would do paralelitzation with distributed computing frameworks such as Apache Spark or by utilizing asynchronous programming in languages like Python with libraries like asyncio.

2. **Communication Protocols:**

   - MQTT for data retrieval from the API and for internal communication, if there was any, I would use Kafka.

3. **Database:**

   - The database i would use is InfluxDB because is well-suited for storing and querying time-stamped data.

4. **Scalability:**

   - It is most likely that the volume of data will increase, therefore we would be interested in having horizontal scalability, I would use kubernetes.
