from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from bronze.load import load_bronze
from silver.load import load_silver
from silver.dqc import dqc_silver
from gold.load import load_dim_date
from gold.load import load_dim_race
from gold.load import load_dim_driver
from gold.load import load_dim_constructor
from gold.load import load_dim_circuit
from gold.load import load_dim_status
from gold.load import load_dim_driverstandings
from gold.load import load_dim_constructorstandings
from gold.load import load_fact_results
from gold.load import load_fact_lap
from gold.load import load_fact_pitstops
from gold.dqc import dqc_gold

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026, 6, 1) 
}

with DAG(
    dag_id='DAG-1',
    default_args=default_args, 
    catchup=False,
    schedule_interval=None
) as dag:

    start = EmptyOperator(task_id="start_pipeline")
    
    # Docker mapira tvoje foldere u /opt/airflow/, zato koristimo ove Linux putanje:
    task_load_bronze = PythonOperator(task_id='load_bronze', python_callable=load_bronze)
    task_load_silver = PythonOperator(task_id='load_silver', python_callable=load_silver)
    task_dqc_silver = PythonOperator(task_id='dqc_silver', python_callable=dqc_silver)
    task_load_dim_date=PythonOperator(task_id='load_dim_date', python_callable=load_dim_date)
    task_load_dim_race = PythonOperator(task_id='load_dim_race', python_callable=load_dim_race)
    task_load_dim_driver = PythonOperator(task_id='load_dim_driver', python_callable=load_dim_driver)
    task_load_dim_constructor = PythonOperator(task_id='load_dim_constructor', python_callable=load_dim_constructor)
    task_load_dim_circuit = PythonOperator(task_id='load_dim_circuit', python_callable=load_dim_circuit)
    task_load_dim_status = PythonOperator(task_id='load_dim_satus', python_callable=load_dim_status)
    task_load_dim_constructorstandings = PythonOperator(task_id='load_dim_constructorstandings', python_callable=load_dim_constructorstandings)
    task_load_dim_driverstandings = PythonOperator(task_id='load_dim_driverstandings', python_callable=load_dim_driverstandings)
    task_load_fact_results = PythonOperator(task_id='load_fact_results', python_callable=load_fact_results)
    task_load_fact_lap = PythonOperator(task_id='load_fact_lap', python_callable=load_fact_lap)
    task_load_fact_pitstops = PythonOperator(task_id='load_fact_pitstops', python_callable=load_fact_pitstops)
    task_dqc_gold = PythonOperator(task_id='dqc_gold', python_callable=dqc_gold)
    
    end = EmptyOperator(task_id="end_pipeline")

    start >> task_load_bronze >> task_load_silver 
    task_load_silver >> task_dqc_silver 
    task_dqc_silver >> task_load_dim_date >> task_load_dim_race >> task_load_dim_driver >> task_load_dim_constructor >> task_load_dim_circuit >> task_load_dim_status >> task_load_dim_driverstandings >> task_load_dim_constructorstandings
    task_load_dim_constructorstandings >> task_load_fact_results >> task_load_fact_lap >> task_load_fact_pitstops
    task_load_fact_pitstops >> task_dqc_gold
    task_dqc_gold >> end
