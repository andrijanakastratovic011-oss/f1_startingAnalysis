from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026, 6, 1) 
}

# Koristimo zvanični "with" blok koji Airflow 2.10 zahteva za stabilan rad
with DAG(
    dag_id='DAG-1',
    default_args=default_args, 
    catchup=False,
    schedule_interval=None
) as dag:

    start = EmptyOperator(task_id="start_pipeline")
    
    # Docker mapira tvoje foldere u /opt/airflow/, zato koristimo ove Linux putanje:
    load_bronze = BashOperator(task_id='load_bronze', bash_command="python /opt/airflow/bronze/main.py")
    load_silver = BashOperator(task_id='load_silver', bash_command="python /opt/airflow/silver/main.py")
    dqc_silver = BashOperator(task_id='dqc_silver', bash_command="python /opt/airflow/silver/dqc.py")
    load_gold = BashOperator(task_id='load_gold', bash_command="python /opt/airflow/gold/main.py")
    dqc_gold = BashOperator(task_id='dqc_gold', bash_command="python /opt/airflow/gold/dqc.py")
    
    end = EmptyOperator(task_id="end_pipeline")

    # Pipeline struktura i zavisnosti
    start >> load_bronze >> load_silver 
    load_silver >> dqc_silver 
    load_silver >> load_gold >> dqc_gold
    [dqc_silver, dqc_gold] >> end
