

1. Recollida de dades: Arquitectura orientada a esdeveniments. Llibreria asyncio python per gestionar multiples sollicituds API de manera concurrent i millorar la velocitat de recopilació de dades[1]. 

2. Cua de Missatges: Sistema de cua de missatges com Apache Kafka o Amazon Kinesis. Afegint a un buffer les dades entrants, permetent al sistema processar-les al seu propi ritme. També ofereix suport al processament de dades en temps real[2].

3. Processament de Dades: Us de microserveis per processar les dades. Cada microservei pot ser responsable d'una tasca específica, com ara neteja de dades, transformació o agregació. Permet paral·lelitzar les transformacions, oferint escalabilitat i flexibilitat[3].

4. Base de Dades: Per emmagatzemar sèries temporals, disposem de bases de dades de sèries temporals (TSDB) com InfluxDB, optimitzades per gestionar dades amb marques de temps i poden executar de manera eficient consultes comunes de sèries temporals[4]. 

5. Cloud-Based: Us d'eines cloud per emmagatzemar i processar dades per temes d'escalabilitat, elasticitat i seguretat, aspectes clau per tractar amb grans volums de dades[3].

6. Optimització de Dades: Seguir les millors pràctiques per a col·leccions de sèries temporals, com ara optimitzar les insercions, agrupar les escriptures de documents, utilitzar un ordre de camps consistent en els documents [5].


Referències:
[1] https://stackoverflow.com/questions/57126286/fastest-parallel-requests-in-python
[2] https://dzone.com/refcardz/real-time-data-architecture-patterns
[3] https://www.linkedin.com/advice/1/how-can-you-make-data-processing-more-scalable
[4] https://www.influxdata.com/the-best-way-to-store-collect-analyze-time-series-data/
[5] https://www.mongodb.com/docs/manual/core/timeseries/timeseries-best-practices/
