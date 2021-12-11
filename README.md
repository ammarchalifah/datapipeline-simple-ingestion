# Simple Data Pipeline
*Simple data ingestion from a source Postgres database to destination Postgres database*

## Requirement
docker-compose, psql (postgres client)

## Setup
All required setups are defined in the `docker-compose` file. The docker-compose consists of standard Airflow services (such as webserver, scheduler, worker, redis, and airflow db), source Postgres DB and target Postgres DB.  All containers are built from public Docker images.

The docker-compose file took environment variables from `.env` file. This project has two DAGs, one for creating the sample table in the source DB and the other one for migrating the table from the source DB to the target DB. The DAGs can be found under `./dags/`.

## Usage
1. Clone this repository and move your active directory inside the project
```cd datapipeline-simple-ingestion```
2. Adjust credentials (Airflow, source DB, and target DB) by changing values in `.env`
3. Run the containers by the following command
```
docker-compose up airflow-init
docker-compose up -d
```
4. Open the Airflow web UI by accessing `https://localhost:5884`
5. Open the first DAG (`dag_postgres_create_table`), unpause the DAG and trigger it to create sample table.
6. Open the second DAG (`dag_datalake_postgres`), unpause and trigget it to execute data ingestion task.
7. To inspect the migrated table, access the target DB by the following command
```
psql -h localhost -p 5440 -U {postgres username} -d {postgres db} --password
```
The credentials is identical to the ones inside `.env` file.

Then,
```
SELECT * FROM sample_table;
```