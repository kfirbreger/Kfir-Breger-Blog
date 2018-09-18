Title: Drupal's purge and feeds combi problem
Date: 2013-01-10
Tags: drupal,apache,purge,feeds,server

[Purge](http://drupal.org/project/purge) is a drupal module that clears URLs from reverse proxy caches like Varnish, Squid or Nginx by issuing an http PURGE request to them.

[Feeds](http://drupal.org/project/feeds) is a drupal module that import or aggregate data as nodes, users, taxonomy terms or simple database records. It is a very flexible tool for working with external data sources.

The problem I encountered was when the two are used together on a development server. If that server has no reverse proxy, this module combi gets the server stuck. On the one hand, Feeds tries in a batch to import node. On the other hand Purge is trying to send purge http requests that are not know to apache and therefore are not handled correctly. This leads to crazy growth in the amount of apache processes, memory usage and server load, requiring a restart of apache within a minute to get nay response out of the system.

My pro tip here is:

**If you use the Purge module, make sure its turned of if you have no reverse proxy active**
