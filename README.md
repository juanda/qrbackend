# Backend para aplicación demo para openwebminars

En un entorno virtual de python 3:

    pip install -e .
    python bin/run.py

Y se ejecuta el servicio en el puerto 5000.

Para crear una imagen docker:

    docker build -t nombre_imagen .

Para ejecutar un contenedor con esa imagen:

    docker container run -d -p 5000:5000 qrbackend

Si se quiere desarrollar es más adecuado montar el volumen con el código del
host para que al cambiar ficheros la aplicación se actualice instantáneamente.

    docker container run -d --mount type=bind,source="$(pwd)",target=/app  -p 5000:5000 qrbackend
