# Desafio 1: Containers em Rede

Este projeto implementa dois containers distintos que se comunicam através de uma rede Docker customizada (Bridge Network). O objetivo é demonstrar o funcionamento da resolução de nomes (DNS interno do Docker), onde um container "Client" consegue enviar requisições HTTP para um container "Server" utilizando apenas o seu nome, sem a necessidade de IPs estáticos.

## Como Executar o Projeto
Certifique-se de ter o Docker instalado e rodando em sua máquina.

Acesse a pasta do desafio:

```
cd desafio-1
```

### 1. Criar a Rede Docker
Para que os containers se enxerguem pelo nome, é necessário criar uma rede bridge customizada.

```
docker network create rede-desafio1
```

### 2. Construir as Imagens
Construa as imagens do servidor (Python/Flask) e do cliente (Alpine/Curl).

```
# build do Server
docker build -t img-server ./server

# build do Client
docker build -t img-client ./client
```

### 3. Subir os Containers
Execute os containers conectando-os à rede criada.

**Passo 1: Iniciar o Servidor**
Nós definimos o nome `--name servidor-web`. Esse será o "domínio" que o cliente usará.

```
docker run -d --network rede-desafio1 --name servidor-web img-server
```

**Passo 2: Iniciar o Cliente**
O cliente executará um script em loop tentando acessar `http://servidor-web:8080`.

```
docker run -d --network rede-desafio1 --name cliente-curl img-client
```

### 4. Validar o Funcionamento
Para confirmar que a comunicação está ocorrendo, verificamos os logs do cliente.

```
docker logs -f cliente-curl
```
![log0client](https://github.com/user-attachments/assets/94d6d2f1-df7f-47f5-9600-57a9db50f083)

*Você deverá ver mensagens como: "Olá! A requisição chegou no container..."*

#

## Tecnologias Usadas
* **Engine**: Docker
* **Linguagem Server**: Python (Flask)
* **Linguagem Client**: Shell Script (Curl)
* **SO Base**: Alpine Linux
