Title: Week Lesson 1
Date: 2013-11-23
Tags: week-lessons, css, javascript, web, mysql

Every week there are lot of small things I pick up that I think will be useful to remember, so I decided to start a weekly post with just such things. This is the first entry in the series.

## Positioning the jQueryUI Dialog

when opening a jQuery UI dialog the position could be given as specified in the [api](http://api.jqueryui.com/position/). The short version is, you can give what part of the dialog is positioned relative to what part of which element. Quite nice and readable. giving the dict as the position entry in the dialog definition call will associate that position dict with the dialog element.

## Firefox and css Sprites

Using css sprites relies on the usage of the *background-position* style property. When properly built, adding hover changes can be achieved by just altering the x or the y axe. I find this to be very elegant. This can be done using the *background-position--x* and *background-position-y* properties. Unfortunately, as of today, **Firefox does not support x and y background position properties**. So its back to x and y for hover effects until mozilla adds it.

## MySQL foreign key constrain

When adding a foreign key constrain, it seems that both tables need to have the same engine. I was trying to add a constrain and it kept failing. I had no idea why till I came across a [stack overflow question](http://stackoverflow.com/a/16969176/481651), where the answer specifies the engine should be the same. Mine weren't. Making them the same solved my problems.