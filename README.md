Python3:


https://www.codingforentrepreneurs.com/blog/install-django-on-mac-or-linux/

pip3 install

to change the python version use the virtual env

to lockdown to one version in virtual env

python3.6 -m env (envname)

new project:

  django-admin startproject project-name

new app:

python manage.py startapp products

virtualenv

new one => virtualenv myenv (mien is the name)
setup => source myenv/bin/activate
comeout => deactivate

python manage.py startapp jobs


model:

   django model fields

  python manage.py makemigrations

   python manage.py migrate

python manage.py collectstatic => to collect all static files from other smaller apps


Django Shell:

python manage.py shell

import models like node