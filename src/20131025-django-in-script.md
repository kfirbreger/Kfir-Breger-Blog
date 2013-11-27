Title: Including your django site in a script
Tags: python, django
Date: 2013-10-25

Out of the box django comes with a command line tool that is pretty useful. Just reading the [getting started](https://docs.djangoproject.com/en/dev/intro/) will introduce you to it. One of the options it has is top open an [interactive python shell](https://docs.djangoproject.com/en/dev/ref/django-admin/#shell) that will allow you to interact with your django app[^djmanage]. If a certain task is done regularly, there is also the possibility of writing your own management commands. Its actually quite easy to do and can be incredibly useful, as it can also be combined with [Fabric](http://fabfile.org) to automate a lot of work.

That said there are those rare occasions when the need arises to run an independent python script that uses some part of the django code. since django is just python code in a few simple steps you can be hacking away at your custom script. What is needed is to import the settings and the right directories to the python path. Assuming your app is called my_app and that all the django apps are in a folder called apps the following code should do the trick:

	import os
	import sys
	sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
	sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'apps')))
	os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

And done. Its now possible to just import apps and other django packages as in a normal django app.
What did this do? The first two lines are cleared. The third line adds the parent folder to the python path. this will allow the use of my_app as a package. The fourth line adds the apps folder to the python path. This will allow inclusion with just app names. finally, in line 5 the django settings is set. Of course if your settings file is else where, this needs to change to where it is.

[^djmanage]: [Full documentation of the manage command](https://docs.djangoproject.com/en/dev/ref/django-admin/)