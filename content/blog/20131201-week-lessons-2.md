Title: Week Lessons 2
Date: 2013-12-01
Tags: week-lessons, shell

## Use curl to post data

While developing an api, I needed to do some posts to a certain url. The fastest way I could think of was to use the command line <code>curl</code> command. However, by default curl does a <code>GET</code> request, and of course, sends no data. However a short googling trip took me to [this superuser answer](http://superuser.com/a/255624), which demonstrates how to do it. I was posting json to my api endpoint in no time. Example:

	curl -X POST -d @filename.json http://example.com/api/endpoint/ --header "Content-Type:application/json"

Which will do a post using data from <code>filename.json</code> to the given url. The request header content type is also set to json. Of course if your not posting json this should be changed to reflect the data.

