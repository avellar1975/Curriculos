![Python package](https://github.com/avellar1975/Curriculos/workflows/Python%20package/badge.svg)

# Curriculos
Solução de Banco de Currículos

# Afiando o machado
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
## Ambientes virtuais

### 1. Pyenv

O que o pyenv nos oferece:
* Instalação do interpretador python usando o $HOME do usuário
* Instalação de várias versões diferentes do python, cada uma com seu diretório isolado

Para instalar o Pyenv:

- Instalar as libs de dependência:
```
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm gettext libncurses5-dev tk-dev tcl-dev blt-dev libgdbm-dev git python-dev python3-dev aria2 vim libnss3-tools python3-venv liblzma-dev libpq-dev
```
- Instalar o pyenv:

```
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

- Editar no .bashrc:
```
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
```

- Instalação de versão do python:
```
pyenv install <versao>
```

- Setando python global:
```
pyenv global <versao>
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
python -m venv .venv
```

- Ativar o ambiente virtual venv:

```
source .venv/bin/activate
```
- Para desativar:

```
deactivate
```

### 3.PIP
Com o virtualenv ATIVADO instalar as bibliotecas que serão utilizadas no projeto através do comando:
```
pip install <nome_da_biblioteca>
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
pip freeze > requirements.txt
```
É possível instalar todas as bibliotecas do arquivo requirements.txt através do comando:
```
pip install -r requirements.txt
```

## Flake8

Flake8 é um projeto que combina 3 ótimas ferramentas em um só pacote:

- Pep8 que verifica se o estilo do código respeita o padrão adotado pela comunidade descrito na Python Enhancement Proposal 8.
- PyFlakes que analisa estaticamente seu código detectando inúmeros anti-patterns e erros lógicos como módulos importados que não são utilizados, uso de variáveis não declaradas, entre muitas outras coisas.
- Codepaths que realiza a análise da complexidade ciclomática do código com base nas métricas de McCabe.

* Para instalar:

```
pip install flake8
```

* Criar arquivo .flake8:

```
[flake8]
exclude=.venv
```
Isso vai permitir para que o flake8 não analise a pasta .venv

* Para executar o Flake8 local basta digitar o comando:
```
flake8
```

## Integração Contínua com Git Actions

Na opção **Actions** ao lado de *Pull requests* clique na opção *Set up this workflow* no quadro **Python Applications**

<img src="/images/git-actions.png">

Com o arquivo de configuração aberto é possível alterar alguns parâmetros, por exemplo de quanto o CI será iniciado com um pull request na master ou um commit.

![Python package](https://github.com/avellar1975/Curriculos/workflows/Python%20package/badge.svg)

Para inserir o badge referente à atualização do CI basta copiar o código conforme figura abaixo e colar no arquivo README:

<img src="/images/badges.png">

- Issues:
> (upgrade de dependencias, testes automáticos com pytest,  e pipenv)
Para criar CI com githup action basta configurar o **Continuous integration workflows** Django CI
