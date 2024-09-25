[Voltar ao módulo 3](../Módulo%203%20Apache%20Airflow%20+%20Hive.md)

# Ciclo de Vida da Task

No Apache Airflow, o ciclo de vida de uma task é o conjunto de estados pelos quais uma task passa durante sua execução. Compreender esses estados ajuda a diagnosticar problemas, otimizar workflows e garantir a execução eficiente das tarefas.

```mermaid
**stateDiagram-v2
    [*] --> None
    None --> Scheduled : Task agendada pelo Scheduler
    Scheduled --> Queued : Task enfileirada para execução
    Queued --> Running : Task em execução
    Running --> Success : Task executada com sucesso
    Running --> Failed : Task encontrou erro irreparável
    Failed --> Up_for_Retry : Task configurada para retry
    Up_for_Retry --> Queued : Task re-enfileirada para execução
    Running --> Deferred : Task aguardando condição externa (assíncrono)
    Failed --> Upstream_Failed : Dependência falhou
    Scheduled --> Skipped : Task propositalmente ignorada
    [*] --> Removed : Task removida da DAG
    Removed --> Restored : Task reintegrada na DAG
    Running --> Shut_Down : Airflow interrompido durante execução**

```

### 1. **None**

- **Descrição**: Quando uma task é definida dentro de uma DAG, mas ainda não foi agendada ou iniciada, seu estado é `None`. Nesse estado, a task existe apenas como parte da definição do pipeline e não foi avaliada pelo scheduler.
- **Significado**: A task ainda não foi considerada para execução.

### 2. **Scheduled**

- **Descrição**: O estado `scheduled` ocorre quando o scheduler do Airflow determina que a task deve ser executada com base na lógica da DAG e em suas dependências.
- **Significado**: A task foi agendada e está aguardando a execução. As dependências da task foram atendidas, mas ela ainda não começou a ser processada.

### 3. **Queued**

- **Descrição**: No estado `queued`, a task está na fila para ser executada. Isso acontece quando o scheduler enfileira a task para o executor, mas a task ainda não começou a rodar.
- **Significado**: A task foi atribuída a um executor, mas está aguardando recursos ou a sua vez na fila de execução.

### 4. **Running**

- **Descrição**: Quando uma task está efetivamente sendo executada, seu estado muda para `running`. Nesse estado, o executor está processando a task.
- **Significado**: A task está ativa, executando a operação que foi programada (por exemplo, rodando um script Python, executando um comando Bash, etc.).

### 5. **Success**

- **Descrição**: O estado `success` indica que a task foi concluída com êxito. A task realizou todas as operações sem encontrar erros.
- **Significado**: A task terminou com sucesso, e o fluxo de execução pode continuar para as próximas tarefas na DAG que dependem dessa task.

### 6. **Failed**

- **Descrição**: Se a task encontrar um erro irrecuperável durante sua execução, seu estado mudará para `failed`. Isso pode acontecer devido a falhas no código, erros de configuração, problemas com recursos externos, entre outros.
- **Significado**: A task não conseguiu ser concluída com êxito. Dependendo da configuração da DAG, isso pode interromper o workflow ou acionar políticas de retry.

### 7. **Up for Retry**

- **Descrição**: Quando uma task falha, mas está configurada para tentar novamente (retry), ela entra no estado `up_for_retry`. O Airflow aguardará um tempo pré-definido antes de tentar executar a task novamente.
- **Significado**: A task falhou, mas uma nova tentativa de execução será feita após o tempo de espera especificado.

### 8. **Upstream Failed**

- **Descrição**: Se uma task depende de outra task que falhou, seu estado pode ser `upstream_failed`, significando que a task não será executada porque uma de suas tarefas predecessoras falhou.
- **Significado**: A task não será executada porque uma de suas dependências falhou.

### 9. **Skipped**

- **Descrição**: O estado `skipped` ocorre quando a task foi programada para ser pulada. Isso pode acontecer por várias razões, como uma condição especificada no código que determina que a task não deve ser executada.
- **Significado**: A task foi propositalmente ignorada durante a execução da DAG, talvez por uma condição lógica que determinou que não era necessário executá-la.

### 10. **Deferred**

- **Descrição**: Um estado introduzido no Apache Airflow 2.3, o `deferred` indica que uma task está aguardando uma condição externa ou sensor para continuar. Esse estado é utilizado principalmente em contextos assíncronos.
- **Significado**: A task aguarda um evento ou condição externa para continuar a execução.

### 11. **Shut Down**

- **Descrição**: Se o Airflow é desligado de maneira abrupta durante a execução de uma task, essa task pode entrar no estado `shutdown`. Este estado indica que a execução foi interrompida antes que a task pudesse ser completada.
- **Significado**: A task foi interrompida devido a um encerramento inesperado do Airflow.

### 12. **Removed**

- **Descrição**: Quando uma task é removida de uma DAG, seu estado pode ser marcado como `removed`. Isso indica que a task não faz mais parte do workflow definido.
- **Significado**: A task não existe mais na definição atual da DAG.

### 13. **Restored**

- **Descrição**: Quando uma task que estava marcada como `removed` é adicionada de volta à DAG, ela entra no estado `restored`.
- **Significado**: A task foi reintegrada à definição da DAG e está pronta para ser agendada.

### 14. **Kicked Off**

- **Descrição**: No contexto de triggers em DAGs, uma task pode ser “kicked off”, ou seja, iniciada por um evento específico, como a chegada de um arquivo ou um horário programado.
- **Significado**: A task foi iniciada por um evento externo que ativou a DAG.

---

### Como Monitorar o Lifecycle das Tasks

A Web UI do Apache Airflow é a principal ferramenta para monitorar o ciclo de vida das tasks. Nela, você pode visualizar o estado atual de cada task, acessar logs detalhados de execução e obter insights sobre o desempenho e possíveis problemas no workflow. Ao entender o ciclo de vida das tasks, você pode antecipar problemas, ajustar configurações e otimizar seus workflows para uma execução mais eficiente.

Se precisar de mais detalhes ou tiver outras dúvidas, é só me avisar!

### Próximo Documento

- [DAG com Bash Operator](DAG%20com%20Bash%20Operator.md)
