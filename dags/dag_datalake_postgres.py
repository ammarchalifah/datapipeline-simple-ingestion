from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.hooks.base import BaseHook

from scripts.postgres_ingestion import ingest_postgres

dag = DAG(
    dag_id='dag_datalake_postgres',
    default_args={'start_date': days_ago(1)}, 
    schedule_interval=None,
    tags = ['postgres']
    )

connection_source = BaseHook.get_connection('postgres_source')
connection_target = BaseHook.get_connection('postgres_target')

ingest_postgres_table = PythonOperator(
    task_id = "ingest_postgres_table",
    python_callable = ingest_postgres,
    params = {
        'host_source': connection_source.host,
        'user_source': connection_source.login,
        'port_source': connection_source.port,
        'dbname_source': connection_source.schema,
        'password_source': connection_source.password,
        'host_target': connection_target.host,
        'user_target': connection_target.login,
        'port_target': connection_target.port,
        'dbname_target': connection_target.schema,
        'password_target': connection_target.password,
        'query': """SELECT * from sample_table;""",
        'table_name': 'sample_table'
    },
    dag = dag
    )