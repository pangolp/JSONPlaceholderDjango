# JSONPlaceholderDjango

![api_root](https://user-images.githubusercontent.com/2810187/91445225-399d7380-e84c-11ea-9e62-f7c583feb0bb.png)

![user_list](https://user-images.githubusercontent.com/2810187/91445255-4621cc00-e84c-11ea-9aad-3be91af4bbb1.png)

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
3. python manage.py migrate
```

# Para crear un super usuario

```
python manage.py createsuperuser --user=tutor --email=paganiwalter@gmail.com
```
