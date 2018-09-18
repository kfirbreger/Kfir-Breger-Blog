Title:How to truly disable drupal cache
Date: 2009-05-29 12:26:05
Tags: drupal, guide, guide, hacks, php, programming, web

Drupal, like most CMSes uses cache intensively to speed things up. In a
production site that is exactly what you what. However when developing, cache
can cause you much pain.

If your an expert in drupal you probably already realized when you need to
clear the cache in order to see changes and when not too. the developer module
even makes it quite easy to do. However for me, and I am quite sure to quite a
lot of other people it is not that clear.

"Wait", you might say. "Drupal has a disable cache setting". You would be
right to say that. Only it doesn't completely disable the cache, only part of
the cache, namely the page caching. To truly disable cache you need to do a
bit of a hacking to the cache code. Yes I know they say to never hack core
(cache is part of the core drupal release). for me this was worth it. I figure
as long as you remember its there and don't use it in production you should be
fine. The following piece of code needs to be added in `include/cache.inc`.
There are two functions there that you need to edit:

  * `cache_get`
  * `cache_set`
In `cache_get` place the code right after the `global $user`. In `cache_set`
place it at the start of the function. Here is the code that you need to add.
` if(variable_get('cache', CACHE_DISABLED) == CACHE_DISABLED) { return 0; } `
Kudos for this hack goes to Rolf van de Krol. Cheers mate.

