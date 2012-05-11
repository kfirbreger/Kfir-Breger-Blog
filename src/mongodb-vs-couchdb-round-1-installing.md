Title:MongoDB vs CouchDB round 1 - Installing
Date: 2010-12-18 11:45:08
Tags: couchdb, mongodb, setup, web

Recently I have started on a new project which will utilize a lot of the new
web technology. The server will be nginx, combined with nodejs. For the
database side there are two options to consider: MongoDB and CouchDB. Since I
know two little about these two databases, I decided to try them both out and
see which one comes on top, for my needs. As this is the first time I will be
using any of these databases, the first step is of course installation, which
I will need to go through twice, once for the development environment and once
for the production environment.

  * MongoDB - Download unzip and put where you want.
  * CouchDB - Has been building for over 5 min, and had to rerun make once.

I am installing on OS X 10.6.4 running on a Macbook. No ports, just bash. As
you can see, MongoDB is in much easier to install. Next up is configuring to
work with node.js

Edit: It took me almost an hour to finish installing CouchDB. To be fair most
of it was from dependencies that were needed and for installing Erlang. Then
again, I dont know many machines that come with Erlang out of the box, so you
will probably need to go through this as well.

Score: MongoDB:1 CouchDB:0


