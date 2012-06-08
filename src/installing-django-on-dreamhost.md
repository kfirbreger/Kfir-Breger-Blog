Title:Installing Django on Dreamhost
Date: 2008-05-19 12:29:44
Tags: django, dreamhost, programming, python, web

Dreamhost appears on the django site as one of the django friendly hosting
services. Unfortunately, dreamhost does not officially support django. It does
not have mod_python installed. Django is instead deployed using FastCGI.
Hopefully sometime in the future mod_python will be added. There are a few
good guides I have found, that explain how to setup django on a dreamhost
account:

* Jeff Croft has a good guide on his [blog](http://jeffcroft.com/blog/2006/may/11/django-dreamhost/)
* Gordon Tillman also has a good informative [page](http://www.gordontillman.info/Development/DjangoDreamhost)
* The dreamhost wiki also has a [guide](http://wiki.dreamhost.com/index.php/Django)
Between the three of them you can probably find all the information needed for
installing django for use on a dreamhost account. I will not repeat what they
explain but instead add some from my own experience.

## Python

Dreamhost, at the moment of writing, is running python 2.4. Luckily it is
possible for you to locally install python. I highly recommend it as it will
enable you to setup the python environment exactly the way you want it, and it
will make it easier to upgrade to future versions of python. ` cd ~/soft wget
http://www.python.org/ftp/python/2.5.2/Python-2.5.2.tgz tar xvfz
Python-2.5.2.tgz cd Python-2.5.2 ./configure --prefix ~/install/dir --enable-shared make make install ` Where `~/install/dir` is the directory you want
python installed in. I followed dreamhost's [Unix account setup
guide](http://wiki.dreamhost.com/Unix_account_setup) and installed it under
run. I recommend you do to, as it is easier to have full control over you
`/usr/local`. Also adding setuptools makes future installs easier ` cd ~/soft
wget http://peak.telecommunity.com/dist/ez_setup.py
~/path/to/yourpython/python ez_setup.py ` This will add the `easy_install`
script which will simplify adding packages to your own python install. The
final step is adding the new MySQLdb package ` cd ~/soft svn co https://mysql-python.svn.sourceforge.net/svnroot/mysql-python/trunk/MySQLdb MySQLdb
easy_install MySQLdb ` This is assuming easy_install is in your PATH. If it is
not it needs to be added. Your now ready to install django using your very own
Python installation. That is detailed enough so I will move to two problems I
met after the installation.

## Post Installation Problems

I met with two problems that had frustrated me for a few hours. To save you
the future installer some pain here they are in case you experience something
similar **syncdb after admin activation:** This should have been very obvious
to me but for some reason it escaped me. After enabling the admin page you
must run `django-admin.py syncdb` in your project home page. What happened was
that I ran it before I enabled the admin application. This lead to the
creation of the needed tables in the MySQL database, but no tables for the
admin application. After enabling the admin application, more tables need to
be created to accommodate the new application data. The errors I got gave me
the impression that there was an error in the MySQLdb egg, so I reinstalled
it, then tried to find some workaround. Eventually I realized that I'm just
missing the admin tables. **.htacess:** This was the real mind bender. I kept
getting an internal server error saying that it reached maximum internal
allowed redirects. It was obviously a configuration error so I compared my
.htaccess with that of the guides and it looked the same. So I looked else,
but I kept coming back to the conclusion it has to be in the .htaccess. Yet no
matter how often I looked at it I couldn't find what was wrong. I need to
point out that I am no expret when it comes to apache and that maybe if I knew
more about it this would have been simple, but I didn't so I got some gray
hairs before I realized I'm missing a space between the - and the [L]. A
bloody white space! I was feeling furious and incredibly stupid at the same
time. Django is now up and running, and I like it so far. I sure is a lot
nicer to work with then with JSP and servlets. Enjoy your python

