Neste repositório consta a implementação de um website, de uma doceria popular com os produtos que produz, para teste neste repositório contem o arquivo **db.sqlite3** que é o banco de dados utilizados com as informações.

Para funcionamento do website via servidor local siga as seguintes informações:

 1.º Passo
Crie uma pasta no seu computador, apos isto vai usar o seu **CMD**, entrar na pasta criada e usar o seguindo comando.

     git clone https://github.com/SoberanosTeam/Marketplace.git

Apos ter os arquivos passados para seu computador, dentro de sua pasta criada **(..\Sua pasta\)** vai esta a pasta Marketplace, pasta onde contém tudo necessário para executar o website.

 2.º Passo
Em sua linha de comando, vai executar o código

    python -m venv myvenv

 Assim criando um ambiente virtual, que vai estar na pasta myvenv dentro de sua pasta **(..\Sua pasta\)**, para ativar o ambiente virtual se utiliza o comando

    myvenv\Scripts\activate

Pronto seu ambiente virtual esta ativo.

 3.º Passo 
Agora que temos o ambiente virtual instalado vamos instalar o Django.

Antes de fazer isto, devemos garantir que temos instalada a última versão do pip, que é o software que usamos para instalar o Django, com a execução do comando

    python -m pip install --upgrade pip

 4.º Passo
Com seu pip atualizado, vamos agora instalar o que for necessário para executar o website, dentro de sua pasta vai ter 2 pastas a myvenv e a Marketplace, no CMD **(..\Sua pasta\)** vai usar o comando 

    CD Marketplace

Deixando neste Diretório **(..\Sua pasta\Marketplace)** e em seguida execute 

    pip install -r requirements.txt

Para instalar as dependências que serão utilizadas.

 5.º Passo
Neste passo vamos enfim iniciar o servidor (web), vamos executar o comando no **CMD**, se certificando que estamos no caminho **..\Sua pasta\Marketplace**, estando nesta pasta bastar executar 

    python manage.py runserver

Agora seu servidor estará pronto para uso.

 6.º Passo
Com o servidor rodando o acesso é feito através do link **http://127.0.0.1:8000/** , por este repositório conter um banco de dados vai ter alguns dados para o usuário ter uma melhor visualização do projeto.

Produtos cadastrados apenas para testes de execução.

Este projeto pode ser conferido no repositório do Github abaixo:

https://github.com/SoberanosTeam/Marketplace

	**Projeto realizado pela organização SoberanosTeam composta por Davi Chagas Silva, Francisco Vitor Felix de Aquino, Jefter Roberto Mota Targino e Veridiano Francisco da Silva, todos os alunos de Ciência da Computação, da disciplina de Programação Avançada do 5º período da UERN - Campus Central, ministrada pelo professor Alysson Mendes de Oliveira.**