What machine with HeyM8 should look like.

Download:
1) postgresql https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04, sudo -u user_name, ALTER USER user_name WITH PASSWORD 'new_password'; 
2) pgAdmin4 (convenient) https://askubuntu.com/questions/831262/how-to-install-pgadmin-4-in-desktop-mode-on-ubuntu
3) apache2 https://www.tecmint.com/install-apache-web-server-on-ubuntu-18-04/,
in development set user to daniil and group to root, set hostnames in /etc/hosts
4) mod_wsgi https://devops.profitbricks.com/tutorials/install-and-configure-mod_wsgi-on-ubuntu-1604-1/ sudo apt-get install libapache2-mod-wsgi-py3
5) memcached https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-memcached-on-ubuntu-16-04

There is no sense in storing venv in dropbox so create venv directly on every machine.
Venv must include:
1) Django
2) celery
3) psycopg2-binary
4) Pillow
5) python-memcached

*VS Code extensions:
1) Python
2) HTML, CSS, JS
3) Django templates
4) JQuery