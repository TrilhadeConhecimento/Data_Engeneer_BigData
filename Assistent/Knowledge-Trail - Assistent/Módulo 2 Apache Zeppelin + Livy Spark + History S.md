[Início](../README.md)

# Módulo 2: Apache Zeppelin + Livy Spark + History Server

## Introdução ao Apache Zeppelin, Livy Spark e Análise do Dataset de E-commerce

Neste módulo, vamos explorar um conjunto de datasets de um e-commerce brasileiro usando o Apache Zeppelin e o Livy Spark. Os arquivos que vamos trabalhar contêm informações detalhadas sobre pedidos, clientes, produtos, vendedores e muito mais. O objetivo é realizar uma análise aprofundada desses dados, extraindo insights valiosos e praticando operações comuns em Big Data.

## Objetivos do Módulo

- Compreender o funcionamento do Apache Zeppelin com Livy Spark.
- Carregar e explorar múltiplos datasets de um e-commerce.
- Executar operações de agregação, transformação e análise nos dados.
- Realizar consultas SQL e visualizar resultados de forma interativa.
- Integrar e cruzar dados entre diferentes datasets para extrair insights.
- Visualizar e monitorar o histórico de jobs Spark utilizando o Spark History Server.

## Requisitos

- Docker instalado e configurado corretamente.
- Ambiente Big Data Sandbox em execução, com Apache Spark, Livy, e Zeppelin disponíveis.
- Arquivos CSV carregados e disponíveis no MinIO.

## Passo 1: Acessando o Apache Zeppelin

### 1.1. Verificando a configuração

Certifique-se de que o Apache Zeppelin está rodando no Docker. O Zeppelin no Big Data Sandbox está acessível através da porta 8080:

