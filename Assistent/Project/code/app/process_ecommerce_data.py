from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, count, date_format

# Inicializa a Spark Session
spark = SparkSession.builder.appName("SimpleEcommerceProcessing").enableHiveSupport().getOrCreate()

# Caminhos dos arquivos CSV no MinIO (ou outro serviço compatível com S3)
base_path = "s3a://meus-dados/"

# Caminhos para os datasets
orders_path = f"{base_path}olist_orders_dataset.csv"
items_path = f"{base_path}olist_order_items_dataset.csv"
payments_path = f"{base_path}olist_order_payments_dataset.csv"

# Carregar os datasets em DataFrames
orders_df = spark.read.format("csv").option("header", "true").load(orders_path)
items_df = spark.read.format("csv").option("header", "true").load(items_path)
payments_df = spark.read.format("csv").option("header", "true").load(payments_path)

# Conversão de tipos para as colunas necessárias
orders_df = orders_df.withColumn("order_purchase_timestamp", col("order_purchase_timestamp").cast("timestamp"))

# Agregação simples: total gasto por pedido e total de itens
order_items_agg = items_df.groupBy("order_id") \
    .agg(
        _sum("price").alias("total_order_price"),
        count("order_item_id").alias("total_items")
    )

# Agregação de pagamentos: total de valor pago por pedido
payments_agg = payments_df.groupBy("order_id") \
    .agg(
        _sum("payment_value").alias("total_payment_value")
    )

# Join entre agregações de pedidos e pagamentos
final_data = order_items_agg.join(payments_agg, "order_id", "inner")

# Adicionar data da compra formatada
final_data = final_data.join(orders_df.select("order_id", date_format(col("order_purchase_timestamp"), "yyyyMMdd").alias("order_date")), "order_id", "inner")

# Escrever o DataFrame final em uma tabela Hive com compressão ORC
final_data.write \
    .format("orc") \
    .option("compression", "zlib") \
    .mode("overwrite") \
    .saveAsTable("default.Simple_Purchase_Analysis")

# Mostrar o resultado final
final_data.show()
