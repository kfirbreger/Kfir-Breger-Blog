Title:Full screen terminal with custom settings via applescript
Date: 2011-08-05 11:44:32
Tags: applescript, guide, os x, terminal

The new full screen option in Lion is quite nice. At the moment my favorite
application to run full screen is terminal. It has a great old school vibe to
it, not to mention that it allows you to be fully focused on that one window.
I do however, always want to change the settings when going full screen. For
some more geek credit, I go for a bigger font and a good old fashion system
font. This makes the Terminal app appear like a real old fashion terminal. To
automate the process I have written this short applescript that, when run from
the terminal window will change the settings and make the window go full
screen.

    
    
    #!/usr/bin/osascript
    -- In the line bellow, give the name of your full screen terminal settings
    set fullscreenSettings to "Pro Fullscreen"
    
    tell application "Terminal"
        -- Changing to full screen settings.
    	set current settings of front window to settings set fullscreenSettings
    	-- going fullscreen
        tell application "System Events" to keystroke "f" using {command down, option down}
    end tell
    

What this script does is in the front window, the one in which you are running
this script, it changes the settings and then simulates pressing the key combo
for full screen. I saved the file to my home directory and have made it
executable using

    
    
    chmod +x gofullscreen.applescript
    

Enjoy your old school terminal

