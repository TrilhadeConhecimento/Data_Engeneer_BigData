[Início](../README.md)

# Módulo 1: MinIO

## Introdução ao MinIO

O MinIO é um servidor de armazenamento de objetos de código aberto, projetado para ser compatível com a API do Amazon S3. É uma solução poderosa e escalável para armazenar e gerenciar grandes volumes de dados não estruturados, como arquivos CSV, imagens, vídeos e documentos. Neste módulo, você aprenderá como configurar e utilizar o MinIO para suas necessidades de armazenamento local.

## Objetivos do Módulo

- Entender o que é o MinIO e suas principais funcionalidades.
- Configurar e acessar a interface do MinIO.
- Aprender a criar buckets e fazer upload de arquivos, incluindo arquivos CSV.
- Criar buckets adicionais necessários para o projeto ("warehouse" e "scripts").
- Fazer upload do arquivo `process_ecommerce_data.py` armazenado na pasta `Assistent/Project/code/app/`.
- Realizar operações básicas de gerenciamento de objetos no MinIO.

## Requisitos

- Docker deve estar instalado e configurado no seu ambiente local.
- O ambiente Docker do Big Data Sandbox deve estar em execução.

## Passo 1: Acessando o MinIO

### 1.1. Verificando a configuração

Certifique-se de que o MinIO está rodando no Docker. Se o ambiente estiver configurado corretamente, o MinIO estará acessível nas seguintes portas:

- Porta 9000: API do MinIO
- Porta 9001: Interface do usuário do MinIO

### 1.2. Acessando a interface do usuário

Abra o navegador e acesse o MinIO através do link [http://localhost:9001](http://localhost:9001/). A página de login será exibida. Use as credenciais padrão ou aquelas definidas na configuração do ambiente.

- **Username:** minioadmin
- **Password:** minioadmin

## Passo 2: Navegando pela Interface do MinIO

Após o login, você verá o painel principal do MinIO. Aqui estão algumas áreas importantes:

- **Buckets:** Contêineres onde os objetos são armazenados. Similar a pastas, mas no contexto de armazenamento de objetos.
- **Objects:** Arquivos ou dados armazenados dentro dos buckets.
- **Console:** Painel de controle para gerenciar buckets, usuários e visualizar logs de atividades.

## Passo 3: Criando Buckets Necessários para o Projeto

Neste passo, além de criar um bucket para armazenar os arquivos de dados, você também criará outros dois buckets essenciais para o funcionamento do projeto: "warehouse" e "scripts".

### 3.1. Criando um novo bucket

1. Clique no botão "Create Bucket" no canto superior direito da interface.
2. Escolha um nome para o seu bucket. Siga este procedimento para criar os três buckets necessários:
   - Bucket 1: "meus-dados" (para arquivos CSV e dados brutos)
   - Bucket 2: "warehouse" (para armazenamento de dados processados ou estruturados)
   - Bucket 3: "scripts" (para armazenar scripts e arquivos de código, como arquivos `process_ecommerce_data.py`)
3. Clique em "Create Bucket" para finalizar cada um.

Agora, os buckets "meus-dados", "warehouse" e "scripts" estão prontos para uso.

## Passo 4: Fazendo Download de Arquivos do Kaggle

Neste passo, você irá acessar o Kaggle, baixar o dataset de e-commerce brasileiro, descompactar e fazer upload dos arquivos para o MinIO.
Sobre o dataset: [Brazilian E-Commerce Public Dataset](Brazilian%20E-Commerce%20Public%20Dataset.md)

### 4.1. Acessando e baixando o dataset do Kaggle

1. Acesse o link do dataset do Kaggle: [Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
2. Se você ainda não está logado no Kaggle, faça login com sua conta.
3. Na página do dataset, clique no botão "Download" para baixar o arquivo `brazilian-ecommerce.zip`.

### 4.2. Descompactando o arquivo

1. Após o download, localize o arquivo `brazilian-ecommerce.zip` no seu sistema.
2. Descompacte o arquivo usando um gerenciador de arquivos (como o 7-Zip, WinRAR ou o gerenciador de arquivos nativo do seu sistema).
3. A pasta descompactada conterá vários arquivos CSV relacionados ao dataset de e-commerce.

## Passo 5: Fazendo Upload da Pasta e Scripts para o MinIO

### 5.1. Preparando o Upload

Certifique-se de que a pasta descompactada e o arquivo `process_ecommerce_data.py` estão prontos para serem enviados para o MinIO.

### 5.2. Upload dos arquivos CSV para o bucket "meus-dados"

1. Acesse o bucket "meus-dados" através da aba “Object Browser”.
2. Clique no botão "Upload Files" na parte superior.
3. Selecione “Upload Folder” para fazer upload da pasta descompactada que contém os arquivos CSV.
4. Clique em "Browse" e selecione a **pasta descompactada** que contém os arquivos CSV.
5. Após selecionar a pasta, clique em "Upload" para enviar todos os arquivos para o bucket "meus-dados".

### 5.3. Upload do arquivo `process_ecommerce_data.py` para o bucket "scripts"

1. Acesse o bucket "scripts".
2. Clique no botão "Upload Files".
3. Selecione o arquivo `process_ecommerce_data.py` localizado na pasta `Assistent/Project/code/app/`.
4. Após selecionar o arquivo, clique em "Upload" para enviá-lo para o bucket "scripts".

### 5.4. Verificando o Upload

Após o upload, os arquivos CSV aparecerão listados dentro do bucket "meus-dados", e o arquivo `process_ecommerce_data.py` estará no bucket "scripts". Você pode clicar no nome de cada arquivo para ver suas propriedades ou baixá-los novamente.

## Passo 6: Gerenciando Arquivos no MinIO

### 6.1. Excluindo arquivos

- Para excluir um arquivo, selecione o arquivo desejado e clique em "Actions" -> "Delete".

## Passo 7: Integração com Aplicações Externas

O MinIO pode ser facilmente integrado com aplicações que utilizam a API do S3, como ferramentas de análise de dados e pipelines de ETL.

### 7.1. Gerando credenciais de acesso

Para permitir que outras aplicações acessem seu bucket, você pode gerar novas credenciais (Access Key e Secret Key) através do painel de usuários na interface do MinIO.

## Conclusão

Você concluiu o módulo de introdução ao MinIO! Agora, você está familiarizado com a interface do MinIO, sabe como criar buckets e fazer upload de arquivos, e entende como gerenciar seus dados no ambiente de armazenamento de objetos. Além disso, configurou os buckets "warehouse" e "scripts", essenciais para o funcionamento do projeto, e fez o upload do arquivo `process_ecommerce_data.py` necessário.

Continue explorando outras funcionalidades do MinIO e veja como ele pode ser integrado em seu fluxo de trabalho de Big Data.
