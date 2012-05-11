Title:Some bash script tips
Date: 2011-12-09 12:13:59
Tags: bash, programming, script, shell, tips, unix

Every morning do a refresh of all my repositories so that I know I don't fall
behind on the code if I need to solve some problem or continue developing.
Doing this manually is not practical, and so I created a bash script to
refresh all my repositories. While I was at it I added a starting command for
the apache and mysql. Since I do not desire to start them if they are already
running, the script check first if they are already running. Writing this
script I learned a lot about shell scripting. Here are some of the things I
picked up

Adding -x to the shebang will make bash output everything that is going on,
helps with debugging

Giving a variable as a parameter to a function, if you just give the variable
name it will be treated as a string value and that will be passed to the
function. I ended up encapsulating it as `"${var}"` since the value was a
string. If your value is not a string you probably need some other solution.

Comparing a variable to a string is best achieved with the following syntax:
`if[ "${var}" = "foo" ]; then` Notice the space between the brackets and the
values inside.

Using grep to pick something out of a list of processes requires an extra step
in which you remove the grep itself from the list. `ps -e | grep -v grep |
grep searchstring` Otherwise grep might find its own search process, which is
of course not the desired effect.

Hopefully this will save you some time in scripting.

