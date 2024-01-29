# Getting started

Start up the application by running:

`docker compose build`

`docker compose up`



Check the server is ON in the url:
>localhost:5000/

To turn OFF the API just run:

`docker compose down`




## How to get consumption data

Get data consumption by passing the 'date' with format YYYY-MM-DD as a parameter in the url
>localhost:5000/consumption/?date=...

Example:
>localhost:5000/consumption/?date=2019-04-30


