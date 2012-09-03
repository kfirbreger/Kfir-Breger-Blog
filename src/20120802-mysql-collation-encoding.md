Title: Mysql Collation Encoding
Date: 2012-08-02
Tags: mysql,character encoding,utf8


While importing a big database today I can across a duplicate primary key. The database came form the live site and I knew it did not actually had any primamry key conflict. Looking closely at the error message it was about a word with the letter **ß** in it. It was an encoding issue. Mysql was returning true on:

	ß == s

Which is actually not true. I had assumed that using utf8 also meant that the encoding was unicode however that is not the case. The Mysql [dev documents](http://dev.mysql.com/doc/refman/5.5/en/charset-unicode-sets.html) states that the default utf8 encoding is not, actually unicode.  I changed my *my.cnf* to look like this[^cnf]

	[client]
	default-character-set=utf8
	[mysql]
	default-character-set=utf8
	[mysqld]
	# This is required for some large drupal sites
	max_allowed_packet=8M
	# Char encoding
	character_set_server=utf8
	init-connect='SET NAMES utf8'
	# Setting default collation to utf-8 unicode so that special chars are considered different from ascii chars.
	collation_server=utf8_unicode_ci

This should have made Mysql use utf8 unicode for encoding en collation. To test if the server is set up correctly you can use the following query:

	show variables like "%character%";show variables like "%collation%";

You should see all utf8 and unicode.

With that done, I was expecting the import to work correctly. Yet it did not. I was still getting the duplicate key error. Digging some more into the Mysql documentation I found the page about [create table and encoding](http://dev.mysql.com/doc/refman/5.0/en/charset-table.html). Looking at the dump, the charset was indeed specified as utf-8, without collation specification. So even though the *default* setting for the server was set correctly, each table was made with collation **utf8_general_ci**. The solution was to either remove the charset directive or add a collation directive to each table creation query. Being a believer of **Explicit is better then Implicit** I chose to add the collation directive utilizing the awesomeness of vim[^vim]. The import now works properly.



[^cnf]: The max_allowed_packet has nothing to do with encoding, so feel free to ignore it.

[^vim]: If you must know this is the vim command I used: :%s/DEFAULT CHARSET=utf8/DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci/g