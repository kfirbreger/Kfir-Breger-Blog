Title:Django and static files
Date: 2008-09-26 20:18:18
Tags: coding, django, programming, python, web

After a long break I have resumed my side project in django. Last night I came
upon a problem. When testing a page outside django, the page was rendered
correctly. When it was rendered through django the javascript files were not
located.

At this point I have to admit I was a bit fullish and forgot to look at the
web server's log to see if the files were correctly served. that was an hour
and a half of trying to figure out why the javascript functions were not
found. So after smartening up I found out that the javascript files were not
found. It seemed that django kept looking for them in the wrong location.
Using the example [here](http://docs.djangoproject.com/en/dev/howto/static-files/?from=olddocs) I eventually got it all to working.

It comes down to this. in the settings.py file there is a reference to the
media URL and to the file system path to the media directory. Adding the
following code to the urls.py ` if settings.DEBUG: urlpatterns += patterns('',
(r'^tripcalc/media/(?P .*)$', 'django.views.static.serve', {'document_root':
settings.MEDIA_ROOT}), ) ` Will make sure that while django is in debug mode,
serving of the static files will be done via django. for production sites it
is better to let a dedicated web server (such as Apache) serve these static
files. And that took care of it. I can now continue with the development. And
it also enabled me to call the CSS file, so style is also shown. hurray.

