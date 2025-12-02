# Desafio 2: Volumes e Persistência de Dados
Este projeto demonstra a persistência de dados em containers Docker utilizando **Bind Mounts**. O objetivo é comprovar que o ciclo de vida dos dados pode ser desacoplado do ciclo de vida do container. Para isso, utilizamos um script Python que manipula um banco de dados SQLite; os dados são gravados dentro do container, mas armazenados fisicamente no host, sobrevivendo à destruição do container.

## Como Executar o Projeto
É necessário ter o Docker instalado na sua máquina.

Acesse a pasta do desafio:

```
cd desafio-2
```

### 1. Construir a Imagem
Primeiro, criamos a imagem da aplicação que contém o script de manipulação do banco de dados.

```
docker build -t img-persist ./app
```

### 2. Executar o Container (Com Persistência)
Para que a persistência funcione, precisamos mapear uma pasta do seu computador para dentro do container usando a flag `-v`.

**Para Windows (CMD):**

1. Utilize a variável `%cd%` para pegar o diretório atual.
2. Execute o comando abaixo. Note a flag `--rm`, que deleta o container assim que ele termina (para provar que o dado não ficou na memória do container).

```
docker run --rm -v "%cd%\dados:/data" img-persist
```

**Para Linux / macOS / PowerShell:**

1. Utilize `$(pwd)` ou `${PWD}` para o caminho atual.

```
docker run --rm -v "$(pwd)/dados:/data" img-persist
```

### 3. Validar a Persistência
O teste consiste em rodar o comando acima **duas vezes**.

1. **Primeira Execução**: O log informará que o banco não existia e foi criado. Um arquivo `.db` aparecerá na sua pasta `dados` local.

![log2](https://github.com/user-attachments/assets/172fe599-380d-4d2c-b83a-8c1ff4e7e1ec)

2. **Segunda Execução**: O log informará que "Banco de dados existente encontrado" e listará os registros anteriores, provando que o dado persistiu.

![log3](https://github.com/user-attachments/assets/65111b80-639a-4ada-b995-278adc6d3206)

#
 
## Tecnologias Usadas
* **Engine**: Docker
* **Linguagem**: Python
* **Banco de Dados**: SQLite3 (Nativo)
* **Conceito Chave**: Docker Volumes (Bind Mount)
