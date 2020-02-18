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
1. Fix - attach a volume to a container
    1. create docker image from container with current db and
    2. start new container from new image with **volume** to a folder in this project
    3. remove old original image
    4. update configuration to start with new image/container
    5. check a wey to privately publish the new image for



