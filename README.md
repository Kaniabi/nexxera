# Nexxera Nix

Esta é o protótipo de solução a "avaliação situacional backend" enviada
pela Nexxera como teste para a vaga de desenvolvedor BackEnd.


# Notas:

* Tomei a liberdade de fazer todo o sistema em inglês, inclusive os
campos dos banco de dados. Em um caso real isso deveria se acoplar as
necessidades de linguagem do cliente e do banco de dados.

* Foram feitos apenas testes de API, sem nenhum teste unitário.
Pessoalmente acredito que os testes de alto nível dão mais valor do que
testes unitários e por isso priorizei eles. Com o devido tempo pode-se
adicionar testes unitários a medida que eles sejam necessários.


# Instalação

### Baixa o código do repositório

```
$ git clone github.com/kaniabi/nexxera
```


### Criar um ambiente virtual

Nota: Estou usando o virtualenvwrapper, mas pode-se criar o ambiente
virtual com a ferramenta que estiver disponível.

```
$ mkvirtualenv -p python3 nexxera-nix
```


### Instalar dependências

```
$ cd nexxera/nix
$ pip install -r requirements.txt
```


### Rodar os testes (com coverage)

Os testes de API se encontram no arquivo:

* `nexxera/nix/_tests/test_nix.tavern.yml.`

```
$ pytest --cov nexxera --cov-report=term-missing
```
