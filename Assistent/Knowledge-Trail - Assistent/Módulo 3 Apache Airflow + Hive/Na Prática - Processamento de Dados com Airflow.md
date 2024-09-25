[Voltar ao módulo 3](../Módulo%203%20Apache%20Airflow%20+%20Hive.md)

# Na Prática - Processamento de Dados com Airflow, Spark e Hive

## Visão Geral

Neste módulo, você colocará em prática os conceitos abordados até o momento. O foco aqui será utilizar ferramentas como MinIO, Airflow, PySpark e Zeppelin para processar dados de um e-commerce fictício e realizar análises. O fluxo geral será verificar se os arquivos CSV necessários estão disponíveis no MinIO, processar os dados utilizando PySpark através de um workflow definido no Airflow e, por fim, realizar consultas utilizando o Apache Zeppelin com Hive.

### Objetivos:

- Verificar a disponibilidade dos arquivos CSV no MinIO.
- Estabelecer a conexão e executar uma DAG no Airflow que utiliza o Apache Livy para processar dados com PySpark.
- Armazenar os resultados em uma tabela Hive.
- Analisar os resultados utilizando Apache Zeppelin.

---

## Passo 1: Verificar Arquivos CSV no MinIO

O primeiro passo é garantir que os arquivos CSV necessários para o processamento estejam no MinIO. No módulo anterior, os arquivos foram enviados ao MinIO. Agora, é hora de verificá-los:

1. Acesse a interface web do MinIO através do navegador usando o endereço `http://localhost:9001`.
2. Na interface do MinIO, navegue até o bucket onde você armazenou os arquivos no módulo anterior.
3. Verifique se os seguintes arquivos estão presentes:
   - `olist_orders_dataset.csv`
   - `olist_order_items_dataset.csv`
   - `olist_order_payments_dataset.csv`

Esses arquivos contêm os dados necessários para o processamento de pedidos, itens e pagamentos do e-commerce.

---

## Passo 2: Configurar Conexão do Airflow com o Livy

Antes de rodar a DAG, precisamos estabelecer a conexão entre o Airflow e o Livy para garantir que o Apache Airflow consiga enviar as tarefas PySpark para serem executadas no Spark.

### 2.1. Acessar o Airflow e Configurar a Conexão

1. Acesse o Airflow através do navegador no endereço `http://localhost:8081`.
2. No menu principal, vá até a seção **Admin** > **Connections**.
3. Clique no botão **+** no canto superior direito para criar uma nova conexão.

### 2.2. Definir os Parâmetros da Conexão

Na tela de criação da nova conexão, preencha os campos com as seguintes informações:

- **Conn Id**: `livy_spark_conn`
  (Este é o ID que será usado na DAG para identificar a conexão)
- **Conn Type**: `Apache Livy`
  (Selecione `Apache Livy` no menu dropdown)
- **Host**: `livy`
  (Este é o hostname onde o Livy está rodando, geralmente definido como `livy` no docker-compose ou em outro ambiente de execução)
- **Port**: `8998`
  (O Livy geralmente usa a porta padrão `8998`)
- **Extra**: Deixe vazio, a menos que precise passar informações adicionais de configuração.

1. Após preencher todos os campos, clique em **Save** para salvar a conexão.

## Passo 3: Executar DAG no Airflow

Agora que os arquivos CSV foram verificados no MinIO, vamos utilizar o Apache Airflow para orquestrar o processamento desses dados. Para isso, temos uma DAG pré-definida que executa um script PySpark usando Livy, uma interface REST para interagir com o Apache Spark.

### 3.1. Acessar o Apache Airflow

1. Acesse o Airflow através do navegador, usando o endereço `http://localhost:8081`.
2. No Airflow, procure pela DAG chamada `livy_process_ecommerce_data_dag`.

### 3.2. Explicação da DAG

Abaixo, está o código da DAG que será executada. A função principal dessa DAG é executar um script PySpark para processar dados de e-commerce.

```python
from airflow import DAG
from airflow.providers.apache.livy.operators.livy import LivyOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'livy_process_ecommerce_data_dag',
    default_args=default_args,
    description='Executa o script de processamento de dados via Livy e Spark',
    schedule_interval=timedelta(days=1),
)

livy_task = LivyOperator(
    task_id='run_livy_spark_process_ecommerce_data',
    livy_conn_id='livy_spark_conn',
    file='s3a://scripts/process_ecommerce_data.py',
    conf={"spark.executor.memory": "2g", "spark.driver.memory": "1g"},
    polling_interval=10,
    dag=dag,
)

livy_task

```

### 3.3. Explicação do Código:

