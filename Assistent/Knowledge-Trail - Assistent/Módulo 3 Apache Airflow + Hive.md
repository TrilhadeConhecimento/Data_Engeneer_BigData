[Início](../README.md)

# Módulo 3: Apache Airflow + Hive

## Introdução ao Apache Airflow e Apache Hive

O **Apache Airflow** e o **Apache Hive** são ferramentas amplamente utilizadas no ecossistema de Engenharia de Dados para automação, orquestração e gerenciamento de grandes volumes de dados.

O **Apache Airflow** é uma plataforma poderosa e flexível para a criação, agendamento e monitoramento de workflows (fluxos de trabalho). Um workflow pode ser entendido como uma sequência de tarefas que precisam ser executadas em uma ordem específica para alcançar um objetivo final, como o processamento de dados, a movimentação de arquivos ou a integração de sistemas. Airflow permite que você defina workflows complexos como código, facilitando a manutenção, a reprodução e a colaboração. Sua interface gráfica também facilita o monitoramento e a gestão dos workflows em tempo real.

O **Apache Hive** é uma ferramenta de data warehouse usada para consultar e gerenciar grandes volumes de dados armazenados em sistemas distribuídos, como o Hadoop ou o S3. Ele permite a execução de consultas SQL (HiveQL) sobre grandes datasets e oferece uma maneira escalável de organizar, particionar e consultar esses dados. Além disso, o Hive se integra bem com outros sistemas de processamento distribuído, como o Apache Spark, e é frequentemente utilizado em conjunto com o Airflow para orquestrar pipelines de dados.

### Objetivos do Módulo

- **Explorar a arquitetura do Apache Airflow e do Hive**: Entender como o Airflow orquestra workflows e como o Hive facilita a consulta e o gerenciamento de grandes datasets.
- **Compreender os principais conceitos**: Aprender os conceitos fundamentais do Airflow (como DAGs, Tasks e Operators) e do Hive (tabelas, partições e consultas SQL).
- **Criar e executar um workflow de dados integrando Airflow e Hive**: Escrever uma DAG no Airflow que processe dados com PySpark e os armazene em uma tabela Hive.
- **Configurar o Airflow e o Hive no seu ambiente**: Instalar e configurar o Airflow e o Hive localmente para que você possa começar a criar e gerenciar pipelines de dados.

### Requisitos

- **Docker**: Vamos utilizar contêineres Docker para rodar tanto o Airflow quanto o Hive de maneira isolada e fácil de gerenciar. Certifique-se de que o Docker está instalado e funcionando corretamente.
- **Conhecimento básico em Python**: Como o Airflow define workflows como código, um entendimento básico de Python será útil.
- **Conhecimento básico em SQL**: O Hive usa uma linguagem SQL para interagir com os dados, então ter noções de SQL será vantajoso.
- **Acesso às interfaces do Apache Airflow e do Hive**: A interface web do Airflow é essencial para monitoramento e gestão de workflows, e a interface do Hive será usada para realizar consultas nos dados. No nosso ambiente, ambos estarão acessíveis através do navegador.

### Estrutura do Módulo

1. **Conceitos Centrais do Airflow e do Hive**: Uma visão detalhada dos principais conceitos de ambas as ferramentas e como elas se integram para formar pipelines de dados eficientes.
2. **Criando Sua Primeira DAG e Consultas no Hive**: Passo a passo para criar uma DAG que processa dados com PySpark e salva os resultados em uma tabela Hive, além de como consultar esses dados no Hive.
3. **Monitoramento e Gestão de Workflows**: Como usar a interface web do Airflow para monitorar e gerenciar a execução das tarefas e como usar o Hive para realizar consultas de dados processados.

---

### Explicação da Integração entre Airflow e Hive

A combinação do Airflow com o Hive é bastante poderosa. O Airflow orquestra o pipeline de dados, agendando tarefas, gerenciando dependências e controlando o fluxo de execução. Já o Hive oferece uma maneira eficiente de armazenar, organizar e consultar os resultados desses processos. No contexto deste módulo, você criará workflows no Airflow que processam dados de e-commerce com PySpark e salvam os resultados em uma tabela Hive, que poderá ser consultada para análise posterior.

---

[Conceitos Centrais](Módulo%203%20Apache%20Airflow%20+%20Hive/Conceitos%20Centrais.md)

[Ciclo de Vida da Task](Módulo%203%20Apache%20Airflow%20+%20Hive/Ciclo%20de%20Vida%20da%20Task.md)

[DAG com Bash Operator](Módulo%203%20Apache%20Airflow%20+%20Hive/DAG%20com%20Bash%20Operator.md)

[DAG com Python Operator](Módulo%203%20Apache%20Airflow%20+%20Hive/DAG%20com%20Python%20Operator.md)

[Na Prática - Processamento de Dados com Airflow, Spark e Hive](Módulo%203%20Apache%20Airflow%20+%20Hive/Na%20Prática%20-%20Processamento%20de%20Dados%20com%20Airflow.md)
