# test_trigo
clone the repo to local server  
pip install docker-compose  
cd /app  
run docker-compoae -f docker-compose up -d  
to add config file:  
curl --header "Content-Type: application/json" \
  A--request POST \
  --data '{"username":"xyz","password":"xyz"}' \
  http://<server>/prod/service-a/config
