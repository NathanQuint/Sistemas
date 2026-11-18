# Verbos HTTPS <=> API Backend
GET -> Guarda a informação
POST -> Posta a informaçãp
PUT -> Altera a informação
DELETE -> Deleta a informação

``O HTTPS e o CRUD tem a mesma função, so que por serem de tecnologias diferentes, eles recebem nomenclaturas distintas.``

# CRUD Backend <=> BD
C -> create - é quando eu crio alguma coisa no BD.
R -> read - é quando eu consumo dados do BD.
U -> update - é quando algo no BD é alterado.
D -> delete - é quando você EXCLUI algo no BD.



# COMANDOS DO DJANGO

1. ``pip install django`` -> instala o django no projeto
2. ``django-admin startproject nome_do_projeto`` -> Criando um novo projeto em django
3. ``python manage.py runserver`` -> Subindo servidor
4. ``python manage.py startapp nome_do_app`` -> criando um novo app
5. ``python manage.py migrate`` - > Realiza as migrações(ativa) do projeto
6. ``python manage.py makemigrations`` -> Criar/gera um novo pacote de migração (Util para novo app e alteração do BD).
7. ``python manage.py createsuperuser`` -> Criar um novo super usuario
8. ``python manage.py changepassword nomedousuario`` -> Altera a senha
9. ``from django.http import HttpResponse`` -> Utilizado qnd n se tem html pronto. Feito pra testar se a função esta rodando corretamente



# Tags do DJANGO HTML

``{% load static %}`` -> Habilita o static no arquivo. Cada template que usa o ``{% static %}`` precisa ser carregado
``{% block title %}`` -> Insere o título da aba. As páginas filhas trocam.
``{% block header %}`` -> Header público (logo+entrar). ``O base_logado.html`` troca por inteiro.
``{% block header_actions %}`` -> Só o botão "entrar". O <login.html> esvazio o bloco
``{% include %}`` -> Insere as mensagens o/ou blocos de código.
``{% block content %}`` -> O miolo da página, cada filha vai ter o seu próprio <main>.

## Tags de ROTA
``{% url 'sistema:medico-list' %}`` -> Fica nos templates e se refere a uma lista de médicos que está no app sistema
``{% url 'sistema:medico-update' medico.pk %}`` -> Utilização no template com parâmetro para update do médico
``{% url url_voltar %}`` -> url_voltar é o nome de uma varável que guarda uma lógica de retorno à página anterior
``redirect('sistema:medico-list')`` -> Fica numa view e informa que quando uma ação for realizada ,o usuário será redirecionado



# Definições de Termos

1. ``Ensalamento`` -> Afim, de não ter que criar mil caminhos no arquivo de urls, criamos 1 pasta que contenha todos eles. Assim, facilitando a modificação dessas urls e deixando mais limpa a visualização desses caminhos.

2. ``Recursividade`` -> Quando uma função chama a si mesma