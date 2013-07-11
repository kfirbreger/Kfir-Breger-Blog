Title: Debug http request in Python
Date: 2013-06-10
Tags: python

Creating an http request in python is quite ismple. If anything, there are to many options to get do it. My prefered way is to use the wonderful [requests](https://github.com/kennethreitz/requests) library. However, this library can be a bit slow for some used cases. I was facing just such a used case today.

Going with <code>urllib2</code> I didn't expect any trouble. Unofrtunatley, taht was not the case. I was getting <code>401</code> errors and the response object was not set. It seemed like I was stuck with my debugging. I almost gave in and instaled requests when I came across [this stackoverflow](http://stackoverflow.com/questions/2233687/overriding-urllib2-httperror-and-reading-response-html-anyway) question. Seems that the error is what I needed to inspect (actually read). Calling <code>e.read()</code> was all that was needed to show me what was actually going wrong with the requests.