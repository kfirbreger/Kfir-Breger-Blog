Title: Week Lessons 3
Date: 2013-12-08
Tags: mercurial, django, content, javascript

## Mercurial Bookmarks

If one bookmaker is a direct decedent of another bookmaker, it is not possible to use <code>hg merge</code> between the two, since mercurial does not have a fast-forward option like git. The solution is to simply, update. Do note that it seems impossible to update to a bookmark that is half way through the tree. There is great [stack overflow question and answer](http://stackoverflow.com/questions/14702334/cant-merge-feature-bookmark-into-master-bookmark-in-mercurial) about this.

## Django-compress

page gave a 500 error
logs said SuspiciousOperation error. access was denied to file

problem was css compressor if more then 1 file was compressed. Reason was a bad media_root setting

## Mixed content

iFrame https in a http parent does not qualify but this is good to know
- [Mozilla blog post](https://blog.mozilla.org/tanvi/2013/04/10/mixed-content-blocking-enabled-in-firefox-23/)

## Check in js if in iFrame

Window top === window self

## Django timestamp field

See code

