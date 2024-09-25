## Apache Zeppelin

### 1. Pré-requisitos do Lab

- **Docker Preparado**: Certifique-se de que o Docker está instalado e em funcionamento.
- **Java JDK**: Instale o Java Development Kit (JDK) 8 ou superior.
- **Tecnologias Adjacentes e suas Versões**:
  - Apache Zeppelin: 0.9.0
  - Docker: Compatível com seu sistema operacional
  - Java JDK: 8 ou superior
- **Dados Mocks**: Prepare conjuntos de dados de teste que serão utilizados nos notebooks do Zeppelin.
- **Emulação de Network**: Configuração de rede que simule um ambiente de produção.
- **Chocolatey**: Certifique-se de que todos os pré-requisitos necessários estão liberados no nosso chocolatey, como:
  - openjdk8
  - docker

### 2. Como Fazer o Setup

#### Variáveis de Ambiente

Adicione as seguintes variáveis de ambiente:

```bash
export ZEPPELIN_PORT=8080
export JAVA_HOME=/path/to/java
export PATH=$PATH:$JAVA_HOME/bin
```

#### Especificação de Portas

- **Zeppelin**: 8080

#### Inicialização

Baixe e execute o Docker container do Zeppelin:

```bash
docker pull apache/zeppelin:0.9.0
docker run -d -p 8080:8080 --name zeppelin apache/zeppelin:0.9.0
```

### 3. Descrição dos Passos do Lab

#### Objetivo do Lab

Configurar e utilizar o Apache Zeppelin para criar e compartilhar relatórios baseados em dados.

#### Passo a Passo

1. **Preparar Ambiente**:

   - **Instalação do Docker**:

     - No Windows: Utilize o Chocolatey para instalar o Docker.
       ```bash
       choco install docker-desktop
       ```
     - No Linux: Siga as instruções da distribuição para instalar o Docker.
       ```bash
       sudo apt-get update
       sudo apt-get install docker-ce docker-ce-cli containerd.io
       ```
     - No macOS: Utilize o Homebrew para instalar o Docker.
       ```bash
       brew cask install docker
       ```

   - **Configuração do Java JDK**:
     - Baixe e instale o JDK 8 ou superior.
     - Configure a variável de ambiente `JAVA_HOME` para apontar para a instalação do JDK.
     - Adicione o diretório `bin` do JDK ao `PATH`.

2. **Configurar Zeppelin**:

   - **Definição de Variáveis de Ambiente**:

     - Configure a variável de ambiente `ZEPPELIN_PORT` para especificar a porta em que o Zeppelin será executado.
     - Certifique-se de que o `JAVA_HOME` está configurado corretamente.

   - **Verificação da Especificação de Portas**:
     - Garanta que a porta 8080 está disponível e não está sendo usada por outros serviços.

3. **Inicializar Zeppelin**:

   - **Baixar e Executar o Docker Container**:
     - Utilize o comando Docker para baixar a imagem do Zeppelin e iniciar o container.
     ```bash
     docker pull apache/zeppelin:0.9.0
     docker run -d -p 8080:8080 --name zeppelin apache/zeppelin:0.9.0
     ```
   - **Verificar a Inicialização**:
     - Verifique se o container está em execução utilizando o comando:
     ```bash
     docker ps
     ```

4. **Criar Notebooks**:
   - **Acesso à Interface Web do Zeppelin**:
     - Abra um navegador e acesse `http://localhost:8080`.
   - **Criação de Notebooks**:
     - Clique em "Create new note" para criar um novo notebook.
     - Dê um nome ao notebook e selecione o interpretador (por exemplo, Apache Spark) a ser utilizado.
   - **Execução de Códigos e Visualizações**:
     - Insira comandos e scripts nos diferentes blocos do notebook e execute-os.
     - Utilize as funcionalidades de visualização de dados do Zeppelin para criar gráficos e tabelas interativas.
   - **Compartilhamento de Notebooks**:
     - Utilize a funcionalidade de compartilhamento para permitir que outros usuários acessem e colaborem nos notebooks criados.

### 4. Resultados Esperados

- **Ambiente Zeppelin Funcionando**: O Apache Zeppelin deve estar acessível na porta 8080.
- **Criação e Compartilhamento de Notebooks**:
  - Capacidade de criar notebooks interativos.
  - Visualização de dados através de gráficos e tabelas.
  - Compartilhamento de notebooks com outros usuários para colaboração.
- **Integração com Outras Ferramentas da Sandbox**:
  - Conectividade e interação com outras ferramentas como Apache Hive, Apache Spark, e MinIO, permitindo a execução de consultas e scripts que envolvam múltiplas tecnologias.
  - Capacidade de utilizar dados armazenados no MinIO, executar jobs no Apache Spark, e consultar tabelas no Apache Hive diretamente a partir do Zeppelin.
  - Implementação de workflows complexos que integrem diferentes componentes da sandbox, demonstrando a flexibilidade e interoperabilidade do Zeppelin.

---

### 5. Fale Comigo

- **Nome**: Vinicius Antunes Silva
- **Email**: vinicius.antunes@2rpnet.com
- **GitHub**: https://github.com/viniciusantunes26

---

Se precisar de mais alguma coisa ou de outra ferramenta, por favor, me avise!
