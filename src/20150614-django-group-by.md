Title: Django ORM group by
Date: 2015-06-14 13:44:00
Tags: python, django

Filtering in Django over foreign keys or many to many relations's values has, as a buy product, the possibility of creating duplicates of the object you are actually filtering from. A simple way to avoid this is to <code>group by</code> on the primary key of the model. Django, however, does not have group by in the ORM. There is however a way to make Django add it. By slightly abusing annotation it is possible to add just such a claus.

<code>
from django.db.models import Count
obj1.objects.filter(obj2__value=1).annotate(Count('pk'))
</code>

This will add the <code>group by</code> on the obj1 primary key and avoid duplication on the result set.
