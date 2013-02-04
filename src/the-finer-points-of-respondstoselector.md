Title:The finer points of respondsToSelector
Date: 2011-05-27 13:46:33
Tags: cocoa, os x, programming, work

Cocoa's object model is something I really like. Coming from Java, being able
to declare a property and have the getters and setters auto generated is
really wonderful. The key value way to interact with an object is also a very
powerful tool. The problem is what happens when these two collide.

For a project at work I needed to parse some XML. The xml contained several
entries of entries. Only part of the information given for each entry was
actually needed by the software. Therefor the object used did not have a
property for each field in the entry. Just doing the follow code will not
work:

` [currentObject setValue:(id)elemValue forKey:objProperty]; `

This will raise an exception as soon as an attempt is made to set a property
that does not exist. Wrapping the setter in a check to see if the object has
this property will solve this problem. Using responseToSelector a test can be
made to see if the object reacts to a selector

` if ([currentObject responseToSelector:NSSelectorFromString(objProperty)]) {
[currentObject setValue:(id)elemValue forKey:objProperty]; } `

This should do it. Except it doesn't completely. If your object has a function
that is named like objProperty, responseToSelector will return true, because
your object does response to it. Its just not a property that is set-able, but
instead, a method. Actually, reponseToSelector only controls for function.
Since synthesizing a property creates a method with the name of the property,
it works for detecting properties as well. To avoid getting an exception on
setting values for keys. Make sure that objProperty does not contain a value
equal to a method in currentObject that does not represent a property.

