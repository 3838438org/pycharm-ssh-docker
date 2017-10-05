IMAGE_NAME=eg_sshd
APP_NAME=test_sshd
HOST_PORT=8888

build:
	docker build -t $(IMAGE_NAME) .

run: 
	docker run -d -p 8888:22 --name $(APP_NAME) $(IMAGE_NAME) 

test: run
	docker port $(APP_NAME) 22

stop:
	docker stop $(APP_NAME); docker rm $(APP_NAME)
