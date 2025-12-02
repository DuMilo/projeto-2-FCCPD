# Desafio 5: Microsserviços com API Gateway
Este projeto implementa o padrão de arquitetura **API Gateway** centralizando o acesso a microsserviços. O objetivo é criar um ponto único de entrada (Gateway em Node.js) que recebe as requisições externas e as roteia para os serviços de backend apropriados (Users e Orders em Python).

Uma característica fundamental desta implementação é a segurança via isolamento de rede: os microsserviços de dados não expõem portas para a máquina host, sendo acessíveis apenas internamente pelo Gateway.

## Como Executar o Projeto
É necessário ter o Docker e o Docker Compose instalados na sua máquina.

Acesse a pasta do desafio:

```
cd desafio-5
```

### 1. Subir a Stack
Utilizamos o `docker-compose` para orquestrar o Gateway e os dois microsserviços simultaneamente. Note que apenas a porta `8080` (Gateway) está mapeada para o seu computador.

```
docker-compose up --build
```

### 2. Validar o Gateway
O teste consiste em fazer requisições para o Gateway e verificar se ele traz os dados dos serviços ocultos.

![gateway](https://github.com/user-attachments/assets/2a51a63a-f235-430b-9528-8b0f689ffc62)

1. **Rota de Usuários**: Acesse `http://localhost:8080/users`.
    * **Resultado**: JSON contendo a lista de usuários (vindo do container `users-service`).
  
![users](https://github.com/user-attachments/assets/3f432463-cb90-469f-9c7a-dbc280cfb495)

2. **Rota de Pedidos**: Acesse `http://localhost:8080/orders`.
    * **Resultado**: JSON contendo a lista de pedidos (vindo do container `orders-service`).

![orders](https://github.com/user-attachments/assets/32041e89-9f2d-4331-8555-120f244d0ef3)

### 3. Teste de Segurança (Isolamento)
Para provar que o Gateway é a única entrada:

1. Tente acessar diretamente o serviço de usuários: `http://localhost:5001/users`.
2. **Resultado Esperado**: O navegador deve exibir "Falha na conexão" ou "Não foi possível conectar". Isso ocorre porque utilizamos a diretiva `expose` no Docker Compose (rede interna) ao invés de `ports`, garantindo o encapsulamento.

![gatewayapenas](https://github.com/user-attachments/assets/ed412adc-0c5e-4c3b-bc32-422b6d8d826a)

### 4. Parar a Aplicação
Para encerrar a execução e remover a infraestrutura:

```
docker-compose down
```

#
 
## Tecnologias Usadas
* **Orquestrador**: Docker Compose
* **Gateway**: Node.js (Express + Axios)
* **Microsserviços**: Python (Flask)
* **Conceito Chave**: API Gateway Pattern & Network Isolation
