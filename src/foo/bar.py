import os
import pwd


def greet():
    print("Hi %s!" % pwd.getpwuid(os.getuid()).pw_name)

