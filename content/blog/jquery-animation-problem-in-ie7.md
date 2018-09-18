Title:jQuery animation problem in ie7
Date: 2010-05-28 13:24:30
Tags: ie problems, javascript, programming, web

For one of our projects, I was creating a photo bar. When the mouse was over
one of the photos it was ment to increase in size and decrease back to
original size when the mouse left. Unfortunately the client for which this was
developed uses ie7 exclusively. This has brought two problems: 1. ie7 does not
support the mouseleave event. I needed to replace it with mouseout event. 2.
ie7 does not accept the position property in the jQuery animate function.
Giving the position as a parameter will cause an error.

