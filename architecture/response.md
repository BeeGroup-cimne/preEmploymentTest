### Problem 1: Architecture (discussion)
In a project, we need to gather electricity consumption and weather data time series  continuously from some very slow api, and store them in a database. The data we are gathering at certain points can be more than the data  that can be processed by the system. 

Also, the api is very slow and the process to gather it has to be parallelized.

Propose an architecture to be able to gather and store this data. Propose the different protocols, databases to use, technologies, etc).

### ANSWER:
The best way to deal with Big Data (time series data) is using a cloud based solution, which offers us paralleism and the commodity to be able to scale up the hardware. Imedialy this imples use the "Shared nothing" architecture, which interconnects many completely independent machines through the network. Each machine has its own disk, memory and obviously processor, which work independently, but at the same time are exposed to the others.

Regarding the data collection, I would use Kafka as the streaming platform, since our dataset is a data stream (data that is produced incrementally over time). Kafka is advantageous for scenarios with irregular arrival, as it will introduce some queuing mechanism to smooth the arrival rate and ensure not data is lost. Moreover, Kafka provides near-real time time response, allowing complex processing and efficient distribution of data to multiple engine instances.

To determine where each message goes after being processed by a given machine, I would suggest the non-grouping pattern, where execution stays in the same thread (if possible). This pattern involves keeping the execution within the same thread whenever possible, minimizing unnecessary data movement and ensuring that information from previous processing steps is available in the next one.

Finally, the choosen data warehousing architecture is the kappa architecture (Figure 1), which it is a simplification of the traditional Lambda architecture. K-architecture eliminates the need to maintain separate implementations for data transformations in different systems.  If for some reason, we require different versions of the transformations for different statistical models, we can keep all of them in the same system and choose the most appropriate one at every moment, independently of whether it is for training or production.

The Kappa architecture consists of two layers: 
* stream processing: this layer handles real-time decision-making and processing of streaming data.
* serving: this layer stores results and responds to queries based on these results.

![kappa architecture](https://github.com/miriam-mendez/preEmploymentTest/architecture/kappa.PNG)