==========
About Lino
==========

.. glossary::

  Lino framework

    The the collection of tools and approaches published and documented at
    `www.lino-framework.org <https://www.lino-framework.org>`__.

    See also :doc:`/lino/framework`.

    The Lino Framework can be used by any :term:`developer` as a toolkit for
    developing :term:`Lino applications <Lino application>`. It is governed by
    the :ref:`lsf` and published under a :term:`free software license`.


  Lino application

    A :term:`software product` developed using the
    :term:`Lino framework` that has a given set of functionalities, that can be
    recognized by its :term:`end users <end user>`.

    Each :term:`Lino application` is a :term:`software product` on its own,
    governed and maintained by its :term:`application carrier`.


  Lino site

    An instance of a given :term:`Lino application` running on a given
    :term:`server <Lino server>`.

    See also :doc:`/lino/site`.

    The :term:`site operator` owns all the data on their site. The
    :term:`application carrier` decides which functionalities are available.

    Every :term:`Lino site` has a web :term:`front end` under a domain or
    subdomain name, a set of local settings and configuration files, and
    usually its own database.  Multiple sites can share a same database in
    order to provide different front ends.


  demo site

    A :term:`Lino site` that contains fictive data used for demonstration or
    testing purposes.

  production site

    A :term:`Lino site` that contains sensitive data owned by its :term:`site
    operator`.

  Lino server

    A virtual or physical computer operated in order to run one or several
    :term:`Lino sites <Lino site>`.

    A Lino server is installed and maintained by a :term:`server operator`,
    either for themselves (self-hosting) or for a :term:`server provider` who
    sells this as a service to their customers.

  production server

    A :term:`Lino server` used to host one or several :term:`production sites
    <production site>`.

  demo server

    A :term:`Lino server` designed to host one or several of :term:`demo sites
    <demo site>`.

  Framework Carrier

    The legal person that governs the :term:`Lino framework` as a
    :term:`software product`. This role is currently assumed *de facto* by
    *Rumma & Ko Ltd* until a successor takes over this responsibility.
