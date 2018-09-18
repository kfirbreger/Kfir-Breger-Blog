Title:Updating SOLR's schema
Date: 2012-01-24 11:47:15
Tags: solr

When changing SOLR's schema, it is not enough to just change the file itself.
Solr does not dynamically load the file. As long as no action is taken, the
old schema will still be in effect. After updating the schema.xml you can
either:

  * Restart SOLR or Tomcat (depending on your configuration)
  * Reload the core that will use the new schema

Relaoding the core can be done using the reload action:
`http://localhost:8983/solr/admin/cores?action=RELOAD&core=core0` Where core0
is the core you want to restart. You can visit the cores page to make sure the
core is successfully restarted.

