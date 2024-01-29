

1.API --> 2.python script --> 3.rabbitmq --> 4.python script (multithread and multiserver) --> 5. Relational data base

1. API de la qual s'alimenta el sistema
2. Un script de python que agafi les dades de la API i les insereixi a la cua de missatgeria rabbitmq
3. Un gestor de cues, en aquest cas rabbit mqtt, que ens permetrà processar les dades al ritme del nostre sistema
4. Scrpit de python que consumeix i processa les dades emmagatzemades a la cua de missatgeria. Aquest script en python ens permet que sigui multifil i també permetria utilitzar més d'un servidor. Un cop processades les dades, alimenta la base de dades
5. A mesura que es van processant les dades, s'alimenta la base de dades relacional, per exemple, mySQL