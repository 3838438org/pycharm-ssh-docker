HOST=<your-host>
PASSWD=<your-passwd>

sshpass -p $PASSWD ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@$HOST -p 8888
