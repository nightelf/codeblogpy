# assumes you  are in the app dir
sudo apt-get install python-pip
pip install virtualenv
sudo pip install virtualenv
sudo apt-get install postgresql-9.1
sudo apt-get install postgresql-client-9.1
sudo apt-get install pgadmin3
sudo apt-get install python dev

sudo apt-get install libapache2-mod-wsgi
sudo cp news_blog/conf/newsblo* /etc/apache2/sites-available/
sudo cp news_blog/conf/wsgi.conf /etc/apache2/mods-available/
sudo a2ensite newsblo*
sudo a2enmod ssl 
sudo service apache2 restart

virtualenv newsblogenv --no-site-packages
source newsblogenv/bin/activate
pip install -r requirements.txt
