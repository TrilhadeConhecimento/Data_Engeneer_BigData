from airflow import DAG
from airflow.providers.apache.livy.operators.livy import LivyOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# Argumentos padrão que serão passados para cada operador na DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Definindo a DAG (grafo acíclico dirigido)
dag = DAG(
    'livy_process_ecommerce_data_dag',
    default_args=default_args,
    description='Executa o script de processamento de dados via Livy e Spark',
    schedule_interval=timedelta(days=1),
)

# Operador Livy para executar um trabalho PySpark
livy_task = LivyOperator(
    task_id='run_livy_spark_process_ecommerce_data',
    livy_conn_id='livy_spark_conn',  # Configuração do Livy no Airflow
    file='s3a://scripts/process_ecommerce_data.py',  # Caminho do script no S3
    conf={"spark.executor.memory": "2g", "spark.driver.memory": "1g"},  # Configurações de memória
    polling_interval=10,  # Intervalo de polling para verificar o status
    dag=dag,
)

# Definindo a sequência de execução das tarefas (apenas uma tarefa aqui)
livy_task
