title: dynamically loading google adsense
date: 2013-02-11
tags: javascirpt, code

With the new cookie law in Europe, its no longer an option to load google’s adsense javascript right off the bat. Once that script is loaded, cookies will be set. Since this is no longer allowed, what you need is to check if the user has accepted ads cookies and only then load the script. This did not seem like to hard a job. Since jQuery was already loaded, I figured I’d just use <code>$.getScript</code>. The script was loaded, but not executed it seemed as the ads were not shown.

My next bet was to create a script element and add it so:

	var script = document.createElement(‘script’)
	script.src = “http://link/to/google/script”
	script.type = “text/javascript”
	document.getElementById(‘container’).appendChild(script);
	
Unfortubately it didn’t work. Again, the script was loaded but not executed. The only option left was:

	document.write(‘<script src=“http://link/to/google/script”><\/script>’)
	
which both loaded the script and executed it.

This all goes to show that sometimes the simplest solution is also the best.

