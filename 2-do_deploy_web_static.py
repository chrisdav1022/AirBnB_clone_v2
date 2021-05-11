#!/usr/bin/python3
"""archive to your web servers"""
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

# give the ips of my both servers :3
env.hosts = ["34.75.46.215", "34.73.24.104"]


def do_deploy(archive_path):
    """Distributes an archive to a web server"""

    if os.path.isfile(archive_path) is False:
        return False
    # archive_path =versions/web_static_20170315003959.tgz
    file = archive_path.split("/")[-1]
    name = file.replace('.tgz', '')

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
            format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
            format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return FalseXS
    if run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
            format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(name)).failed is True:
        return False
    return True
