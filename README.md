#  Desafio Técnico - Resh

## Descrição

Resh Cyber Defense me deu um desafio técnico para uma vaga que estou participando, 
e esse desafio consiste em criar uma aplicação simples usando Django.

## Requisitos do desafio

 - Criar uma conta
 - Conecte-se
 - Sair
 - Alterar e-mail ou senha
 - Deletar conta

## Começando

Para executar o projeto, você precisa instalar os seguintes programas:

- [Python: Obrigatorio para criar o projeto](https://www.python.org/downloads/)
- [VS Code: Obrigatorio para desenvolver o projeto](https://code.visualstudio.com/)

## ⌨️ Desenvolvendo

Use o Gitpod, um ambiente de desenvolvimento online gratuito para o GitHub.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Suspir0n/resh.git)

Ou use o código localmente usando:
```
$ cd "diretorio da sua escolha"
$ git clone https://github.com/Suspir0n/resh.git
```

### Construindo

Para construir uma aplicação Django, execute os comandos abaixos:

```
$ pip install -r requirements.txt
```

Estes são as dependências dentro do requirements.txt:

```
asgiref==3.7.2
Django==4.2.1
python-dotenv==1.0.0
sqlparse==0.4.4
tzdata==2023.3
```

Faça essas configurações para que seu aplicativo Django funcione perfeitamente

## Run Tests with coverage

```` 
pytest -v --cov --cov-report=term-missing --cov-fail-under=90
````

## Features

## Configuration

To execute the project, it is necessary to use VsCode or an IDE of your preference, so that it identifies the dependencies necessary for execution in the repository. Once the project is imported, it will be possible to test its functionality in real time.

## Contributions

Contributions are always welcome! I hope I have helped someone in need.

## 🔓 License
MIT © [Evandro Silva](https://www.linkedin.com/in/suspir0n/)