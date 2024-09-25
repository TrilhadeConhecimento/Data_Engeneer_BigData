[Início](../README.md)

# Preparação do ambiente

## Instalação

Siga os passos abaixo para instalar o projeto:

1. Clone este repositório para o seu ambiente local.

```bash
git clone https://github.com/TrilhadeConhecimento/Data_Engeneer_BigData.git

```

1. Navegue até o diretório do projeto.

```bash
cd Assistent/Project
```

1. Execute o comando de inicialização do Docker.

```bash
docker compose up --build

```

## Configuração

Após a instalação, o ambiente será configurado automaticamente. Você pode acessar os seguintes serviços:

- Zeppelin: [http://localhost:8080](http://localhost:8080/)
- MinIO: [http://localhost:9001](http://localhost:9001/)
- Livy-Spark: [http://localhost:18080](https://localhost:18080)
- Metastore: [http://localhost:9083](http://localhost:9083)
- HiveServer: [http://localhost:10002](http://localhost:10002)

## Iniciar / Parar

Depois que o projeto estiver instalado, não é mais necessário instala-lo novamente, ao invés disso, usar os seguintes comandos

```bash
docker compose start
```

```bash
docker compose stop
```

## Solução de Problemas

Se os serviços não estiverem funcionando conforme o esperado, siga estes passos de solução de problemas:

1. Certifique-se de que o Docker está em execução.
2. Verifique os logs dos contêineres para mensagens de erro.
3. Reinicie os contêineres usando o comando:

   ```bash
   docker compose restart
   ```
