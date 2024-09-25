[Voltar ao módulo 3](../Módulo%203%20Apache%20Airflow%20+%20Hive.md)

# DAG com Python Operator

No Apache Airflow, uma DAG (Directed Acyclic Graph) pode incluir tarefas definidas com diferentes operadores, e o **PythonOperator** é um dos mais poderosos e flexíveis. Ele permite que você execute funções Python diretamente como parte do seu fluxo de trabalho, o que é muito útil para tarefas que envolvem lógica complexa, manipulação de dados, ou integração com APIs.

### O que é uma DAG?

Uma DAG (Directed Acyclic Graph) no Airflow representa um conjunto de tarefas organizadas de forma a definir a execução de um workflow. As arestas entre as tarefas estabelecem as dependências e a ordem de execução.

### O que é o PythonOperator?

O **PythonOperator** é um operador no Apache Airflow que permite executar funções Python. Ao contrário do BashOperator, que executa comandos do sistema operacional, o PythonOperator roda código Python diretamente. Isso torna o PythonOperator ideal para tarefas como processamento de dados, chamadas de APIs, e qualquer outro tipo de lógica que você possa codificar em Python.

### Criando uma DAG com PythonOperator

Aqui está um exemplo básico de como criar uma DAG no Airflow utilizando o PythonOperator:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Definindo os argumentos padrão da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Definindo a DAG
dag = DAG(
    'python_operator_example',
    default_args=default_args,
    description='Uma DAG simples com PythonOperator',
    schedule_interval=timedelta(days=1),
)

# Função Python a ser executada
def print_hello():
    return 'Hello, Airflow!'

# Definindo a task com PythonOperator
hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,  # Nome da função Python a ser executada
    dag=dag,
)

# Task adicional que executa uma função com parâmetros
def multiply_by_two(x):
    return x * 2

multiply_task = PythonOperator(
    task_id='multiply_task',
    python_callable=multiply_by_two,  # Nome da função
    op_args=[10],  # Argumentos posicionais para a função
    dag=dag,
)

# Definindo a ordem de execução das tasks
hello_task >> multiply_task

```

### Explicação do Exemplo

1. **Definição de `default_args`**: Estes são os argumentos padrão aplicados a todas as tasks na DAG, incluindo informações como o proprietário (`owner`), se a execução depende de execuções passadas (`depends_on_past`), e o número de tentativas em caso de falha (`retries`).
2. **Definição da DAG**: A DAG é nomeada `'python_operator_example'` e está programada para rodar uma vez por dia (`schedule_interval=timedelta(days=1)`).
3. **Função `print_hello`**: Esta é uma função Python simples que retorna a string `"Hello, Airflow!"`. Esta função será chamada pelo PythonOperator.
4. **Task `hello_task`**: Esta task usa o `PythonOperator` para executar a função `print_hello`.
5. **Função `multiply_by_two`**: Outra função Python que recebe um argumento (`x`) e retorna o dobro desse valor.
6. **Task `multiply_task`**: Esta task usa o `PythonOperator` para executar a função `multiply_by_two` com o argumento `10`, o que resulta em `20`.
7. **Encadeamento de Tasks**: As tasks são encadeadas usando `>>`, o que indica que `hello_task` deve ser executada antes de `multiply_task`.

### Passagem de Parâmetros

O PythonOperator permite que você passe parâmetros para a função Python através de `op_args` (argumentos posicionais) e `op_kwargs` (argumentos nomeados):

- **`op_args`**: Uma lista de argumentos posicionais que serão passados para a função.
- **`op_kwargs`**: Um dicionário de argumentos nomeados.

### Utilizando o XComs para Compartilhar Dados Entre Tasks

O Airflow permite que você compartilhe dados entre tasks usando o XComs (cross-communications). Com o PythonOperator, você pode facilmente enviar e receber dados entre tasks:

```python
def push_to_xcom(ti):
    ti.xcom_push(key='my_key', value='some_value')

def pull_from_xcom(ti):
    my_value = ti.xcom_pull(key='my_key')
    print(f'Retrieved value: {my_value}')

push_task = PythonOperator(
    task_id='push_task',
    python_callable=push_to_xcom,
    dag=dag,
)

pull_task = PythonOperator(
    task_id='pull_task',
    python_callable=pull_from_xcom,
    dag=dag,
)

push_task >> pull_task

```

### Quando Usar o PythonOperator?

Use o PythonOperator quando você precisa:

- Executar lógica complexa diretamente no código Python.
- Fazer chamadas de APIs ou interagir com outras bibliotecas Python.
- Manipular dados em memória antes de passá-los para outras tarefas.
- Integrar com serviços que têm bibliotecas Python disponíveis.

O PythonOperator é uma ferramenta muito poderosa no Airflow, permitindo que você crie workflows altamente personalizados e complexos, aproveitando todo o ecossistema Python.

Se precisar de mais detalhes ou exemplos, estou aqui para ajudar!

### Próximo Documento

- [Na Prática - Processamento de Dados com Airflow, Spark e Hive](Na%20Prática%20-%20Processamento%20de%20Dados%20com%20Airflow.md)
