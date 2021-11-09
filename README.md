# Locust Demo

Esse projeto é um "hello world" da biblioteca Locust, biblioteca Python usada em testes de carga.

## Execução dos testes
Temos dois testes, ambos bem simples:
- Teste de uma API REST;
- Teste de um e-commerce.

Para executar os testes é necessário que tenha instalado [Docker](https://docs.docker.com/engine/install/ubuntu/) e 
[docker-compose](https://docs.docker.com/compose/install/). Caso tenha o [make](https://guialinux.uniriotec.br/make/) instalado
pode usar os atalhos do arquivo Makefile que acompanha o projeto.

### Teste da API
```bash
docker-compose up api_test
```

### Teste do e-commerce
```bash
docker-compose up havan_test
```

Quando executar algum dos comandos acima, o Locust subirá um [servidor](http://0.0.0.0:8089/) na porta 8089, 
onde será possível parametrizar os testes, com a quantidade total de usuários e a taxa de crescimento dos usuários.

## Links:
- [Documentação](http://docs.locust.io/en/stable/index.html)
- [Site](https://locust.io/)
