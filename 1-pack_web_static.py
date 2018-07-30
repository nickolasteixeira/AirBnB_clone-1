#!/usr/bin/python3
from fabric.api import local, put, env
from datetime import datetime
from os import stat

env.hosts = ['localhost']


def do_pack():
    n = datetime.now()
    filename = "web_static_{}{}{}{}{}{}.tgz".format(n.year, n.month, n.day,
                                                    n.hour, n.minute, n.second)
    local("mkdir -p versions")
    local("tar -cvzf versions/{} web_static".format(filename))
    print("web_static packed: versions/{} -> {}".format(filename,
                                                        stat('versions/' + filename).st_size))
