Title:Namespacing and setTimeOut in Javascript
Date: 2010-05-11 12:39:47
Tags: javascript, programming, web

It is good practice to put all of your javascript code in its own namespace.
When doing so in combination with setTimeOut timer function it is important to
remember that the object evoking the function will be the DOM window and not
your namespace object. Therefore it is needed to add the namespace before the
name of the function called.

