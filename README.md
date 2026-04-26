# Implementación de API REST
---
## Andy Campos Escandon
## Piero Huaytalla Otarola
## Pablo Isla Arone

---

## Ejecución del proyecto (clonado)

### 1. Clonar repositorio

```bash
git clone https://github.com/Andy-CE17/Laboratorio-5.git
cd cinespoilers

2. Crear entorno virtual
python -m venv venv

3. Activar entorno virtual (Windows)
venv\Scripts\activate

4. Instalar dependencias
pip install -r requirements.txt

5. Aplicar migracionesgit status
python manage.py migrate

6. Crear superusuario (opcional)
python manage.py createsuperuser

7. Ejecutar servidor
python manage.py runserver

8. Acceder al sistema

API Root:
http://127.0.0.1:8000/api/

---
Movies API
http://127.0.0.1:8000/api/movies/

---
Genres API
http://127.0.0.1:8000/api/genres/

---
Rooms API
http://127.0.0.1:8000/api/rooms/

---
Showtimes API
http://127.0.0.1:8000/api/showtimes/

---
Tickets API
http://127.0.0.1:8000/api/tickets/

---
Admin
http://127.0.0.1:8000/admin/
```
### Salas (Room) y Funciones (Showtime) – Andy Campos Escandon

## Creación de sala (POST)
![POST](docs/room_post.png.png)
![POST](docs/B_ROOM.png)

## Creación de función (POST)
![POST](docs/show_post.png.png)
![POST](docs/BD_SHOWTIMES.png)

## Actualización completa (PUT)
![POST](docs/show_put.png.png)
![POST](docs/BD_SHOWPUT.png)

## Actualización parcial (PATCH)
![POST](docs/show_patch.png)
![POST](docs/BD_PATCH.png)

### Eliminación de función (DELETE)
![POST](docs/show_delete.png)
![POST](docs/BD_DELETE.png)

## Piero Huaytalla Otarola

## Genre List
![POST](docs/PieroGenreList.png)

## Get Genres
![POST](docs/PieroGetGenres.png)

## Post Genres
![POST](docs/PieroPostGenres.png)

## Put Genres
![POST](docs/PieroPutGenres.png)

## Patch Genres
![POST](docs/PieroPatchGenres.png)

## Delete Genres
![POST](docs/PieroDeleteGenres.png)

## Post Movie
![POST](docs/PieroPostM.png)


## AUTOR
Pablo Isla Arone

## MOVIES
1. GET – Listado de películas
![GET](docs/LISTAR.png)

2. GET – Película por ID
![GET](docs/LISTARXID.png)

3. POST – Crear película
![POST](docs/POST06.png)

4. PUT – Actualizar película completa
![PUT](docs/PUT06.png)

5. PATCH – Actualización parcial
![PATCH](docs/PATCH06.png)

6. DELETE – Eliminar película
![DELETE](docs/DELETE06.png)

## GENRES
7. GET – Listado de géneros
![GET](docs/GET06.png)

8. GET – Género por ID
![GET](docs/GET06ID.png)

9. POST – Crear género
![POST](docs/POST06GE.png)

10. PUT – Actualizar género
![PUT](docs/PUT06GE.png)

11. DELETE – Eliminar género
![DELETE](docs/DELETE06GE.png)
![GET](docs/GET07GE.png)

## AUTOR

Pablo Isla Arone

