from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'Adesh',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('Tianic_Data_Miner', default_args=default_args, schedule_interval=timedelta(days=1))

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='Tianic_Data_Miner',
    #bash_command='docker run -it --link e5a0d72e8381:27017 --link b7398774a8ba:8529 ml_base python ml/miners/titanic_miner.py',
    bash_command='docker run -it machinelearningpipeline_ml_base python ml/miners/titanic_miner.py',
    dag=dag)

t1