# PyCharm and remote Docker
The main purpose of this document is to describe how one should setup his/hers PyCharm to be able to run and debug code in container in a remote docker.

## Contents
* bin
    1. mac-connect.sh - script to ssh into a running container frictionless
    2. mac-setup.sh   - script to download sshpass 
* src
    1. test.py - this is the python code that will be executed on the server
* Dockerfile - installs ssh server into your base container
* Makefile - handful of commands that setups the container in the remote sever

## How to run it?
### Server Side
* Clone this repo to the remote cluster you are going to run your code on.
* Setup your claimed ports and GPUs in the makefile

To run the container type:
```bash
> make run
```
This will build your docker image, mount the `$(pwd)/src` directory to `/root/src` in container and run it.

### Local
* sshfs the folder you are working on in the remote server to some your folder. 
* Open PyCharm and [setup your python interpreter to be the remote interpreter via ssh](https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html) using the `root` user and password from the `Dockerfile`. Remember to map the paths!
* Update the credentials in `./bin/mac-connect.sh' 
* Test the connection by running `./bin/mac-connect.sh`
* Voila! You can run and debug code in PyCharm.

## TODO
* proper secret management. 
* some config setup, so that `Dockerfile`, `Makefile` and shell scripts are sharing stuff (port, user names, passwords, etc.)
* *You have to ssh in console before running code in PyCharm* to make this work. I don't know why.
