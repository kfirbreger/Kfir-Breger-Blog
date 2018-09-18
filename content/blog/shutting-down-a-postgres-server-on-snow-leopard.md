Title:Shutting down a Postgres server on Snow Leopard
Date: 2010-10-15 21:41:18
Tags: guide, os x, postgresql, work

Shutting down Postgres server on Snow Leopard requires some shell work, so
open up terminal and execute the following commands: `sudo su - postgres` This
will log you into the postgres server user and move you to its directory.
`bin/pg_ctl -D data stop` This will stop the server from running.

