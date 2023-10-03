# Construye la imagen
docker build --tag humanos-conectados .

# Elimina el contenedor si existe 
docker container stop --time 5 humanos-conectados 
docker container rm humanos-conectados 

# Crea un contenedor y lo ejecuta
docker run -d -p 5000:5000 --name humanos-conectados localhost/humanos-conectados:latest

echo 'Ya está disponible http://127.0.0.1:5000'