docker build -t flask-redirect-app .
#docker logout
echo "friedrichbrunzema/password-in-password-file under Docker Hub"
docker login
docker tag flask-redirect-app friedrichbrunzema/flask-redirect-app:v3
docker push friedrichbrunzema/flask-redirect-app:v3