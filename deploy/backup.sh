#!/usr/bin/env bash

timestamp=$(date "+%F-%T")

mkdir /tmp/backup
mkdir /tmp/backup_finale
chown postgres:postgres /tmp/backup

cp /etc/nginx/sites-available/* /tmp/backup
sudo -u postgres pg_dump -Fc uniqoinsdb > /tmp/backup/uniqoinsdb.dump
tar -czvf /tmp/backup/uniqoins_media.tar.gz /home/enapiuz/UniQoins/media
tar -czvf /tmp/backup_finale/backup.tar.gz /tmp/backup

rm -rf /tmp/backup_finale/backup.tar.gz.gpg

gpg --encrypt -r backup@uniqoins.com --always-trust /tmp/backup_finale/backup.tar.gz

rm -rf /tmp/backup/*

/usr/local/bin/megaput --username=backup@uniqoins.com --path /Root/uniqoins_backup/backup.${timestamp}.tar.gz.gpg /tmp/backup_finale/backup.tar.gz.gpg < ./megapass


set from = "info@qoinon.com"
echo "Regular backup made at ${timestamp}" | mutt -s "Regular Qoinon backup" -- enapiuz@gmail.com
