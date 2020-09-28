# App for data science with API REST / Django Rest Framework

API criada em Django Rest Framework para realizar o upload de arquivo de textos.

Em conjunto aplicação para criação de vocabulários formados pelas palavras dos textos recebidos da API. Criado um vetor para armazenar as palavras mais citadas e mostrando a quantidade de vezes que a mesma foi identificada. 

Todo o projeto foi desenvolvido utilizando o PyCharm. Mas para sua execução pode-se utilizar alguma IDE de sua preferência.

A estrutura para criação do vocabulário foi baseada no algoritmo Map Reduce originado do Google e utilizado em outros sistemas.

Map: É aplicado uma função para cada elemento da lista e pode ser executado de forma paralela, nesse caso contando o número de palavras em uma coleção de ducumentos.
Reduce: Funçao de agrupamento, aplicado em um conjunto de dados reduzindo para um simples valor.

## Iniciando

Essas instruções fornecerão uma cópia do projeto instalado e funcionando em sua máquina local, seque alguns requisitos para sua execução.

## Pré-requisitos

O que você precisa para executar o projeto:

* Python 3.x
* Mincemeat
* Algumas bibliotecas Python

## Instalando 

Todas as biblioteca utilizadas estão no arquivo requirements.txt.

Execute:
```
pip install -r requirements.txt
```

### Mincemeat 

Mincemeat é uma implementação Python para utilizar uma estrutura de computação distribuída MapReduce.

[Você pode encontrar instruções de instalação no repositório oficial.](https://github.com/michaelfairley/mincemeatpy)


## Executando o código

Para execução da API:

```
python manage.py runserver
```

### Rotas para acesso a API pelo browser ou alguma aplicação de conexão:

```
http://127.0.0.1:8000/api/v1/text/
```

### Executando a app para geração dos vocabulários:

Abra dois terminais para as execuções. Navegue até a pasta que contém o arquivo `vectors.py`

No primeiro terminal entre com o comando:

```
python vectors.py
```

No segundo terminal entre com o comando: 

```
python mincemeat.py -p changeme localhost
```

Será criado um arquivo .csv com os resultados na pasta `media`
