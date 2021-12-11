from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator

import logging

dag = DAG(
    dag_id='dag_postgres_create_table',
    default_args={'start_date': days_ago(1)}, 
    schedule_interval=None,
    tags = ['postgres']
    )


create_sample_table = PostgresOperator(
    task_id = "create_sample_table",
    postgres_conn_id = "postgres_source",
    sql = """
    DROP TABLE IF EXISTS sample_table;
    
    CREATE TABLE sample_table
    (
        id integer,
        creation_date date,
        updated_date date,
        company_id integer,
        cash_in bigint,
        cash_out bigint
    );

    INSERT INTO sample_table VALUES (1, '2021-10-01', '2021-10-01', 234, 450, 455);
    INSERT INTO sample_table VALUES (2, '2021-11-01', '2021-11-01', 340, 40, 55);
    INSERT INTO sample_table VALUES (3, '2021-11-01', '2021-11-01', 340, 50, 55);
    INSERT INTO sample_table VALUES (4, '2021-11-01', '2021-11-03', 365, 1340, 3455);
    INSERT INTO sample_table VALUES (5, '2021-11-02', '2021-11-04', 365, 1200, 2455);
    INSERT INTO sample_table VALUES (6, '2021-11-04', '2021-11-04', 450, 0, 4);
    INSERT INTO sample_table VALUES (7, '2021-11-12', '2021-11-12', 450, 0, 55);
    INSERT INTO sample_table VALUES (8, '2021-11-15', '2021-11-20', 450, 0, 45);
    """,
    dag = dag
    )