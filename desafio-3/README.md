# Desafio 3: Docker Compose Orquestrando Serviços
Este projeto demonstra a orquestração de múltiplos serviços dependentes utilizando **Docker Compose**. O objetivo é subir uma stack completa composta por uma aplicação Web (Flask), um Cache (Redis) e um Banco de Dados (PostgreSQL) com apenas um comando, garantindo que as dependências e a rede interna sejam configuradas automaticamente via arquivo YAML.

## Como Executar o Projeto
É necessário ter o Docker e o Docker Compose instalados na sua máquina.

Acesse a pasta do desafio:

```
cd desafio-3
```

### 1. Subir a Stack (Build e Execução)
Diferente dos desafios anteriores, não precisamos construir a imagem manualmente e depois rodar. O Docker Compose faz tudo junto. O parâmetro `--build` garante que qualquer alteração no código Python seja recompilada.

```
docker-compose up --build
```

### 2. Validar a Aplicação
Após o terminal indicar que os serviços (web, db, cache) foram iniciados, abra o seu navegador.

1. Acesse o endereço: `http://localhost:5000`
2. **Resultado Esperado**: Você verá uma página HTML simples exibindo:
    * O número de acessos (contado pelo **Redis**).
    * O status da conexão com o banco de dados (**PostgreSQL**).

![log4](https://github.com/user-attachments/assets/5049493b-d76e-4ffa-9df0-0df22227b37e)

3. **Teste de Persistência/Cache**: Atualize a página (F5) várias vezes. O contador de acessos deve subir (1, 2, 3...), provando que o container Python está se comunicando com o container Redis e mantendo o estado.

![log5](https://github.com/user-attachments/assets/1d1b9bab-3b81-440f-994d-a4af9ba2459a)

### 3. Parar a Aplicação
Para encerrar a execução e remover os containers criados pelo Compose, utilize o comando:

```
docker-compose down
```

## Tecnologias Usadas
* **Orquestrador**: Docker Compose
* **Linguagem**: Python (Flask)
* **Banco de Dados**: PostgreSQL 13
* **Cache**: Redis Alpine
* **Conceito-Chave**: Service Orchestration & Dependency Management
