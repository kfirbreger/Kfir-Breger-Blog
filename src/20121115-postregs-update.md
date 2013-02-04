Title: Update Postgres from 9.1 to 9.2 with homebrew
Date: 2012-11-12
Tags: homebrew, postgresql, os x

[Homebrew](http://mxcl.github.com/homebrew/) has really changed the way I used my terminal[^brew]. I tried both fink, and (mac)ports. Both of them felt short of a good package manager system. Then along came homebrew and won me over. It just work. For instance, with the command <code>brew upgrade</code> all your packages get upgraded. Easy.

My postgresql installation is done via homebrew, as it is easiest way to install postgresql on a mac[^1]. And so yesterday when I ran my usual upgrade, postgres was updated from 9.1 to 9.2. Didn't really seem like  a bog deal, but when I tried to start the server, it complained that the database was created for 9.1 and is not compatible with 9.2.

**Shit**

Ok, so what do I do now? Googling around I found that there is a tool within postgres to update the database, but using it seemed to require having both versions installed side by side. Not really an option for me (Correct me if I'm wrong). the other option seemed to be the [dump and restore](http://www.postgresql.org/docs/9.1/static/backup.html) route. Its not elegant, but it is workable. So the first step was to revert to postgres 9.1

	brew switch postgres 9.1.5

This restored me to postgres 9.1 to be able to access the database. If you don't have to upgrade its also possible to just stop now and keep using 9.1. I however like to always keep the latest (stable) version around and so the next step was dump. Start the server and run:

	pg_dumpall > clusterdata.sql

The reason I used dumpall is that it dumps all the cluster data. With the data in a dump file , its time to revert back to 9.2.1. So stop the server and run:

	brew switch postgres 9.2.1

And I figured, its now a question of starting the server. Only problem is, you need to give <code>pg_ctl</code> a cluster to start. I had none. I tried the <code>createdb</code> shell command, which didn't work either because it requires the server to run. Searching some more I found that <code>pg_ctl</code> can also be used to init a new cluser with the, wait for it, init(db) command. Running the next command will create a new 9.2 compatible cluster:

	pg_ctl initdb -D /path/to/cluster/clustername

Now the server can be started with the new cluster. The last step is to import the data:

	psql -f clusterdata.sql databasename

According to the docs, if your starting with a new cluster, which we are doing, you should use postgres for database name. In any case, that is what I did.

Enjoy your upgraded database server.

[^brew]: You really should use it if your not already, its brilliant.
[^1]: As easy as <code>brew install postgresql</code>