[Voltar ao módulo 3](../Módulo%203%20Apache%20Airflow%20+%20Hive.md)

# DAG com Bash Operator

Uma DAG no Apache Airflow é uma coleção de tarefas organizadas de forma que descrevam um processo de trabalho ou pipeline. Dentro de uma DAG, você pode usar diversos operadores para definir as tarefas, e um dos mais comuns é o **BashOperator**.

### O que é uma DAG?

Uma DAG (Directed Acyclic Graph) no Airflow é uma estrutura que representa um fluxo de trabalho. Cada nó na DAG é uma tarefa (task), e as arestas (edges) entre os nós definem as dependências entre essas tarefas. O Airflow garante que as tarefas sejam executadas na ordem correta, seguindo essas dependências.

### O que é o BashOperator?

O **BashOperator** é um operador no Apache Airflow que permite executar comandos Bash diretamente no ambiente onde o Airflow está rodando. Esse operador é útil para tarefas que precisam de comandos do sistema operacional, como mover arquivos, chamar scripts shell, ou executar comandos Unix.

### Criando uma DAG com BashOperator

Aqui está um exemplo simples de como criar uma DAG no Airflow que utiliza o BashOperator:

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
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
    'bash_operator_example',
    default_args=default_args,
    description='Uma DAG simples com BashOperator',
    schedule_interval=timedelta(days=1),
)

# Definindo as tasks com BashOperator

# Task 1: Imprimir a data
print_date = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

# Task 2: Dormir por 5 segundos
sleep = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    dag=dag,
)

# Task 3: Exibir uma mensagem
echo_message = BashOperator(
    task_id='echo_message',
    bash_command='echo "Airflow DAG com BashOperator!"',
    dag=dag,
)

# Definindo a ordem de execução das tasks
print_date >> sleep >> echo_message

```

### Explicação do Exemplo

1. **Definição de `default_args`**: Esta seção define os argumentos padrão que serão aplicados a todas as tasks da DAG, como o proprietário (`owner`), se a execução depende de execuções anteriores (`depends_on_past`), a data de início (`start_date`), entre outros.
2. **Definição da DAG**: A DAG é definida com o nome `'bash_operator_example'`, e configurada para rodar diariamente (`schedule_interval=timedelta(days=1)`).
3. **Definição das Tasks**:
   - **`print_date`**: Executa o comando `date`, que imprime a data atual.
   - **`sleep`**: Executa o comando `sleep 5`, que faz a task dormir por 5 segundos.
   - **`echo_message`**: Executa o comando `echo "Airflow DAG com BashOperator!"`, que imprime a mensagem no console.
4. **Dependências das Tasks**: As tasks são encadeadas usando o operador `>>`, indicando que `print_date` deve ser executada antes de `sleep`, que por sua vez deve ser executada antes de `echo_message`.

### Executando a DAG

Depois de criar e salvar essa DAG em um arquivo Python dentro da pasta `dags` do Airflow, o Scheduler do Airflow irá detectar automaticamente a nova DAG. Você pode então ativar e monitorar a DAG através da Web UI do Airflow.

### Quando Usar o BashOperator?

O BashOperator é ideal para situações em que você precisa executar comandos simples do sistema, invocar scripts que já existem, ou realizar operações que não necessitam de integrações complexas. Contudo, para tarefas que envolvem lógica de negócios complexa, é geralmente mais apropriado usar operadores dedicados ou criar um PythonOperator que encapsule essa lógica.

### Próximo Documento

- [DAG com Python Operator](DAG%20com%20Python%20Operator.md)
