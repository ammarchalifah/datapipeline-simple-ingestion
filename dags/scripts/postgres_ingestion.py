import logging
import pandas as pd
import psycopg2

from sqlalchemy import create_engine

pd.set_option('display.max_columns', None)

def ingest_postgres(**kwargs):
    host_source = kwargs['params']['host_source']
    user_source = kwargs['params']['user_source']
    port_source = kwargs['params']['port_source']
    dbname_source = kwargs['params']['dbname_source']
    password_source = kwargs['params']['password_source']

    host_target = kwargs['params']['host_target']
    user_target = kwargs['params']['user_target']
    port_target = kwargs['params']['port_target']
    dbname_target = kwargs['params']['dbname_target']
    password_target = kwargs['params']['password_target']

    query = kwargs['params']['query']
    table_name = kwargs['params']['table_name']

    source_conn = psycopg2.connect(host=host_source, port=port_source, user=user_source, password=password_source, dbname=dbname_source)
    result_df = pd.read_sql(sql=query, con = source_conn)

    logging.info(f"Queried data: {str(result_df)}")

    # Snapshot strategy
    target_engine = create_engine(f'postgresql://{user_target}:{password_target}@{host_target}:{port_target}/{dbname_target}')
    result_df.to_sql(table_name, target_engine, if_exists='replace')
