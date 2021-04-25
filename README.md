# test_trigo
clone the repo to local server  
pip install docker-compose  
run docker-compoae -f docker-compose up -d  
to insert config file:  
curl --location --request POST '<server>/prod/service-a/config' \
--header 'Content-Type: application/json' \
--data-raw '{
    "conf_name": "service-a",
    "test": "test1"
}'  
to update config:  
curl --location --request PUT '<server>/prod/service-a/config' \
--header 'Content-Type: application/json' \
--data-raw '{
    "conf_name": "service-a",
    "test": "test2"
}'
