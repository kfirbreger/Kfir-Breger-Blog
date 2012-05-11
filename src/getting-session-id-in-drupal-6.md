Title:Getting session ID in Drupal 6
Date: 2010-02-25 22:49:22
Tags: drupal, guide, php, programming, web

Drupal saves its sessions in the sessions table. One can always query they
table to get the session ID. There is however a faster way. If the user is
logged it, the session id can be found with the following code:

    
    
    global $user;
    $user->sid;
    

In any case the session id can also be read from the cookie:

    
    
    $_COOKIE[session_name()];
    

