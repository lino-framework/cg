======================
The values behind Lino
======================

"Lino" is also an acronym of the words **Linked objects** (as we said in
:doc:`name`). This can help us to reflect about some values behind Lino.

Every software application has a "model" of its "world", i.e. of the things it
is designed to manage.  We call this a **database schema**. Such a schema mainly
consists of "objects" and the "relations" or "links" between them. The idea of
using *linked objects* for this modelization has been first formulated by Edgar
F. Codd in 1969 in his `relational database model
<https://en.wikipedia.org/wiki/Relational_model>`_.

But even 50 years later this idea is still some kind of expert knowledge, known
to database engineers but not to normal people.

Since the early 1990s I have often observed that application developers seem to
hide from the :term:`end users <end user>` the fact that their application is
basically "nothing but a collection of linked objects". As if they were ashamed
to admit that what they are doing is *that* easy.

Yes, **Lino applications are that easy.** They feature a transparent view of
their database schema, leading to :term:`end users <end user>` being intuitively
aware of the structure behind what they are doing.  One Lino :term:`application
developer`, upon realizing this, wrote: "The development is so terribly easy,
that one customer looked at the code and started to code Layouts and modify
models by himself and I almost felt no developer is needed anymore :-)"

No, **there is no reason to feel ashamed.** The world will always need
professional developers because the gory details require some experience, and
because it is an art to make the right choices on what to take into account and
what to ignore.

The division between end users and developers is also caused naturally by
specialization, which is a necessary aspect of bigger software projects.  Lino
does not hinder specialization but lets it happen where the project needs it.

Lino encourages **communication between end users and developers.** There are
lots of competent developers who are unable to communicate with :term:`end users
<end user>`.  This is where specialization becomes absurd, because a software
application makes no sense without its users.  Lino is optimized for developers
who care about end users, and for end users who care about developers.

When :term:`end users <end user>` are intuitively aware of the structure behind
what they are doing, this leads to better communication between them and the
developers because **they speak the same language**.  Of course there are
certain differences in vocabulary, but they stop to completely miss the point of
what the other is talking about.

Lino applications give their users a **feeling of being able** to do it
themselves.  This motivates them to think about how they actually *would* do it
themselves.  The developer then just implements what they ask, no more need to
translate their language or to analyze their "true needs", because the users
understand what is possible and correctly analyze what they really need.
