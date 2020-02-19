### Starting the dev environment
Creating a docker image for PostgreSQL container:  
For the first run ( e.g. @make psql-docker from make start ) use gitBash to avoid ${PWD} error

###  Docker containers
##### PostgreSQL container:
exposed port: 32768 --> 5432  
docker database: **docker**  
docker database user: **docker**

**Useful PostgreSQL commands**  
\du ( display users )  
\l ( list databases )
\c <db_name>  ( connect to database )

**Useful links:**  
Docker:  
Creating the Dockerfile for PostgreSQL image:  
https://docs.docker.com/engine/examples/postgresql_service/

## TODO
1. ~~Fix - attach a volume to a container~~
   1. ~~create docker image from container with current db and~~
   2. ~~start new container from new image with **volume** to a folder in this project~~
   5. ~~check a wey to privately publish the new image for~~

2. ~~backup psql db to a file outside container~~

   3. ~~used Docker cp command~~



