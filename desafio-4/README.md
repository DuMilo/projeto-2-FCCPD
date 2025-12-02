# Desafio 4: Microsserviços Independentes
Este projeto implementa uma arquitetura de **Microsserviços Poliglotas**. O objetivo é criar dois serviços independentes (desenvolvidos em linguagens diferentes) que se comunicam via protocolo HTTP dentro da rede interna do Docker. O **Service A (Node.js)** atua como uma API provedora de dados, enquanto o **Service B (Python)** consome esses dados e gera um relatório formatado para o usuário final.

## Como Executar o Projeto
É necessário ter o Docker e o Docker Compose instalados na sua máquina.

Acesse a pasta do desafio:

```
cd desafio-4
```

### 1. Subir a Stack
Neste desafio, utilizamos o `docker-compose` para construir as imagens de ambos os serviços e conectá-los na mesma rede automaticamente.

```
docker-compose up --build
```

### 2. Validar a Comunicação
O teste consiste em acessar o serviço consumidor (Service B) e verificar se ele conseguiu buscar os dados no Service A.

1. **Acessar no Navegador**: Abra o endereço `http://localhost:5000`.
2. **Resultado Esperado**: Você verá uma página HTML intitulada "Relatório de Usuários". Os dados exibidos **não** estão no código do Python; eles foram obtidos via requisição HTTP ao Node.js.

![log6](https://github.com/user-attachments/assets/0433a2ca-b301-413d-967c-f89b80de6cf2)

3. **Verificar Logs**: No terminal onde o Docker está rodando, observe os logs.
    * O **Service B** (Python) registrará a saída da requisição.
    * O **Service A** (Node) registrará: `[Service A] Recebi uma requisição em /users`.

![log7](https://github.com/user-attachments/assets/8adf2faa-d893-4b69-b652-d7d41e7a6794)

### 3. Parar a Aplicação
Para encerrar a execução e remover os containers:

```
docker-compose down
```

#
 
## Tecnologias Usadas
* **Orquestrador**: Docker Compose
* **Serviço A**: Node.js (Express) - API REST
* **Serviço B**: Python (Flask + Requests) - Cliente HTTP
* **Conceito Chave**: Comunicação HTTP entre Containers & Arquitetura Poliglota
