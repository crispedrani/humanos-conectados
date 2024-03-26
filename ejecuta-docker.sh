# Construye la imagen
sudo docker build --tag humanos-conectados .

# Elimina el contenedor si existe 
sudo docker container stop --time 5 humanos-conectados 
sudo docker container rm humanos-conectados 

# Crea un contenedor y lo ejecuta
sudo docker run -d -p 5000:5000 --name humanos-conectados humanos-conectados:latest

echo 'Ya está disponible http://127.0.0.1:5000'
