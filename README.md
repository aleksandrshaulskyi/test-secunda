# Test task

## Disclaimer
1) String length is limited to 120 characters only for the purpose of convinience.
2) DB dump is in repo for the same purpose.

## Use
1) Switch to the project directory that contains the docker-compose.yaml file.
2) ```docker-compose up --build```.
3) Move dump to a convinient location.
4) docker exec -i postgresql psql -U ```username``` ```database_name``` < ```dump.sql path```.
