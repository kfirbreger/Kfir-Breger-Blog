Title:Setting up Solr for Drupal under tomcat
Date: 2010-07-13 08:37:56
Tags: drupal, programming, setup, solr, tomcat, web, work

Disclaimer: This method will probably not work for all servers running tomcat,
it is more a personal guide then a general one. Solr is a "popular, blazing
fast open source enterprise search platform from the Apache Lucene project".
Drupal search has traditionally been less then adequate. Using Solr to index
and search you Drupal site is therefore quite helpful. To start, download the
Solr package ([link](http://www.apache.org/dyn/closer.cgi/lucene/solr/)) and
the Solr drupal module ([link](http://drupal.org/project/apachesolr)). the
current standard distribution is Solr 1.4 and Drupal 6. Unarchive the tar
files in a location that is reachable from your server. We will assume that
tomcat is installed in `/opt/tomcat` In the Solr package there is an example
application. That is the Solr application we are going to use. If you can
write your own, you probably don't need this tutorial. **Step 1:** Copy the
example application, found in the solr package under `example/webapps` to the
tomecat webapps folder which should be `/opt/tomcat/webapps`. when copying the
file rename it to something other the solr. this will enable you to have
multiplie solr installations running under one Tomcat container. We will
assume the app is renamed `new_solr_inst`. If you are in the tomcat root
folder the command should like like this: `cp /path/to/solr/package/apache-solr-1.4.0/apache-solr-1.4.0/example/webapps/solr.war
webapps/new_solr_inst.war` Tomcat will pick up the war file and open it
automatically after a restart. **Step 2:** In the tomcat root folder create a
folder to hold your Solr configuration and data. `mkdir new_solr_inst` Copy
the example app configuration into that folder `cp -R /path/to/solr/package
/apache-solr-1.4.0/apache-solr-1.4.0/example/solr/* new_solr_inst` **Step 3:**
You need to replace the original `schema.xml` and `solrconfig.xml` with the
ones provided by the drupal module. Copy these two files to your Solr
configuration folder. Assuming you are currently at the tomcat root folder `cp
/path/to/solr/module/schema.xml new_solr_inst/conf` `cp
/path/to/solr/module/solrconfig.xml new_solr_inst/conf` The Solr app is now
ready for use. **Step 4:** The last step is needed to inform Tomcat about the
app and its settings. Go to `conf/Catalina/localhost` and create the file
`new_solr_inst.xml`. In that file fill the following content:

`<Context docBase="/opt/tomcat/webapps/new_solr_inst.war" debug="0"
privileged="true" allowLinking="true" crossContext="true">`

`<Environment name="solr/home" type="java.lang.String"
value="/opt/tomcat/new_solr_inst" override="true" />`

`</Context>`

**Step 5:** You need to restart tomcat `/opt/tomcat/bin/shutdown.sh` `/opt/tomcat/bin/startup.sh` And your Solr should be running. There are three tests we can use to check everything went well. 

  * Tomcat has opened the war file. There is now a folder `new_solr_inst` in the `webapps` folder of Tomcat.
  * Solr has made a `data` directory in the Solr home folder (that is `/opt/tomcat/new_solr_inst`)
  * In your browser go to the Solr app `http://domain:tomcat_port/new_solr_inst` and you should see a welcome screen
If all is well you are ready to combine this Solr installation with your
Drupal **Step 6:** Activate the Apache-Solr module and go to the Solr module
settings page `admin/settings/apachesolr` Assuming tomcat and drupal are
running on the same server fill in `localhost` as the host name, fill in the
port tomcat is running on and solr path should be your app name in the tomcat
webapps folder. In our case is it `new_solr_inst`. Save the settings. Drupal
should inform you that a connection is made with Solr Notes

  * It is not nessecary to put the app configuration in the Tomcat root folder. you can probably (though I have not tested this) place it anywhere you want. you do need to make sure that the environment tag in the Tomact configuration file (the one in the `conf/Catalina/localhost` folder) is pointing to the right place.
  * If you make changes to the schema you may need to dump all the indices Solr has made. you can do this via the Drupal admin interface for the Solr module.

