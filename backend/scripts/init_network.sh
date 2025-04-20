# backend/scripts/init_network.sh
#!/bin/bash

docker network create danang-net
docker network connect danang-net backend
docker network connect danang-net frontend
docker network connect danang-net db
