#!/usr/bin/env bash

timestamp=$(date)

mkdir /tmp/backup
mkdir /tmp/backup_finale
chown postgres:postgres /tmp/backup

sudo -u postgres pg_dump -Fc uniqoinsdb > /tmp/backup/uniqoinsdb.dump
tar -czvf /tmp/backup/uniqoins_media.tar.gz /home/enapiuz/UniQoins/media
tar -czvf /tmp/backup_finale/backup.tar.gz /tmp/backup


megaput --username=backup@uniqoins.com --path /Root/uniqoins_backup/backup.${timestamp}.tar.gz /tmp/backup_finale/backup.tar.gz < ./megapass


echo "Regular backup made at ${timestamp}" | mutt -s "Regular UniQoins backup" -- enapiuz@gmail.com
