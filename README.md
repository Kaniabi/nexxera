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

* A maioria das _features_ do sistema foram herdadas do
  `flask-restless`. Isso facilitou muito a criação de API REST padrão
  mas dificultou um pouco as customizações das APIs.


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


# Faltas

Infelizmente não consegui implementar alguns dos requisitos a tempo:

* Listagem por data: Na estrutura de dados original não existe um campo
  de timestamp. Isso deveria ser adicionado para poder fazer essa
  listagem.
  Além disso, para poder fazer os testes é necessário poder sobrescrever
  a data via chamada da API de modo que os testes não dependam da hora
  atual.

* Não foram feitos testes unitários, apenas um grande teste de API
  usando o `tavern`. Isso pode ser melhorado tanto adicionando testes
  unitários onde for interessante bem como organizando melhor os testes
  de API.

* Documentação da API. Iniciei o projeto usando o `connexion`, que cria
  a API a partir da documentação do OpenAPI. Essa implementação foi
  abandonada em favor do `flask-restless`. Com isso ainda existe uma
  documentação inicial, mas ela não reflete o código.
  A idéia seria gerar a documentação OpenAPI/Swagger a partir do
  flask-restless, mas não consegui tempo de testar o pacote que faz
  isso.

* A implemtação da deleção lógica tem problemas e deveria ser feita com
  mais cuidado e testes. Dependendo da motivação original podem existir
  outras soluções possíveis.
  O problema é que na implementação atual o sistema ignora os IDs dos
  items deletados usando eles novamente.
