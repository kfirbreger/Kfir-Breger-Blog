title: RabbitMQ under OS X 10.8
date: 2013-02-04
tags: os x, homebrew, build

Today I needed to install [RabbitMQ](http://www.rabbitmq.com) on my mac for a django project I was going to work on. I figured it was simply a question of <code>brew install rabbitmq</code>

Unfortunately, it was not. As of XCode 4.3 Apple has removed **automake**, **autoconf** and **libtool** from the xcode command line package. Luckily, they are not difficult to get thanks, again, to brew.

	brew install automake libtool rabbitmq
	
That solved the problem. Its a shame that apple removed these much needed tools from the xcode command line package.