Title:Installing PostgreSQL and Sql-Ledger for Django apps on Snow Leopard
Date: 2010-10-15 21:03:09
Tags: django, guide, os x, postgresql, python, sql-ledger, work

At DOP we started working on a django front end for Sql-Ledger with the idea
of combining it later on with our ticketing system. Getting it going on my
MacBook proved to be more challenging then expected. Most of the problems were
easily solvable, but finding the oplossing proved to be tricky. Therefor I
have decided to create this simple guide, showing the steps I have taken to
get everything going. **Step 1: PostgreSQL** You can download a binary
installer from the [PostgreSQL site](http://www.postgresql.org/download/). It
will install Postgre to your `/Library` folder. This should take care of the
Postgre part. **Step 2: Sql-Ledger** Ledger is written in perl, and requires
perl to run. Luckily Snow Leopard comes standard with perl. What it does not
come standard with is the perl binding for PostgreSQL. The following 3
commands will take care of that: `sudo perl -MCPAN -e "install +YAML"` YAML is
not necessary but it can be helpful, and lacking YAML might give you problems
with DBI. `sudo perl -MCPAN -e "install DBI"` `sudo perl -MCPAN -e "install
DBD::Pg"` This will install the perl binding for PostreSQL. Download Sql-Ledger
from [here](http://www.sql-ledger.com/source/sql-ledger-2.8.31.tar.gz).
As of this writing, the latest version is 2.8.31 Unzip and untar the archive
and follow the instructions in the readme file. I did not manage to build
using the automated script and had to do everything by hand. There is also
[this page](http://www.sql-ledger.org/cgi-bin/nav.pl?page=source/mac/howto-sql-ledger-osx.html) on the ledger page with a somewhat oldish instructions
for OS X. Once Ledger is tested and it is working, its time to get the python
binding **Step 3: Python binding** ** **The pyhton binding is for PostgreSQL.
You can get the binding library, called Psycopg2 (don't ask me why) from
[here](http://initd.org/psycopg/download/). Download and upack it. Installing
is done by running: `python setup.py build` `sudo python setup.py install` If
you are not able to build it might be a problem with your path. Python is
trying to link to the PostgreSQL bin files. Try to add it to your path and
then to build again. And your done. Enjoy (or not) working with Django-Sql-Ledger

