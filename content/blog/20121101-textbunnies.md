Title: Bunnies, now in text
Date: 2012-11-01
Tags: python

One of the small irritations faced by developers is source code commit messages. So much so, that there is even a [website](http://whatthecommit.com) dedicated to weird, stupid and/or pointless commit messages. Inspired by one of the messages there. One drawing an ASCII bunny, I decided to make a site dedicated to commit bunnies. And so [bunnyapprovesthesechanges.com](http://bunnyapprovesthesechanges.com) was born. It was a simple php script that created a random bunny with a message. I was planning on recoding it in python and making it more usable, but I never got around to it. I used it here and there but I figures I was pretty much the only one.

Two days ago, I got an email from a person working for an american company. He thanked me for making the site, said that they use it frequently in his company and was wondering if I was planning to add the ability to get plain text messages instead of html. I was pleasantly surprised. Someone out there was actually using this. It felt awesome. And so last night I sat down and rewrote everything in python.

Since this is a very simple app even [flask](http://flask.pocoo.org) felt like overkill, so I went with [werkzeug](http://werkzeug.pocoo.org). And as mentioned I got around to add plain text form. Since I use python a lot I also added a multiline python string option. The site now works as follows:

* Just visitng the site will give html
* adding a /txt will return a plain text version
* adding a /py will return a multiline python string

Happy coding