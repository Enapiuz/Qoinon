#!/usr/bin/env bash

mkdir /tmp/backup
mkdir /tmp/backup_finale
chown postgres:postgres /tmp/backup

sudo -u postgres pg_dump -Fc uniqoinsdb > /tmp/backup/uniqoinsdb.dump
tar -czvf /tmp/backup/uniqoins_media.tar.gz /home/enapiuz/UniQoins/media
tar -czvf /tmp/backup_finale/backup.tar.gz /tmp/backup

echo "Regular backup" | mutt -a "/tmp/backup_finale/backup.tar.gz" -s "Regular UniQoins backup" -- enapiuz@gmail.com
