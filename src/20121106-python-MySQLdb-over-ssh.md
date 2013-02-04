Title: python MySQLdb over ssh
Date: 2012-11-06
Tags: python, mysql

**Note**: These instructions have been tested on OS X 10.8. If your using a different OS, this might not work for you.

MySQLdb is good way to make a connection to a MySQL database from your python script. However what to do when you need to first ssh to some server first? The solution seems to be to open an [SSH Tunnel](http://en.wikipedia.org/wiki/Tunneling_protocol).

### SSH Tunnel
Setting up a tunnel is fairly easy:

	ssh user@host -L localport:mysql-server:mysql-server-port

the <code>-L</code> declares local machine. What this does is forward anything on the local machine sent to <code>localport</code> to <code>mysql-server</code> on <code>mysql-server-port</code> **via** <code>host</code>. If the remote server and the database server are on the same machine you can just use <code>localhost</code> for <code>mysql-server</code>
If our host is called <code>remote.foo</code>,the database server is called <code>dbs.bar</code> and uses the default port, and we want to use port 9870 to tunnel our command will look like this:

	ssh user@remote.foo -L 9870:dbs.bar:3306

Running this command in the terminal will setup the tunnel and open an ssh shell on remote.foo as a side effect. Keep that terminal tab open. If you close it or exit the remote shell, the tunnelling will be terminated. Open a new tab for your python script.

### Python connection
Assuming the same settings are used as used above, the python connect call will look like this:

	MySQLdb.connect(host='127.0.0.1', port=9870, user='user', passwd='password')

The connection is opening to your local machine op port 9870. The SSH Tunnel forwards all communication on that port, to <code>dbs.bar:3306</code> via <code>remote.foo</code>. 