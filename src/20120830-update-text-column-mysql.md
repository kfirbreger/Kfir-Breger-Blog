Title: Update text in a column in MySQL
Date: 2012-08-30
Tags: mysql, db, tip

It is somethimes needed to change part of a string inside a column, like altering part of a file path. The simple **UPDATE** does not work here. MySQL has a [**REPLACE** function](http://dev.mysql.com/doc/refman/5.5/en/string-functions.html#function_replace) that solves this problem. Using the replace function the value can be updated while only replacing part of the string.[^1]

    UPDATE table_name SET column = REPLACE(column, 'search string', 'replace string') WHERE condition

To use my file path as an example here is what an actual query might be:

	UPDATE files SET file_path = REPLACE(file_path, 'old_dir', 'new_dir')

[^1]: As with all update commands, the where is optional.