Title: MySQL Optimisation, part 1
Date: 2013-05-12
Tags: mysql, server

Optimising a database server is a delicate and complex job. It is very hard to extrapolate one optimisation on another. Repeating the same steps would not necessarily give you the same benefits. That said, the tools use to measure where the problems are do have a lot of overlap between problems.

## Setting up for optimisation
There are a few setup steps that can be helpful when attempting to start optimising a database. For starters, changing the prompt from <code>mysql></code> to something more meaningful.

	prompt \d [\R:\m]>

The prompt will now display the database in use and the time, which can be helpful when queries can take over half an hour. The second setup step is turning MySQL’s profiling on. 
	SET profiling = 1;

Using profiling its possible to look back at the queries used and the time they took. To look at what’s been profiles call:

	SHOW profiles;

Last, even though it is not a specific setup it is true to all queries being tested. Use the <code>sql_no_cache</code> right after a select to make sure the query uses no cache and so the improvements you measure are not doe to better filling of the cache. It is p[possible to turn of the caching on MySQL, however that may not always be an option[^no_cache_off].

## Explain is your friend
Explain is **the** tool for checking what is going on with your queries. Calling the explain function on your query will show you exactly what MySQL is doing, what indices are used, are any temp tables made etc…
I cannot emphasise enough how important it is to understand the output syntax explain gives. Mastering it will make optimisation much simpler. Here are some examples:

	EXPLAIN(select column_name from table_name)

## Some handy inspections
Here you will find a collection of inspection queries that you can use to get a better understanding of how the tables are built and where you might improve.

### Detailing a table

	SHOW CREATE TABLE table_name\G;

This will give you a nice output of all the columns, keys and indices. If only the indices are of interest than its possible to query for only the indices of a table.

	SHOW index IN table_name;

The later shows a much better overview of the indices and can be very helpful in optimising them.

### Column analyse

	SELECT column_name FROM table_name PROCEDURE ANALYSE()\G;

MySQL will analyse the column and make recommendation on the optimal field type.[^procan] for instance if the field type can be replaced by an [enum](http://dev.mysql.com/doc/refman/5.5/en/enum.html). The optimal field recommendation can be then used in an alter table query. If for instance MySQL recommends <code>SMALLINT(3) UNSIGNED NOT NULL</code> and the column has a different field type running the following query will change the column to the recommended type[^mysqlDataIntegrity].

	ALTER TABLE table_name MODIFY COLUMN column_name SMALLINT(3) UNSIGNED NOT NULL;

Depending on the size of your table this can take a while.

### Removing NULL from a column
If you are interested in removing a null from a column, there are three steps that are needed:

- Determine the default value for the column, if one does not yet exists. For instance 0 or an empty string.
- Change all the nulls with the default value, if there are nulls in the column.
- Alter the column to disallow null

To check for null I use the following query:

	SELECT COUNT(primary_key) FROM table_name WHERE column_name IS NULL;

This not only tells you if there are nulls, but how many there are, which I find handy at times. If there are null founds, update the data

	UPDATE table_name SET column_name=default_value WHERE column_name IS NULL;

This will replace all the nulls with default values. Now what’s left is disallowing null and setting the correct default value

	ALTER TABLE table_name MODIFY column_name type NOT NULL DEFAULT default_value;

Where type is the field type[^field_type_opt].

### Adding a unique index
The difference in performance between a unique an non unique index can be huge[^mysql_idx_c]. MySQL allows for unique indices on columns that allow null values, though from my experience that does impact performance. 

	CREATE UNIQUE INDEX index_name ON table_name (column_name)

Indices generally help speed up queries, however that is not always the case. Having to many, or unnecessary indices can have a negative impact on performance. Dropping an index is quite straightforward

	DROP INDEX index_name ON table_name;

### Duplicating a table
If you want to duplicate a table in MySQL it is quite easy.

	CREATE TABLE new_table LIKE old_table;

Done. Oh, you wanted content with that? No, the content was not copied. To copy the content a second query is needed.

	INSERT INTO new_table SELECT * FROM old_table;

Depending on the size of your table, this can take a while.


[^procan]: The MySQL dev site has [good documantion](http://dev.mysql.com/doc/refman/5.0/en/procedure-analyse.html) over the usage of procedure analyse

[^mysqlDataIntegrity]: Scaling up is never an issue, however be careful when scaling down. MySQL **will not give you any warning if altering the table will cause data loss**.

[^mysql_idx_c]: [MySQL create index syntax](http://dev.mysql.com/doc/refman/5.5/en/create-index.html)

[^field_type_opt]: Like <code>int(11)</code> or <code>VARCHAR(60)</code> etc…

[^no_cache_off]: For instance when working on a production server, which I would not recommend, or when you have no access to the database configuration.