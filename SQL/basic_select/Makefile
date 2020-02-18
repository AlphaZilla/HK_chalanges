start:
	@echo Starting PostgreSQL Docker image..
	@make psql-docker

psql-docker:
	# create new image or use the created one
	docker run -p 32768:5432 --name hr-psql-db hr_postgresql || docker start hr-psql-db
#	-v ${PWD}/db_dumps:/db_dumps_docker \

stop:
	@echo Stoping container..
	docker stop hr-psql-db
