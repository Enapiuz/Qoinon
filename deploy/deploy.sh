#!/usr/bin/env bash

ssh -oStrictHostKeyChecking=no root@188.166.114.242 /bin/bash << EOF
    cd /home/enapiuz/UniQoins
    exec sudo -u enapiuz /bin/bash << ENP
        git pull
        cd src
        source ../../ucenv/bin/activate && pip3 install -r ../deploy/requirements.txt
        source ../../ucenv/bin/activate && python manage.py migrate --noinput
        source ../../ucenv/bin/activate && python manage.py bower install
        source ../../ucenv/bin/activate && python manage.py collectstatic --noinput
        cd ../
        touch ./deploy/touch.me

        echo uwsgi touch-restarted
ENP    
EOF
