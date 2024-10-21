# Construye la imagen
podman build --tag humanos-conectados .

# Elimina el contenedor si existe 
podman container stop --time 5 humanos-conectados 
podman container rm humanos-conectados 

# Crea un contenedor y lo ejecuta
podman run -d -p 5000:5000 --name humanos-conectados localhost/humanos-conectados:latest

echo 'Ya está disponible http://127.0.0.1:5000'