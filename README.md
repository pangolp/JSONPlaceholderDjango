# JSONPlaceholderDjango

Utilizando la información proporcionada por [Json Placeholder](https://jsonplaceholder.typicode.com/) construiremos una api rest en Django a partir de los modelos proporcionados por el sitio web.

Modelos que vamos a utilizar:

- [x] /posts
- [x] /comments
- [x] /albums
- [x] /photos
- [x] /todos
- [x] /users


# Importante
Recuerda crear un entorno virtual. Instalar todas las dependencias que se encuentran en el fichero requirements.txt y crear / aplicar las migraciones.

```
1. entorno\Scripts\activate
2. pip install -r requirements.txt
3. python manage.py makemigrations
4. python manage.py migrate
```

# Para crear un super usuario

```
python manage.py createsuperuser --user=tutor --email=paganiwalter@gmail.com
```
