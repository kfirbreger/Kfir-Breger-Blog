title: Testing 404 in django
date: 2013-02-08
tags: django

Django’s debugging system is very useful. It helps you narrow down where things are going wrong. For instance if you get a 404, the debugging template will show you all the url matching rules. Very useful for tracking down why an unwarranted 404 was encountered. Its somewhat less useful if you want to test your 404.html template. In this case you will need to turn off debugging.

One side effect of setting debug to false[^1] is that django’s dev server **stops serving static files**. I was, unfortunately, not aware of this and it took me some time to link the two together. There are two options to solve this:

1. Use a web server on the development system.
2. Run the dev server with <code>—insecure</code>.

Option 1 is probably the better option, esspecially if you use the same web server used in production as it improves the similarites with production. The second option is much easier. Its up to you.