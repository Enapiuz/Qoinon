import os
from fabric.api import run, env, cd, sudo, prefix


env.hosts = ['root@188.166.114.242:22']

def deploy():
    with cd('/home/enapiuz/UniQoins'):
        sudo('git pull', user='enapiuz')
        with cd('src'):
            with prefix('source ../../ucenv/bin/activate'):
                sudo('pip3 install -r ../deploy/requirements.txt', user='enapiuz')
                sudo('python manage.py migrate --noinput', user='enapiuz')
                sudo('python manage.py collectstatic --noinput', user='enapiuz')
        sudo('touch ./deploy/touch.me', user='enapiuz')
