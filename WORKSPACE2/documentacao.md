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
2.  ``django-admin startproject nome_do_projeto .`` -> Criando um novo projeto em django
3. ``python manage.py runserver`` -> Subindo servidor
4. ``python manage.py startapp nome_do_app`` -> criando um novo app
5. ``python manage.py migrate`` - > Realiza as migrações(ativa) do projeto
6. ``python manage.py makemigrations`` -> Criar/gera um novo pacote de migração (Util para novo app e alteração do BD).
7. ``python manage.py createsuperuser`` -> Criar um novo super usuario
8. ``python manage.py changepassword nomedousuario`` -> Altera a senha