- **`default_args`**: Define os parâmetros padrão, como o dono da DAG, se ela depende de execuções anteriores e como ela deve lidar com falhas e tentativas de reexecução.
- **`DAG`**: Um objeto DAG define o workflow. O argumento `schedule_interval` define a periodicidade com que essa DAG será executada (diariamente neste caso).
- **`LivyOperator`**: Este operador é responsável por enviar um script PySpark ao Livy, que por sua vez, executa o script no cluster Spark.
  - **`file`**: O caminho para o script PySpark que será executado, armazenado no S3 compatível com MinIO.
  - **`conf`**: Configurações de Spark, incluindo a quantidade de memória disponível para o executor e o driver.

### 3.4. Verificar a Conexão

Após criar a conexão, ela deve aparecer na lista de conexões configuradas. Verifique se o `Conn Id` está correto (`livy_spark_conn`) e se o tipo de conexão é `Apache Livy`.

### 3.5. Executar a DAG

1. No Airflow, ative a DAG `livy_process_ecommerce_data_dag` clicando no botão de "toggle" (ativação).
2. Execute a DAG manualmente clicando no ícone de "trigger" (gatilho).

---

## Passo 4: Explicação do Script PySpark

O script que será executado na DAG realiza o processamento dos dados de e-commerce. Vamos entender cada parte desse script.

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, count, date_format

spark = SparkSession.builder.appName("SimpleEcommerceProcessing").enableHiveSupport().getOrCreate()

base_path = "s3a://meus-dados/"

orders_path = f"{base_path}olist_orders_dataset.csv"
items_path = f"{base_path}olist_order_items_dataset.csv"
payments_path = f"{base_path}olist_order_payments_dataset.csv"

orders_df = spark.read.format("csv").option("header", "true").load(orders_path)
items_df = spark.read.format("csv").option("header", "true").load(items_path)
payments_df = spark.read.format("csv").option("header", "true").load(payments_path)

orders_df = orders_df.withColumn("order_purchase_timestamp", col("order_purchase_timestamp").cast("timestamp"))

order_items_agg = items_df.groupBy("order_id") \\
    .agg(
        _sum("price").alias("total_order_price"),
        count("order_item_id").alias("total_items")
    )

payments_agg = payments_df.groupBy("order_id") \\
    .agg(
        _sum("payment_value").alias("total_payment_value")
    )

final_data = order_items_agg.join(payments_agg, "order_id", "inner")

final_data = final_data.join(orders_df.select("order_id", date_format(col("order_purchase_timestamp"), "yyyyMMdd").alias("order_date")), "order_id", "inner")

final_data.write \\
    .format("orc") \\
    .option("compression", "zlib") \\
    .mode("overwrite") \\
    .saveAsTable("default.Simple_Purchase_Analysis")

final_data.show()

```

### 4.1. Explicação do Código:

- **SparkSession**: Inicializa uma sessão Spark com suporte ao Hive.
- **Caminhos dos arquivos**: Os arquivos CSV são carregados diretamente do MinIO via o protocolo `s3a`.
- **Leitura dos datasets**: Os datasets de pedidos, itens e pagamentos são lidos no formato CSV com cabeçalhos.
- **Conversão de tipos**: A coluna `order_purchase_timestamp` é convertida para o tipo `timestamp`.
- **Agregação dos dados**:
  - Agrupamento por `order_id` e cálculo do total gasto (`total_order_price`) e número total de itens (`total_items`).
  - Soma do valor total pago por pedido (`total_payment_value`).
- **Joins**: Realiza joins para combinar as agregações dos itens, pagamentos e pedidos.
- **Escrita no Hive**: O DataFrame final é salvo como uma tabela Hive no formato ORC com compressão `zlib`.

---

## Passo 5: Consultas no Zeppelin com Hive

Após o processamento e armazenamento dos dados no Hive, vamos utilizar o Apache Zeppelin para realizar consultas.

1. Acesse o Apache Zeppelin através do navegador, usando o endereço `http://localhost:8080`.
2. Dentro do notebook `olist_data_processing`, execute os seguintes comandos Hive.

### 5.1. Comandos Hive para execução:

```sql
%hive
show tables;

```

Este comando exibe todas as tabelas disponíveis no Hive, incluindo a tabela `simple_purchase_analysis` criada pelo script PySpark.

```sql
%hive
select * from simple_purchase_analysis;

```

Este comando seleciona todos os dados da tabela `simple_purchase_analysis`, mostrando o total gasto por pedido, o número de itens e a data da compra.

---

## Conclusão

Neste módulo, você aprendeu a verificar dados no MinIO, configurar e executar uma DAG no Airflow para processar dados com PySpark e, finalmente, consultar os resultados em uma tabela Hive usando o Apache Zeppelin. Este fluxo exemplifica um pipeline de dados completo, utilizando ferramentas amplamente usadas em Engenharia de Dados.
