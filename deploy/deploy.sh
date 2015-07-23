#!/usr/bin/env bash

ssh root@188.166.114.242 /bin/bash << EOF
    cd /home/enapiuz/UniQoins
    sudo -u enapiuz git pull
    cd src
    source ../../ucenv/bin/activate && sudo -u enapiuz pip3 install -r ../deploy/requirements.txt
    source ../../ucenv/bin/activate && python manage.py migrate --noinput
    source ../../ucenv/bin/activate && python manage.py bower install
    source ../../ucenv/bin/activate && python manage.py collectstatic --noinput
    cd ../
    sudo -u enapiuz touch ./deploy/touch.me
    echo uwsgi touch-restarted
EOF