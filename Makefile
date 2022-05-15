REGISTRY=registry.novogenialab.com
API_HOME=$(SOURCE)/shop-api
API_HOST_PORT=8070
API_MYSQL_HOST_PORT=3370

build:
	sudo docker build -f docker/Dockerfile-dev -t my-pj/shop-api .

create-storage:
	sudo docker run -d --name=my-pj.shop-api.mysql.storage \
		registry.novogenialab.com/notasquare-zero/images/standard-mysql:0.1 true

clear-storage:
	-sudo docker stop my-pj.shop-api.mysql.storage
	-sudo docker rm my-pj.shop-api.mysql.storage

deploy:
	sudo docker run -d --name=my-pj.shop-api.mysql \
		--volumes-from=my-pj.shop-api.mysql.storage \
		-p $(API_MYSQL_HOST_PORT):3306 \
		registry.novogenialab.com/notasquare-zero/images/standard-mysql:0.1
	sudo docker run -d --name=my-pj.shop-api.web \
		-v $(API_HOME)/src/www/:/opt/www/ \
		-p $(API_HOST_PORT):80 \
		--link my-pj.shop-api.mysql:mysql \
		my-pj/shop-api

start:
	sudo docker start my-pj.shop-api.mysql
	sudo docker start my-pj.shop-api.web

stop:
	sudo docker stop my-pj.shop-api.mysql
	sudo docker stop my-pj.shop-api.web

clear:
	-sudo docker stop my-pj.shop-api.mysql
	-sudo docker stop my-pj.shop-api.web
	-sudo docker rm my-pj.shop-api.mysql
	-sudo docker rm my-pj.shop-api.web

ssh-api:
	sudo docker exec -it my-pj.shop-api.web bash

ssh-mysql:
	sudo docker exec -it my-pj.shop-api.mysql bash
