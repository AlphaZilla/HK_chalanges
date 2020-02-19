start:
	@echo Starting PostgreSQL Docker image..
	@make psql-docker

# for first run use gitbash to not encounter error for missing PWD global var
psql-docker:
	docker run -p 32768:5432 \
	-v ${PWD}/db_dumps:/db_dumps_docker \
	--name hr-psql-db-2 -d hr-psql-provisioned-db:test_commit || docker start hr-psql-db-2


stop:
	@echo Stoping container..
#	docker stop hr-psql-db
	docker stop hr-psql-db-2
