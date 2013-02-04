Title: Python MySQL and Unicode
Date: 2012-10-15
Tags: python, mysql, unicode

One of the biggest changes between python 2 and python 3 is unicode support. While python 2 default string is ascii, python 3 is all unicode[citation needed]. For different reasons I have not yet made the move to python 3 which means that every now and again I get into some unicode issues.

Recently I needed to create some special exports from a utf-8 database[^u-u]. At first I completely ignored the fact it was unicode and expected everything to go just fine. Which of course it didn't.

My second attempt was  to try and convert the strings I was getting from the database to utf-8 encoded unicode. This also did not go well. At first I thought I was doing it wrong, or incomplete. Turn out I wasn't. The problem was I was looking at the wrong place. 

When using MySQLdb to connect to the MySQL server, you use the connect function. This function will connect not using the default encoding of the database neither in the default encoding of the script. It will connect using Latin-1. That is, unless you give it the key argument <code>use_unicode=True</code> So for instance to connect to a local mysql server as root the function call would look something like:

	con = MySQLdb.connect('127.0.0.1', 'root', use_unicode=True)

And that pretty much solved all my unicode problems. All the data form the database was now coming as utf-8 encoded unicode.

[^u-u]: unicode and utf-8 are not one and the same. Never forget that.