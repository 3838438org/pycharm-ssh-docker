'''
This is a test for the dockerfile deployment
'''
import platform
import subprocess

BASH_COMMAND = 'nvidia-smi'


if __name__ == '__main__':
    print(platform.python_version())

    process = subprocess.Popen(BASH_COMMAND, stdout=subprocess.PIPE)
    output, error = process.communicate()

    print(output)
    print(error)
