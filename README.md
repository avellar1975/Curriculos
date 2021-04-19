![Django CI](https://github.com/avellar1975/Curriculos/workflows/Django%20CI/badge.svg)
[![Python 3](https://pyup.io/repos/github/avellar1975/Curriculos/python-3-shield.svg)](https://pyup.io/repos/github/avellar1975/Curriculos/)
[![Updates](https://pyup.io/repos/github/avellar1975/Curriculos/shield.svg)](https://pyup.io/repos/github/avellar1975/Curriculos/)
[![codecov](https://codecov.io/gh/avellar1975/Curriculos/branch/main/graph/badge.svg?token=32L3CQIY1P)](https://codecov.io/gh/avellar1975/Curriculos)

# Curriculos
Solução de Banco de Currículos

# Afiando o machado

<img src="/images/machado.jpg" width="100%">

Antes de iniciar a cortar as árvores (desenvolver de fato) é preciso preparar os ambientes que vamos construir os projetos.

## GIT

### Fazendo um clone do repositório remoto na máquina local

Há duas formas de clonar o repositório remoto na máquina local: via HTTPS ou SSH.

### 1. Para clonar via HTTPS:

No terminal basta digitar o comando <kbd>git clone</kbd> seguido da url:
```
$ git clone https://github.com/avellar1975/Curriculos.git
```
<p>A desvantagem de utilizar o protocolo HTTPS é que será solicitado usuário e senha a cada <kbd>push</kbd> de novos commits.</p>

### 2. Para clonar via SSH:

> As URLs de SSH fornecem acesso a um repositório do Git via SSH, um protocolo seguro. Para usar essas URLs, você deve gerar um par de chaves SSH no seu computador e adicionar a chave pública à sua conta de GitHub.

No terminal basta digitar o comando <kbd>git clone</kbd> seguido do recurso:
```
$ git clone git@github.com:avellar1975/Curriculos.git
```

#### 2.1 Gerar chave SSH:

No terminal digitar o comando abaixo com seu e-mail cadastrado no github:
```
$ ssh-keygen -t ed25519 -C "seu.email@gmail.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/usuario/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```
* Na opção do arquivo para salvar sua chave pode manter a sugerida apenas clicando no <kbd>ENTER</kbd> (caso você não tenha outra chave com o mesmo nome)
* Digitar uma senha e confirmar novamente a mesma senha
* Serão gerados dois arquivos no diretório .ssh/: <kbd>id_ed25519</kbd> e <kbd>id_ed25519.pub</kbd>.
* O conteúdo da chave pública que está no arquivo <kbd>id_ed25519.pub</kbd> deve ser cadastrado no github (clicando na foto do seu perfil > Settings > SSH and GPG Keys)

## Fork

No Github quando você clica em fork no repositório de alguém, ele pega o repositório completo dessa pessoa e copia para sua conta git, lá você poderá editar esses arquivos e depois devolver a essa pessoa com as suas edições, se a pessoa aceitar, suas alterações também entram no repositório dele.

Após clonar na máquina local, é possível adicionar o upstream com o comando <kbd>git remote add upstream https://github.com/outro_projeto/projeto.git</kbd>

<p>Para verificar o novo repositório <strong>upstream</strong> (original de onde você "bifurcou") que você especificou para sua bifurcação, digite novamente <kbd>git remote -v</kbd>. Você deverá visualizar a URL da sua bifurcação como origin (origem) e a URL do repositório original como upstream.

```
  $ git remote -v
> origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
> origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
> upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
> upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)

```

## Sobre branches

Use um branch para isolar o trabalho de desenvolvimento sem afetar outros branches no repositório. Cada repositório tem um branch padrão e pode ter vários outros branches. Você pode fazer merge de um branch em outro branch usando uma pull request.

Os branches permitem que você desenvolva recursos, corrija erros ou experimente com segurança novas ideias em uma área contida do seu repositório.

[Leia mais](https://docs.github.com/pt/github/collaborating-with-issues-and-pull-requests/about-branches#about-branches)

## Sobre pull requests

As pull requests permitem que você informe outras pessoas sobre as alterações das quais você fez push para um branch em um repositório no GitHub. Depois que uma pull request é aberta, você pode discutir e revisar as possíveis alterações com colaboradores e adicionar commits de acompanhamento antes que as alterações sofram merge no branch base.

## Sobre Issues

Use os **issues** para rastrear ideias, melhorias, tarefas ou bugs para trabalhar no GitHub.

Através do comentário close #x (sendo x o número da issue) no commit é possível fechar a issue caso o commit chegue na branch principal.

A mesma lógica pode ser usada para abrir um pull request.

---
## Ambientes virtuais e Pacotes

### 1. Pyenv

O que o pyenv nos oferece:
* Instalação do interpretador python usando o $HOME do usuário
* Instalação de várias versões diferentes do python, cada uma com seu diretório isolado

Para instalar o Pyenv:

- Instalar as libs de dependência:

```
$ sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm gettext libncurses5-dev tk-dev tcl-dev blt-dev libgdbm-dev git python-dev python3-dev aria2 vim libnss3-tools python3-venv liblzma-dev libpq-dev
```
- Instalar o pyenv:

```
$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

- Editar no .bashrc:

```
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
```

- Instalação de versão do python:

```
$ pyenv install <versao>
```

- Setando python global:

```
$ pyenv global <versao>
```

- Para verificar as versões instaladas:

```
$ pyenv versions
  system
  2.7.18
* 3.9.1 (set by /home/avellar/.pyenv/version)
```

### 2. Virtualenv
O virtualenv é uma ferramenta que cria um ambiente isolado de desenvolvimento Python com todas as bibliotecas e pacotes que são necessários para **um determinado projeto** sem que haja conflitos entre elas.

- Dentro da pasta do projeto:

```
$ python -m venv .venv
```

- Ativar o ambiente virtual venv:

```
$ source .venv/bin/activate
```
- Para desativar:

```
$ deactivate
```

### 3.PIP
Com o virtualenv ATIVADO instalar as bibliotecas que serão utilizadas no projeto através do comando:
```
$ pip install <nome_da_biblioteca>
```
- comando pip freeze permite listar todas as bibliotecas instaladas:

```
$ pip freeze
certifi==2020.12.5
chardet==4.0.0
idna==2.10
requests==2.25.1
urllib3==1.26.3
```

- **Requirements:**
O arquivo requirements.txt serve para manter suas libs fora do controlador de versão ao mesmo tempo que permite a outros desenvolvedores recriarem o projeto com respectivas dependências.

```
$ pip freeze > requirements.txt
```
É possível instalar todas as bibliotecas do arquivo requirements.txt através do comando:
```
$ pip install -r requirements.txt
```

## Flake8

Flake8 é um projeto que combina 3 ótimas ferramentas em um só pacote:

- Pep8 que verifica se o estilo do código respeita o padrão adotado pela comunidade descrito na Python Enhancement Proposal 8.
- PyFlakes que analisa estaticamente seu código detectando inúmeros anti-patterns e erros lógicos como módulos importados que não são utilizados, uso de variáveis não declaradas, entre muitas outras coisas.
- Codepaths que realiza a análise da complexidade ciclomática do código com base nas métricas de McCabe.

* Para instalar:

```
$ pip install flake8
```

* Criar arquivo .flake8:

```
[flake8]
exclude=.venv
```
Isso vai permitir para que o flake8 não analise a pasta .venv

* Para executar o Flake8 local basta digitar o comando:

```
$ flake8
```

## Integração Contínua com Git Actions

Na opção **Actions** ao lado de *Pull requests* clique na opção *Set up this workflow* no quadro **Python Applications**

<img src="/images/git-actions.png">

Com o arquivo de configuração aberto é possível alterar alguns parâmetros, por exemplo de quanto o CI será iniciado com um pull request na master ou um commit.

[![Django CI](https://github.com/avellar1975/Curriculos/actions/workflows/django.yml/badge.svg)](https://github.com/avellar1975/Curriculos/actions/workflows/django.yml)

Para inserir o badge referente à atualização do CI basta copiar o código conforme figura abaixo e colar no arquivo README:

<img src="/images/badges.png">

## Upgrade de Dependências com PyUp

Acessar o site https://pyup.io/ e fazer login com a conta do github.
Adicionar o Repositório do github no PyUp.
Clicando em cada um dos badges é possível copiar o código para colar no seu README.

## Testes Automáticos

* Instalar o pytest dentro da sua virtualenv:

```
$ pip install pytest
```
* Criar pasta <kbd>tests</kbd> dentro da pasta do projeto

```
$ mkdir tests
```
* Criar um módulo dentro da pasta com nome test_exemplos.py

Exemplo de código de uma função (na raiz do projeto) a ser testada:
```
""Função para implementar um testeself.

Recebe parm1 e parm2
retorna resultado
"""


def funcao_para_testar(parm1, parm2):
    """Retorna multiplicação de dois argumentos."""
    return parm1 * parm2

```

Exemplo do conteúdo do módulo test_exemplos.py:

```
from funcao import funcao_para_testar


def teste_basico():
    assert funcao_para_testar(3, 5) == 15


def teste_numeros_negativos():
    assert funcao_para_testar(-3, 9) == -27

```

* Na raiz do projeto executar o comando (parâmetro -v é o modo verbose):

```
$ pytest tests/ -v
```

### Configuração no CI para rodar os testes:

No arquivo de configuração do CI (yml) incluir o trecho abaixo:

```
    - name: Test with pytest
      run: |
        pytest tests -v
```

### Cobertura de testes

Instalar a biblioteca pytest-cov

```
$ pip install pytest-cov
```

- Para executar os testes com cobertura utilizar o comando onde myproj é o diretório dos códigos que serão testados, tests é o diretório onde estão os testes e o parâmetro -v roda o pytest em modo verbose:

```
pytest --cov=myproj tests/ -v
```

- Alterando o CI para também executar a cobertura de testes

No arquivo de configuração do CI (yml) incluir o trecho abaixo:

```
    - name: Test with pytest
      run: |
        pytest --cov=funcao tests -v
```

- Acessar o site https://codecov.io/, logar com sua conta do github e adicionar seu repositório.
- Adequar o arquivo yml com o conteúdo abaixo:

```
    - uses: codecov/codecov-action@v1
    - name: Codecov
      with:
        token: ${{ secrets.CODECOV_TOKEN }} # not required for public repos

```

Se precisar trabalhar com TOKEN do codecov precisa cadastrá-lo com o nome CODECOV_TOKEN no github em *Settings >> Secrets >> New repository secret*

## Pipenv
> Projeto que visa trazer o melhor de todos os mundos de embalagens para o mundo Python, utiliza: Pipfile , pip e virtualenv ;

Já falamos sobre o pip e virtualenv (venv), ficou faltando a definição do Pipfile.

O Pipfile é uma substituição para o arquivo requirements.txt do pip padrão existente. Ou seja o Pipenv está para o pip, assim como o Pipfile está para o requirements.

Através do parsing do Pipfile, a ferramenta resolve dependências do projeto (através dos parâmetros install, uninstall ou update), exibe a árvore de dependências (através do parâmetro graph) e analisa as mesmas (através do check). Mas além de atuar como um gerenciador de pacotes, o Pipenv tem uma funcionalidade fantástica: Cria e gerencia virtualenvs de forma automática.

Para atualizar local as dependências do projeto no virtualenv basta digitar o comando abaixo:

```
$ pipenv sync -d
```

# Início do projeto
<img src="https://www.mattlayman.com/img/python-django.png">

## Escolha da versão Python através do pyenv
```
$ pyenv install 3.9.1
$ pyenv global 3.9.1
```

## Mudar a configuração do Pipenv

- Instalar o pipenv:

```
$ pip install pipenv
```

- Editar o .bashrc incluindo a linha abaixo. Isso vai permitir alterar o comportamento do pipenv para que a pasta .venv seja criada na pasta do projeto.

```
export PIPENV_VENV_IN_PROJECT=1
```

- Atualizar as variáveis de ambiente:

```
$ source .bashrc
```

## Instalar o Django

- Clonar o projeto pelo Git;
- Se já tiver a pasta .venv criada pelo venv do python é preciso apagar a pasta para recriá-la com o pipenv;
- Instalar o Django com o pipenv dentro da pasta do projeto:

```
$ pipenv install Django
```

### Instalar o flake8 como biblioteca do ambiente de desenvolvimento

```
$ pipenv install --dev flake8
```

## Arquivo .pyup.yml (Adequação aos arquivos Pipfile)

```
requirements:
  - Pipfile
  - Pipfile.lock
```

## Primeira versão do arquivo yml de CI (GitHub Actions)

```
name: Django CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.9]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies with pipenv
      run: |
          pip install pipenv
          pipenv install --deploy --dev
    - run: pipenv run flake8
```

## Montar a estrutura do projeto Django

Dentro do ambiente virtual:

```
$ django-admin startproject curriculos .
$ python manage.py runserver
```

Já teremos aqui o servidor Django rodando

## Configuração do Heroku

- Para instalar o Heroku Command Line Interface (CLI)

```
$ curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
```

- Alterar no arquivo settings.py o parâmetro <kbd>ALLOWED_HOSTS = ['*']</kbd>
- Criar o arquivo Procfile na raiz do projeto com o conteúdo:

```
web: gunicorn curriculos.wsgi --log-file -
```

- Instalar a biblioteca gunicorn através do pipenv

```
$ pipenv install gunicorn
```

- Criando uma aplicação no heroku

```
$ heroku apps:create curriculosdjango
$ heroku config:set DISABLE_COLLECTSTATIC=1
$ git push heroku <branch local>:master -f
```

Agora é só acessar a *url* do heroku para verificar a primeira versão da aplicação rodando em produção.
> Url de produção: https://curriculosdjango.herokuapp.com/

## Deploy Automático
- Acessar o dashboard da aplicação no heroku;
- Na Aba Deploy, opção Connect to GitHub;
- Conecta ao repositório da aplicação no GitHub;
- Confirma a branch;
- Marca a opção "Wait for CI to pass before deploy";
- Clicar no botão "Enable Automatic Deploys"

## Criação da primeira APP do Django

Dentro da pasta curriculos executar o comando:

```
python ../manage.py startapp base
```

- Alterar o arquivo views.py na pasta base da app

```
from django.http import HttpResponse

def home(request):
    return HttpResponse('Olá Django')
```

- Alterar o arquivo settings.py (raiz)

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Minhas APPS
    'curriculos.base',
]
```

- Alterar o arquivo urls.py na pasta raiz

```
from curriculos.base.views import home
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
```


## Pytest Django
- Instalar a biblioteca no nosso ambiente pytest-django

```$ pipenv install -d 'pytest-django' ```

- Na raiz do projeto criar o arquivo pytest.ini com o seguinte conteúdo:

```
[pytest]
DJANGO_SETTINGS_MODULE = curriculos.settings
```
- Criar pasta tests dentro da pasta do app base e criar o arquivo test_home.py com o seguinte conteúdo:

```
from django.test import Client

def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200

```

- Pra executar os testes:

```
$ pipenv run pytest -v
```

- Alterar o arquivo yml com o comando ```pipenv run pytest -v```

## Cobertura de testes

- Instalação das bibliotecas

```
$ pipenv install -d 'pytest-cov' codecov
```
Após instalação é possível executar o comando abaixo:
```
pipenv run pytest -v --cov=curriculos

```
- Substituir a linha do arquivo yml de teste incluindo a Cobertura

```
- name: Execução dos testes
  run: pipenv run pytest -v --cov=curriculos

- name: Posting Coverage
  env:
    super_secret: ${{ secrets.CODECOV_TOKEN }}
  run: pipenv run codecov
```

### codecov.yml

Na documentação oficial do **codecov** é apresentado como ignorarmos arquivos e pastas na cobertura dos testes, criando um arquivo <kbd>codecov.yml</kbd>

Pois não faz sentido medirmos se estamos fazendo testes nas pastas e arquivos padrões do Django, por exemplo.

*You can use the top-level `ignore:` key to tell Codecov to ignore certain paths.*

*Add a list of paths (folders or file names) to your codecov.yml file under the ignore key to exclude files from being collected by Codecov. Ignored files will be skipped during processing.*

*codecov.yml*

```
ignore:
  - "path/to/folder"  # ignore folders and all its contents
  - "test_*.rb"       # wildcards accepted
  - "**/*.py"         # glob accepted
```

Veja como ficou meu arquivo para não varrer por exemplo as migrations e arquivo models.py:

```
ignore:
  - "minha_app/base/migrations/*" # ignore folders and all its contents
  - "minha_app/base/models.py"
```

Referência: https://docs.codecov.io/docs/ignoring-paths


## Python Decouple

Configurações que permitem trabalharmos com valores de variáveis de ambiente distintas para cada ambiente e não expor informações de segurança, como por exemplo a SECRET_KEY, permite desta forma desacoplar as configurações de instância da aplicação.

- Instalar a biblioteca

```
$ pipenv install python-decouple
```

- Importar a função config da biblioteca no arquivo settings.py

```
from decouple import config
```

- Criar o arquivo .env no diretório raiz, ele será ignorado no controle do .gitinore, e editar o arquivo settings.py nas seguintes linhas:

```
SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)
```
No arquivo .env deverá estar definidas as variáveis de ambiente:
DEBUG = True
SECRET_KEY = ************************************
Não utilizar aspas no arquivo .env

- Setar o valor da variáveis de ambiente de produção (heroku), uma vez que não passaremos mais este valor no controlador de versão git:

```
$ heroku config:set DEBUG=False
$ heroku config:set SECRET_KEY=************************************
```

- Criar uma pasta com nome <kbd>contrib</kbd> na raiz do projeto

- Editar o arquivo env-sample com instruções ao desenvolvedor, por exemplo <kdb>SECRET_KEY = digitar aqui a chave secreta</kbd>

- Inserir no arquivo de CI django.yml as seguintes linhas antes das instalações de dependencias:

```
- name: Copiar template de configuração do decouple
  run: cp contrib/env-sample .env
```


## Domínio customizado e ALLOWED_HOSTS

- Como configurar um domínio
https://devcenter.heroku.com/articles/custom-domains

- No arquivo settings.py:

```
from decouple import config, Csv

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
```

- No arquivo .env e contrib/env-sample:

```
ALLOWED_HOSTS=localhost,127.0.0.1
```

- Comando heroku:

```
$ heroku config:set ALLOWED_HOSTS='seudominio.com, subdominio.herokuapp.com'
```

## Configurando o Banco de Dados

- Instalar a bibliotecas

```
$ pipenv install dj-database-url

```

- Atualizar o settings.py

```
import os
from pathlib import Path
from decouple import config, Csv
from functools import partial
import dj_database_url

(...)

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

default_db_url = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

parse_database = partial(dj_database_url.parse, conn_max_age=600)

DATABASES = {
    'default': config('DATABASE_URL',
                      default=default_db_url,
                      cast=parse_database)
                      }


```

## Testando Postgresql no CI

- Instalar a biblioteca psycopg2-binary


```
$ pipenv install psycopg2-binary

```

- Configurar o arquivo yml do CI

```
# Service containers to run with `runner-job`
services:
  # Label used to access the service container
  postgres:
    # Docker Hub image
    image: postgres:13.2
    # Provide the password for postgres
    env:
      POSTGRES_PASSWORD: postgres
      POSTGRES_HOST: localhost
      POSTGRES_DB: testdb
    # Set health checks to wait until postgres has started
    options: >-
      --health-cmd pg_isready
      --health-interval 10s
      --health-timeout 5s
      --health-retries 5
    ports:
      # Maps tcp port 5432 on service container to the host
      - 5432:5432
```

## Lingua e Fuso Horário

- Arquivo settings.py

```
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'
```

## Arquivos Estáticos

- Alterar o arquivo de settings.py

```
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
```

- Executar o comando:

```
$ python manage.py collectstatic
```

### Usuário na AWS

- No AWS Management Console acessar o serviço IAM
- Em Usuários clicar em adicionar Usuário
- Tipo de acesso: "Acesso programático"
- Na opção "Anexar políticas existentes e forma direta" selecionar AmazonS3FullAccess
- Copiar o ID da chave de acesso e a chave de acesso guardando nas variáveis

### Criar e configurar a CDN da Amazon (S3)

- Na opção S3 da Amazon criar um bucket
- Acessar o AWS Policy Generator
- No campo principal inserir o ARN do usuário IAM
- No campo Amazon Resource Name (ARN) inserir o ARN do S3
- Inserir a política criada no Bucket e finalizar a criação
- No  arquivo .env inserir a linha <kbd>AWS_STORAGE_BUCKET_NAME=nomedobucket</kbd>

- Acessar a sua pasta site da Amazon S3 em Buckets entre no seu projeto va no campo Permissões torne sua pasta publica em Bloquear acesso público (configurações do bucket)

- Ainda no buckets vá no campo Objeto assinale a pasta static/ depois clique ações e tornar público



### Configurar a Lib django_s3_folder_storage

```
$ pipenv install django-s3-folder-storage
```

- Configurar o arquivo Settings

```
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

# STORAGE AWS CONFIGS
if AWS_ACCESS_KEY_ID:
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400', }
    AWS_PRELOAD_METADATA = True
    AWS_AUTO_CREATE_BUCKET = False
    AWS_QUERYSTRING_AUTH = True
    AWS_S3_CUSTOM_DOMAIN = None
    AWS_DEFAULT_ACL = 'private'

    # static assets
    STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
    COLLECTFAST_STRATEGY = 'collectfast.strategies.boto3.Boto3Strategy'
    STATIC_S3_PATH = 'static'
    STATIC_ROOT = f'/{STATIC_S3_PATH}/'
    STATIC_URL = f'//s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{STATIC_S3_PATH}/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

    # Upload Media Folder
    DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
    DEFAULT_S3_PATH = 'media'
    MEDIA_ROOT = f'/{DEFAULT_S3_PATH}/'
    MEDIA_URL = f'//s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{{DEFAULT_S3_PATH}/'

    INSTALLED_APPS.append('s3_folder_storage')
    INSTALLED_APPS.append('storages')
```

- Executar o comando (como pipenv shell ativado):

```
python manage.py collectstatic --no-input
```

- Inserir no arquivo contrib/env-sample

```
AWS_SECRET_ACCESS_KEY=
AWS_ACCESS_KEY_ID=
AWS_STORAGE_BUCKET_NAME=
```

> Verificar como ficou o arquivo final do settings: https://github.com/avellar1975/Curriculos/blob/main/curriculos/settings.py
### Enviar para o servidor heroku as variáveis da AWS

```
$ heroku config:set AWS_SECRET_ACCESS_KEY=***********
$ heroku config:set AWS_ACCESS_KEY_ID=***********
$ heroku config:set AWS_STORAGE_BUCKET_NAME=***********
$ heroku config:unset DISABLE_COLLECTSTATIC

```

- Instalar a biblioteca Collectfast

```
$ pipenv install collectfast
```

- Alterar o arquivo settings.py para criar a variável COLLECTFAST_ENABLE

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'collectfast',
    'django.contrib.staticfiles',
    # Minhas APPS
    'curriculos.base',
]

(...)

COLLECTFAST_ENABLE = False

(...)

if AWS_ACCESS_KEY_ID:
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age-86400', }
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age-86400', }
    AWS_PRELOAD_METADATA = True
    AWS_PRELOAD_METADATA = True
    AWS_AUTO_CREATE_BUCKET = False
    AWS_AUTO_CREATE_BUCKET = False
    AWS_QUERYSTRING_AUTH = True
    AWS_QUERYSTRING_AUTH = True
    AWS_S3_CUSTOM_DOMAIN = False
    AWS_S3_CUSTOM_DOMAIN = False

    COLLECTFAST_ENABLE = True
    AWS_DEFAULT_ACL = 'private'
    AWS_DEFAULT_ACL = 'private'

```

## Customização do Model User do Django

Uma das dúvidas mais comum de quem usa Django é Como criar campo(s) na tabela de usuário que o Django provê por default?
Mais do quê isso. Como me se logar informando email em vez de username?
Enfim, como customizar sem estragar o que o Django já nos dá de brinde, como por exemplo o sistema de autenticação.

- Criar o arquivo base>models.py (Exemplo customizado no repositório)
- Configurar o settings.py com a variável AUTH_USER_MODEL = 'base.User'
- Executar os comandos:

```
$ python manage.py makemigrations base
$ python manage.py migrate
$ python manage.py createsuperuser

```

## Administração de Usuários
- Criar o arquivo ../base/admin.py (já está customizado no repositório)


## Aplicando Migrações no Heroku
- Inserir na primeira linha do arquivo Procfile:

```
release: python manage.py migrate --noinput
```

- Após fazer o deploy no servidor heroku executar o comando:

```
$ heroku run python manage.py createsuperuser
```
## Backup do Postgresql

- Agendar o backup através do seguinte comando:

```
$ heroku pg:backups:schedule DATABASE_URL --at '02:00 America/Sao_Paulo'
```
- Para fazer o download do último backup:

```
$ heroku pg:backups:download
```

## Django Debug Toolbar

Instalar a biblioteca através do comando:
```
$ pipenv install django-debug-toolbar
```

- No arquivo settings.py

```
INTERNAL_IPS = config('INTERNAL_IPS', cast=Csv(), default='127.0.0.1')

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
```

- No arquivo urls.py

```    
from django.conf import settings
from django.urls import include, path

(...)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
```

- Acrescentar no arquivo contrib/env-sample

```
INTERNAL_IPS=127.0.0.1
```

- Alterar o arquivo views.py para:

```
from django.http import HttpResponse


def home(requests):
    return HttpResponse('
      <!DOCTYPE html>
      <html lang="pt-br" dir="ltr">
        <head>
          <meta charset="utf-8">
          <title>Django</title>
        </head>
        <body>

        </body>
    </html>    
      ')
```

## Monitorando Erros com Sentry

> Sentry, plataforma para monitoramento de erros.

- Se cadastrar no site http://sentry.io
- Adicionar um novo projeto do tipo Django
- Instalar a biblioteca sentry-sdk

```
pipenv install sentry-sdk
```
- Alterar o settings.py

```
SENTRY_DSN = config('SENTRY_DSN', default=None)

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

if SENTRY_DSN:
  sentry_sdk.init(dsn=SENTRY_DSN, integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True)
```

- Incluir variável no .env

```
SENTRY_DSN="url_do_dsn"
```

- Adequar o arquivo contrib/env-sample
<kbd>SENTRY_DSN=</kbd>

- Configurar no heroku

```
heroku config:set SENTRY_DSN=<dsn_do_seu_projeto_no_sentry>

```


## Criação dos Arquivos Estáticos através do Bootstrap

- Escolher o layout no site [layoutit.com](https://www.layoutit.com)
- Baixar o projeto e salvar a pasta src no diretório minha_app/base/, alterando
o nome do diretório para static
- Dentro da pasta base criar os diretórios templates/base
- Copiar o arquivo index.html para pastas templates/base com o nome home.html

<img src="/images/estrutura_01.png" width="100%">

- Inserir a template tag do Django no início do arquivo home e adequar os links
para os arquivos estáticos conforme imagem abaixo:

<img src="/images/estrutura_02.png" width="100%">

> Se estiver utilizando o layoutit atentar para baixar os arquivos css e js do
bootstrap na versão 4.2 e substituí-los

## Criação de Função para Testar Conteúdo

- Criar o arquivo django_assertions.py
- Incluir um novo teste no test_home.py

```
def test_titulo(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<title>Currículos</title>')
```

## Urls Nomeadas e Encapsulando Urls em Apps

- Adequação do arquivo home.html:
 - Limpeza do navbar
 - Adequar a url

 ```<a class="navbar-brand" href="{% url 'base:home' %}">Currículos</a>```

 - Criar dentro da base um módulo chamado urls.py com o conteúdo:

 ```
 from django.urls import path
 from curriculos.base.views import home


 app_name = 'base'
 urlpatterns = [
     path('', home, name='home'),
 ]
 ```


 - Conteúdo do test_home.py:

 ```
 from curriculos.django_assertions import assert_contains
 import pytest
 from django.urls import reverse


 @pytest.fixture
 def resp(client):
     resp = client.get(reverse('base:home'))
     return resp


 def test_status_code(resp):
     assert resp.status_code == 200


 def test_titulo(resp):
     assert_contains(resp, '<title>Currículos</title>')


 def test_home_link(resp):
     assert_contains(resp, f'href="{reverse("base:home")}">Currículos</a>')
```

- Alterar o trecho do módulo urls global para:

```

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('curriculos.base.urls')),
]

```

## favicon

- Criar um diretório no pasta static com o nome img

## Herança de templates

- Documentação sobre Herança: https://docs.djangoproject.com/en/3.2/ref/templates/language/#template-inheritance

- Documentação do Django sobre variáveis: https://docs.djangoproject.com/en/3.2/ref/templates/language/#variables

- Documentação oficial sobre o include: https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#include


## Banco de Dados

### Banco local

- Instalar o  docker para permitir rodar o banco de dados de forma isolada.

> Docker é um conjunto de produtos de plataforma como serviço que usam virtualização de nível de sistema operacional para entregar software em pacotes chamados contêineres. Os contêineres são isolados uns dos outros e agrupam seus próprios softwares, bibliotecas e arquivos de configuração.

```
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```
- Criar o arquivo docker-compose.yml

- Para executar o Docker e criar o banco de dados:

```
$ sudo docker-compose up
```

- Inserir o .pgdata no .gitignore

- Configurar o acesso da aplicação com o acréscimo da linha abaixo no arquivo .env
de acordo com as configurações do arquivo docker-compose.yml

```
DATABASE_URL=postgres://usuario:senha@localhost:PORTA/meubancodedados
```

- Criar o banco de dados meubancodedados no postgresql

- Dentro do ambiente virtual do pipenv executar o comando:

```
$ python manage.py migrate
```

## Models
https://docs.djangoproject.com/en/3.2/topics/db/models/

## QuerySets
https://docs.djangoproject.com/en/3.2/ref/models/querysets/

## Criação do módulo cadastro
