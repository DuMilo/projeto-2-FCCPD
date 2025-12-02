# Desafios Docker: Orquestração e Microsserviços
Este repositório reúne a resolução de 5 desafios focados em Docker. O projeto aborda desde conceitos fundamentais, como redes bridges customizadas e persistência de dados com volumes, até arquiteturas mais complexas envolvendo orquestração com Docker Compose e implementação de microsserviços com API Gateway.

O objetivo é demonstrar o domínio sobre o ciclo de vida de aplicações containerizadas e a comunicação entre serviços distribuídos.

## Estrutura dos Desafios
O repositório está dividido em pastas independentes, cada uma contendo sua própria solução:

* **Desafio 1 (Redes)**: Comunicação entre containers isolados via DNS interno.
* **Desafio 2 (Persistência)**: Uso de Volumes e Bind Mounts para persistência de dados (SQLite).
* **Desafio 3 (Orquestração)**: Aplicação completa (App + Banco + Cache) gerenciada via Docker Compose.
* **Desafio 4 (Microsserviços)**: Comunicação HTTP entre serviços independentes (Node.js e Python).
* **Desafio 5 (API Gateway)**: Arquitetura com ponto único de entrada protegendo os serviços internos.

## Como Executar o Projeto
É necessário ter o **Docker** e o **Docker Compose** instalados na sua máquina.

Clone o repositório:

```
git clone https://github.com/DuMilo/projeto-2-FCCPD.git
```
## Executando um desafio específico
Cada desafio possui seu próprio `Dockerfile` ou `docker-compose.yml`. Para rodar, entre na pasta correspondente e execute o comando de subida.

**Exemplo (Desafios com Compose - 3, 4 e 5):**

1. Entre na pasta do desafio:

```
cd desafio-3
```

2. Suba a aplicação (o flag `--build` garante a recriação das imagens):

```
docker-compose up --build
```
## Para os Desafios Manuais (1 e 2):
Estes desafios utilizam comandos `docker run` diretos para fixar conceitos. Consulte o `README.md` dentro de cada pasta para os comandos exatos de criação de rede e montagem de volume.

## **Boas práticas e dicas**
* **Isolamento de Rede**: Nos desafios de microsserviços, utilizei redes internas (`expose`) em vez de mapeamento de portas (`ports`) para os serviços de backend, forçando o acesso apenas pelo Gateway.
* **Persistência**: Ao testar o Desafio 2, observe que utilizamos a flag `--rm` para remover o container após o uso, provando que o arquivo `.db` persiste no host local independente do container.
* **Variáveis de Ambiente**: Credenciais e configurações sensíveis foram desacopladas do código (12-Factor App) e injetadas via `docker-compose.yml`.
* **Imagens Leves**: Preferência por imagens base `alpine` e `slim` para reduzir o tamanho final e o tempo de build.

#

## Tecnologias Usadas
* **Containerização**: Docker, Docker Compose
* **Linguagens**: Python, Node.js
* **Frameworks Web**: Flask (Python), Express (Node.js)
* **Banco de Dados & Cache**: PostgreSQL, SQLite, Redis
* **Bibliotecas**: Requests (Python), Axios (Node.js), Psycopg2
