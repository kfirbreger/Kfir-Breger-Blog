Title:Drupal 7 phantom block
Date: 2011-12-02 11:04:44
Tags: blocks, bug, context, drupal, programming

Today I can across an interesting change in the way Drupal 7 handles blocks
created via modules. In a module I made, I defined a block using the
_hook_block_info_ and _hook_block_view_. This block was added to the site's
front page. After some implementation details changed it became apparent that
the current block was not what was needed but a whole series of other blocks.
Both hooks were completely rewritten to reflect this.

I noticed that the _hook_block_view_ was called one to many times. Looking at
the front page, I saw that the, now removed block was still there. The block
admin page, however, did not show it. This was to be expected as there was no
info available for it. It was possible to configure the block though. Either
through typing the correct url, or through the small gear on the top right
side of that block. Both clearing the cache and turning the module on and off
have failed to remove this phantom block, which had no implementation but was
still around. Deinstalling the module was the only way to clear it out of the
block table (aside forma custom sql query of course). Since my module did not
have any custom information in the database this was not a problem. However if
your module does have such information, deinstalling it will remove all that
data. Since my module was available for deinstallation leads me the believe
that this is by design. Keep this in mind when building your modules.

Even after the block has been removed from the blocks table, it was still
visible. Further research led to the **Context** module. The block was added
to the display via a context reaction, and it seems that context does not
check if a block is still available. And so the _hook_block_view_ of my module
was called with the delta of the old, non-existing, block. Opening the
reaction interface for context does not show that the block is part of it,
because, I assume, it is not defined. In the database however it is still
present. Saving the context with the phantom block without making any changes
does remove it from the database, and has removed it from the front page as
well.

