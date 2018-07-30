#!/usr/bin/python3
from fabric.api import local, put, env, run
from datetime import datetime
from os import path, stat

env.hosts = ['35.237.62.36', '104.196.53.129']
env.user = 'ubuntu'


def do_pack():
    n = datetime.now()
    filename = "web_static_{}{}{}{}{}{}.tgz".format(n.year, n.month, n.day,
                                                    n.hour, n.minute, n.second)
    local("mkdir -p versions")
    path = local("tar -cvzf versions/{} web_static".format(filename))
    print("web_static packed: versions/{} -> {}"
          .format(filename, stat('versions/' + filename).st_size))

    return "versions/{}".format(filename)


def do_deploy(archive_path):

    if not path.isfile(archive_path):
        return False

    archive_file = archive_path.split('/')[1]
    file_no_ext = archive_file.split('.')[0]
    releases = '/data/web_static/releases/{}/'.format(file_no_ext)

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(releases))
        run('tar -xzf /tmp/{} -C {}'.format(archive_file, releases))
        run('rm /tmp/{}'.format(archive_file))
        # Not sure why we are doing this
        run('mv {}/web_static/* {}'.format(releases, releases))
        run('rm -rf {}/web_static'.format(releases))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases))
        return True
    except Exception as e:
        return False


def deploy():
    try:
        archive_path = do_pack()
        value = do_deploy(archive_path)
        return value
    except BaseException:
        return False


def do_clean(number=0):
    if number in [0, 1]:
        local("ls -tr versions | tail -n +2 > temp.txt")
        with open('temp.txt', mode='r') as f:
            for line in f:
                local("rm versions/{}".format(line))
        local("rm temp.txt")
    else:
        local("ls -tr versions | tail -n +{} > temp.txt".format(int(number) + 1))
        with open('temp.txt', mode='r') as f:
            for line in f:
                local("rm versions/{}".format(line))
        local("rm temp.txt")
