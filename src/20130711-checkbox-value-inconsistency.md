Title: Checkbox value inconsistency
Date: 2013-07-11
Tags: code

today while debugging an issue I came across this problem. It seems that the W3C has no direct definition for what the value of a checked checkbox should be, but rather it just notes that it is considered 'on' if it is 'checked'[^wwwcchkbx].

Even though it is not mentioned in the spec it seems that all browsers see the value of an unchecked checkbox as False. If there is a need to decide on an action based on the value of a checkbox, it is safer to check if it is unchecked (False).

On a side not, if using jQuery, it is possible to use the <code>$(element).is(':checked')</code> to check if the checkbox is checked. From my experience this seems to work well cross browser.



[^wwwcchkbx]: [Forms in HTML](http://www.w3.org/TR/REC-html40/interact/forms.html#adef-value-INPUT)