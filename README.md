# Curriculos
Solução de Banco de Currículos

## Fazendo um clone do repositório remoto na máquina local

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
