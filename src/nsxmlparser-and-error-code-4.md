Title:NSXMLParser and error code 4
Date: 2011-05-25 11:31:22
Tags: cocoa, ios, objective c, programming, work, xml

Today I had one of the strangest bugs I have seen to date. I am working on an
iOS app that does  a lot of communication with a web app api. the
communication is done via XML. Since the web app requires autherntication, I
am useing specific requests and placing the response xml in a string.

NSXMLParser requires a NSData object to init with data. Following the
conversion cod eI found on Apple's site I did the following:

` NSData *xmlData = [NSData dataWithBytes:[xml
dataUsingEncoding:NSUTF8StringEncoding] length:[xml
lengthOfBytesUsingEncoding:NSUTF8StringEncoding]]; `

Passing the xmlData through to the parser ended in me getting an error 4,
which means document empty. I tried everything. Printed out the xml string to
see it was full, compared length of data and string, releasing the parser.
Still error 4. For the heck of it I tried giving the parser a nil for data.
That gave an error 5. Trying to give an empty NSData object also gave error
code 4. After 3 hours spent in google and stack overflow I was not even a
small step further.

I really didn't know what to do when, while scanning all these pages I saw a
piece of code of converting the string to data without giving the length. for
the heck of it I decided to try this:

` NSData* xmlData = [xml dataUsingEncoding:NSUTF8StringEncoding]; `

What do you know it worked. No idea why. Naturally. I wanted to know what the
length of the data object was now. I was fully expecting it to be bigger than
original. To my surprise it was the same length as the string. The same length
I was giving it in the first call.

Why this now wrks I have no idea. The first and the second calls should give
the same results, yet somehow they don't. If you got this problem, then
converting without giving the function a length. Good luck and happy
programming.