- **Zeppelin:** [http://localhost:8080](http://localhost:8080/)

### 1.2. Acessando a interface do Zeppelin

1. Abra o navegador e acesse o Zeppelin em [http://localhost:8080](http://localhost:8080/).
2. A interface do Zeppelin aparecerá, onde você poderá criar e gerenciar notebooks.

## Passo 2: Carregando os Datasets

Vamos carregar todos os arquivos CSV mencionados. Utilizaremos a seguinte lista de arquivos:

- `olist_customers_dataset.csv`
- `olist_geolocation_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_order_payments_dataset.csv`
- `olist_order_reviews_dataset.csv`
- `olist_orders_dataset.csv`
- `olist_products_dataset.csv`
- `olist_sellers_dataset.csv`
- `product_category_name_translation.csv`

### 2.1. Configuração do Livy no Zeppelin (opicional)

Vamos começar com a configuração do Livy para conectar ao Spark.

```markdown
%livy.pyspark

# Conectando ao Livy e inicializando o SparkContext

sc = spark.sparkContext
```

### 2.2. Carregando os Datasets

Vamos carregar os datasets diretamente do MinIO. Certifique-se de que os arquivos estejam disponíveis no bucket correto. Para carregar e visualizar os dados:

```markdown
%livy.pyspark

# Caminho dos arquivos no MinIO

path = "s3a://meus-dados/"

# Carregar cada dataset como DataFrame

customers_df = spark.read.csv(path + "olist_customers_dataset.csv", header=True, inferSchema=True)
geolocation_df = spark.read.csv(path + "olist_geolocation_dataset.csv", header=True, inferSchema=True)
order_items_df = spark.read.csv(path + "olist_order_items_dataset.csv", header=True, inferSchema=True)
order_payments_df = spark.read.csv(path + "olist_order_payments_dataset.csv", header=True, inferSchema=True)
order_reviews_df = spark.read.csv(path + "olist_order_reviews_dataset.csv", header=True, inferSchema=True)
orders_df = spark.read.csv(path + "olist_orders_dataset.csv", header=True, inferSchema=True)
products_df = spark.read.csv(path + "olist_products_dataset.csv", header=True, inferSchema=True)
sellers_df = spark.read.csv(path + "olist_sellers_dataset.csv", header=True, inferSchema=True)
product_category_df = spark.read.csv(path + "product_category_name_translation.csv", header=True, inferSchema=True)

# Exibir o esquema de cada DataFrame

customers_df.printSchema()
geolocation_df.printSchema()
order_items_df.printSchema()
order_payments_df.printSchema()
order_reviews_df.printSchema()
orders_df.printSchema()
products_df.printSchema()
sellers_df.printSchema()
product_category_df.printSchema()
```

### 2.3. Explorando os Dados

Vamos começar com uma exploração inicial de cada dataset, incluindo contagem de registros e uma olhada nas primeiras linhas.

```markdown
%livy.pyspark

# Contagem de registros em cada dataset

print("Customers:", customers_df.count())
print("Geolocation:", geolocation_df.count())
print("Order Items:", order_items_df.count())
print("Order Payments:", order_payments_df.count())
print("Order Reviews:", order_reviews_df.count())
print("Orders:", orders_df.count())
print("Products:", products_df.count())
print("Sellers:", sellers_df.count())
print("Product Categories:", product_category_df.count())

# Exibir as primeiras 5 linhas de cada dataset

customers_df.show(5)
geolocation_df.show(5)
order_items_df.show(5)
order_payments_df.show(5)
order_reviews_df.show(5)
orders_df.show(5)
products_df.show(5)
sellers_df.show(5)
product_category_df.show(5)
```

## Passo 3: Análise e Transformação dos Dados

Agora que temos uma visão geral dos datasets, vamos realizar algumas operações mais detalhadas.

### 3.1. Analisando Pedidos e Clientes

Vamos explorar os pedidos (`orders_df`) e conectá-los aos clientes (`customers_df`) para ver a distribuição geográfica dos pedidos.

```markdown
%livy.pyspark

# Juntar pedidos com clientes

orders_customers_df = orders_df.join(customers_df, orders_df.customer_id == customers_df.customer_id)

# Contar o número de pedidos por estado

orders_by_state = orders_customers_df.groupBy("customer_state").count().orderBy("count", ascending=False)
orders_by_state.show()

# Visualizar os resultados em um gráfico de barras
```

### 3.2. Relacionando Pedidos e Produtos

Agora vamos explorar quais produtos estão sendo vendidos e quantos, conectando os pedidos com os itens de pedido (`order_items_df`) e os produtos (`products_df`).

```markdown
%livy.pyspark

# Juntar pedidos com itens de pedido e produtos

orders_items_products_df = order_items_df.join(products_df, "product_id")

# Contar o número de vendas por produto

product_sales = orders_items_products_df.groupBy("product_id", "product_category_name").count().orderBy("count", ascending=False)
product_sales.show(10)

# Visualizar os resultados em um gráfico de barras ou pizza
```

### 3.3. Análise de Pagamentos

Vamos analisar como os clientes estão pagando, usando o dataset de pagamentos (`order_payments_df`).

```markdown
%livy.pyspark

# Contar o número de pedidos por tipo de pagamento

payments_by_type = order_payments_df.groupBy("payment_type").count().orderBy("count", ascending=False)
payments_by_type.show()

# Contar o número de parcelas médias por pedido

avg_installments = order_payments_df.groupBy("order_id").avg("payment_installments").orderBy("avg(payment_installments)", ascending=False)
avg_installments.show(10)

# Visualizar os resultados em gráficos
```

### 3.4. Avaliações de Pedidos

Vamos ver as avaliações que os clientes deixam após receberem os produtos, usando o dataset de avaliações (`order_reviews_df`).

```markdown
%livy.pyspark

# Contar a distribuição das avaliações (quantidade por nota)

reviews_distribution = order_reviews_df.groupBy("review_score").count().orderBy("review_score")
reviews_distribution.show()

# Visualizar os resultados em um gráfico de barras
```

## Passo 4: Integração e Cruzamento de Dados

Agora, vamos realizar análises mais complexas, cruzando dados entre vários datasets.

### 4.1. Analisando a Performance dos Vendedores

Vamos juntar os dados de vendedores (`sellers_df`) com os dados de itens de pedido (`order_items_df`) para ver quais vendedores estão tendo mais sucesso.

```markdown
%livy.pyspark

# Juntar vendedores com itens de pedido

sellers_performance_df = sellers_df.join(order_items_df, "seller_id")

# Contar o número de vendas por vendedor

sales_by_seller = sellers_performance_df.groupBy("seller_id").count().orderBy("count", ascending=False)
sales_by_seller.show(10)

# Visualizar os resultados em um gráfico
```

### 4.2. Mapeando Entregas

Vamos mapear as entregas usando os dados de geolocalização (`geolocation_df`), cruzando-os com os pedidos e os vendedores.

```markdown
%livy.pyspark

# Juntar dados de geolocalização com clientes e pedidos

orders_geolocation_df = orders_customers_df.join(geolocation_df, customers_df.zip_code_prefix == geolocation_df.zip_code_prefix)

# Analisar as localizações de entrega

deliveries_by_location = orders_geolocation_df.groupBy("geolocation_city", "geolocation_state").count().orderBy("count", ascending=False)
deliveries_by_location.show(10)

# Visualizar as entregas em um mapa (utilizando ferramentas de visualização externa, como Kepler.gl)
```

## Passo 5: Salvando Resultados no MinIO

Por fim, vamos salvar alguns dos resultados dessas análises no MinIO para uso futuro.

### 5.1. Salvando os Resultados

como CSV

```markdown
%livy.pyspark

# Salvar o DataFrame de vendas por produto no MinIO

product_sales.write.csv("s3a://meus-dados/resultado-vendas-por-produto", header=True)

# Salvar o DataFrame de performance de vendedores no MinIO

sales_by_seller.write.csv("s3a://meus-dados/resultado-performance-vendedores", header=True)
```

## Passo 6: Monitorando Jobs com o Apache Spark History Server

### 3.1. Acessando o Spark History Server

O Spark History Server permite que você visualize o histórico de jobs executados e suas métricas. Ele está acessível na porta 18080 do seu ambiente.

- **Spark History Server:** http://localhost:18080

### 3.2. Navegando no History Server

1. Abra o navegador e acesse o History Server em http://localhost:18080.
2. Na página inicial, você verá uma lista de todos os jobs Spark executados. Cada job pode ser clicado para ver detalhes como DAG (Directed Acyclic Graph), tarefas, executores, entre outros.
3. Explore os jobs executados para entender melhor como o Spark distribui tarefas e como os recursos foram utilizados durante as execuções.

### 3.3. Analisando Performance

Utilize o History Server para analisar a performance dos jobs executados. Observe as fases do DAG, o tempo de execução de cada tarefa, e o uso de memória e CPU. Essa análise é crucial para otimizar jobs Spark, identificando possíveis gargalos e melhorando a eficiência do processamento.

## Conclusão

Neste módulo, exploramos uma ampla gama de operações utilizando o Apache Zeppelin e Livy Spark para analisar datasets de um e-commerce. Carregamos e transformamos os dados, realizamos consultas SQL, visualizamos resultados, e salvamos nossos insights. Essas operações cobrem uma grande parte das tarefas comuns em análise de Big Data, oferecendo uma excelente base para estudos e aplicações práticas.
