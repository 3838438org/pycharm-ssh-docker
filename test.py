'''
This is a test for the dockerfile deployment
'''
import random 
import platform

if __name__ == '__main__':
    x = random.random()
    print(platform.python_version())
    print('yo %0.2f' % x)
