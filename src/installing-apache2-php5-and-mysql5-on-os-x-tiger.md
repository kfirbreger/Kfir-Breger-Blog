Title:Installing Apache2, PHP5 and MySQL5 on OS X Tiger
Date: 2009-05-04 21:45:50
Tags: apache, guide, install, mysql, os x, php, web

Tiger comes bundled with Apache 1.3 and PHP4. While these are still used for
web development they are defenetly on the way out. For this reason I have
decided to set up a more up to date MAMP installation on my old Powerbook G4.
While this was all done on Tiger, it will most likely also work on Leopard.

### **Preparations**

The installation process follows mostly the unix standard. That means that you
will want to have the a /usr/local folder made. If you do not have it yet,
type the following in terminal: `sudo mkdir /usr/local ` The advantage of
using local is that whenever a system updates itself it leaves local alone. If
you install directly into /usr/bin, there is a chance that a system update
will overwrite your installed software with its own update. If you lost me by
now, you are probably off downloading a MAMP binary now. The first step is to
retrieve the packages we will need to properly install MAMP. To keep it nice
and organized make a folder that will contain the source code, if you do not
yet have a designated folder. `mkdir ~/src` We can now start installing MAMP

### **Installation**

#### MySQL

The first thing that will be installed is MySQL. You can get the latest dmg
[here](http://dev.mysql.com/downloads/mysql/5.0.html#macosx-dmg). After
installing MySQL from the dmg, I also recommend installing
[Sequelpro](http://www.sequelpro.com) if you want a GUI interface to the
database. For building MySQL yourself from source check
[this](http://hivelogic.com/articles/view/installing-mysql-on-mac-os-x).

#### Apache2

Apache comes bundled with OS X. Note that the control panel will only affect
the default installation. Starting and stopping your own Apache installation
will need some command line work, or some scripting. The following installs
Apache 2 into /usr/local/sbin/apache2, if you prefer to install into another
folder change the prefix to that folder. ` curl -O
http://apache.hippo.nl/httpd/httpd-2.2.11.tar.gz tar xvzf http-2.2.11.tar.gz
cd http-2.2.11/ ./configure --prefix=/usr/local/sbin/apache2 --enable-modules=all --enable-mods-shared=all make sudo make install cd .. ` Before we
continue to build PHP there are some extra libraries that are needed. If you
are not interested in building PHP with GD you can probably skip most of them.

#### Freetype

A Free, High-Quality, and Portable Font Engine. You can learn more about it
[here](http://www.freetype.org). ` curl -O
http://mirrors.zerg.biz/nongnu/freetype/freetype-2.3.9.tar.gz tar xvzf
freetype-2.3.9.tar.gz cd freetype-2.3.9/ ./configure make sudo make install cd
.. `

#### JPEG

Support for jpeg image format ` curl -O
http://www.ijg.org/files/jpegsrc.v6b.tar.gz tar xzf jpegsrc.v6b.tar.gz cd
jpeg-6b/ cp /usr/share/libtool/config.sub . cp /usr/share/libtool/config.guess
. ./configure --enable-shared make sudo make install cd .. `

#### Libpng

Support for png image format ` curl -O
ftp://ftp.simplesystems.org/pub/libpng/png/src/libpng-1.2.36.tar.gz tar xjf
libpng-1.2.36.tar.gz cd libpng-1.2.36/ ./configure make sudo make install cd
.. `

#### openSSL

Install the latest version of openSSL ` curl -O
http://www.openssl.org/source/openssl-0.9.8k.tar.gz tar xvzf
openssl-0.9.8k.tar.gz cd openssl-0.9.8k ./config --prefix=/usr/local
--openssldir=/usr/local/ssl make sudo make install ./config shared
--prefix=/usr/local --openssldir=/usr/local/ssl make clean make sudo make
install `

#### PHP

Now that the extra libraries are available we can continue to build PHP. We
choose to install it into `/usr/local/php5`. As before if you wish to install
into a different location, change the prefix. ` curl -O
http://de3.php.net/distributions/php-5.2.9.tar.bz2 tar xjf php-5.2.9.tar.bz2
cd php-5.2.9/ ./configure --prefix=/usr/local/php5 --with-
apxs2=/usr/local/sbin/apache2/bin/apxs --with-config-file-scan-
dir=/usr/local/php5/php.d --with-iconv --with-openssl=/usr/local --with-openssl-dir=/usr/local/ssl --with-zlib=/usr --with-gd --with-zlib-dir=/usr
--with-xmlrpc --with-iconv-dir=/usr --enable-exif --enable-sqlite-utf8
--enable-ftp --enable-sockets --enable-dbase --enable-mbstring --with-bz2=/usr
--enable-fastcgi --enable-cgi --enable-zip --with-curl --with-mysql=/usr/local/mysql --with-pdo-mysql=/usr/local/mysql --with-libxml-dir=shared,/usr/local/php5 --with-jpeg-dir=/usr/local/php5 --with-png-dir=/usr/local/php5 --with-freetype-dir=/usr/local/php5 make sudo make install
` You should now have a ready development system.

### Finalization

To make sure that the newly installed software is used instead of the default
installed one make sure that `/usr/local` and the bin and php5 folders within
are in the path before `/usr/bin`. To start the Apache server use the
following command: ` sudo /usr/local/sbin/apache2/bin/apachectl start ` Use
`stop` and `restart` to stop or restart the server.

#### Credit

This article is inspired by the following three great guides: [Compiling
Apache and PHP (and MySQL) on Mac OS X
Leopard](http://projects.serenity.de/php/)

[Apache 2 + PHP 5 + MySQL 4 under OS X
10.3.9](http://www.bioneural.net/2005/04/22/apache-2-php-5-mysql-4-under-mac-os-x-1039/)

[Installing Apache, MySQL and PHP on
Leopard](http://www.klauskomenda.com/archives/2008/10/07/installing-apache-mysql-and-php-on-leopard/)

