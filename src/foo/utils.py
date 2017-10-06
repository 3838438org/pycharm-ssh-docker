import os
import pwd


def greet():
    print("hi %s" % pwd.getpwuid(os.getuid()).pw_name)

