from datetime import datetime
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

default_args = {
  'start_date': datetime(2021, 1, 1),
}

with DAG(
    dag_id="taxi-price-pipeline",
    schedule_interval='@daily',
    default_args=default_args,
    tags=['spark'],
    catchup=False) as dag:
    
    # preproces
    preproces = SparkSubmitOperator(
        application="/Users/yoon/Desktop/yoon/study/DATA/fastcampus/data-engineering/02-airflow/preprocess.py",
        task_id="preprocess",
        conn_id="spark_local"
    )

    # tune hyperparameter
    tune_hyperparameter = SparkSubmitOperator(
        application="/Users/yoon/Desktop/yoon/study/DATA/fastcampus/data-engineering/02-airflow/tune_hyperparameter.py",
        task_id="tune_hyperparameter",
        conn_id="spark_local"
    )

    #train_model
    train_model = SparkSubmitOperator(
        application="/Users/yoon/Desktop/yoon/study/DATA/fastcampus/data-engineering/02-airflow/train_model.py",
        task_id="train_model",
        conn_id="spark_local"
    )

    #의존성
    preproces >> tune_hyperparameter >> train_model
    