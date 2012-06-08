Title:Theming a form in Drupal 6
Date: 2010-02-23 13:07:19
Tags: drupal, form api, php, theming

Form theming in drupal 6 is quite flexible. One of the nicest tricks is the
ability to theme the form in stages. Calling drupal_render on a part of the
form will not only return the rendered version of it, but it will also mark
that part as rendered so that when you call the final drupal_render over the
whole form, it will not re-render the parts already rendered. Remember that in
order for the form to function correctly there are some hidden fields in every
form that must be added to the form. Also drupal needs to generate the form
tag. Therefore it is my advise, after doing the custom rendering of the parts
you want, add a general render of the form. this will reduce the chance of
problems with form submission. Special thanks to Rolf van de Krol, for this
tip.

