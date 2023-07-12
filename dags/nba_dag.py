from operators.nba.bio import NBABioOperator
from operators.nba.stats import NBAStatsOperator
from operators.nba.salary import NBASalaryOperator
from operators.nba.merge import NBAMergeOperator

from datetime import datetime

from airflow import DAG


default_args = {
    "owner": "Unifor",
    "start_date": datetime(1999,1,1),
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "colares.caio@gmail.com",
    "retries": 1
}

with DAG(
    dag_id='nba_data_crawler',
    description='NBA Data Crawler',
    default_args=default_args,
    schedule_interval="@yearly",
    tags=['NBA', 'Crawler', 'Statistics']) as dag:

    stats_operator = NBAStatsOperator(task_id="stats_nba", dag=dag,  process_date="{{ ds }}")
    salary_operator = NBASalaryOperator(task_id="salary_nba",dag=dag,  process_date="{{ ds }}")
    
    bio_operator = NBABioOperator(task_id="bios_nba", dag=dag,  process_date="{{ ds }}")
    
    merge_operator = NBAMergeOperator(task_id="merge_nba", dag=dag,  process_date="{{ ds }}")

    [stats_operator, salary_operator] >> bio_operator >> merge_operator
    