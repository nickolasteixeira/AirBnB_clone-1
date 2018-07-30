#!/usr/bin/python3
from fabric.api import local, put, env
from datetime import datetime

env.hosts = ['localhost']

def do_pack():
    n = datetime.now()
    filename = "web_static_{}{}{}{}{}{}.tgz".format(n.year, n.month, n.day,
                                                    n.hour, n.minute, n.second)
    path = local("tar -cvzf {} web_static".format(filename))
    local("mkdir -p versions")
    put("{}".format(filename), "~/AirBnB_clone_v2/versions")

    return path
