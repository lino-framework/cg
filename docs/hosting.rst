=======
Hosters
=======


.. glossary::


    Hosting provider

        General term for legal or physical persons who run and maintain one or
        several server computers used for hosting :term:`Lino sites <Lino
        site>`.


We differentiate three types of hosting providers, depending on the additional
services they provide:


.. glossary::

    Server hosting

        The most basic hosting service.

        In this type of collaboration the :term:`hosting provider` is not reponsible for
        :term:`server administration <server administrator>` and  :term:`end-user
        support`. The :term:`site operator` usually organizes their own
        :term:`end-user support` and designates a third-party :term:`server
        administrator`.

        Provided by a :term:`server provider`.

    Application hosting

        The :term:`hosting provider` is also the :term:`application operator`.
        i.e. they answer end-user questions about how to use or configure the
        software, and they are able upgrade the site when new versions of the
        software are available. They forward any reported
        problems to the responsible application or core developer.

    Development hosting

        The :term:`hosting provider` additionally provides :term:`expert support` and
        :term:`server administration <server administrator>`


.. glossary::

    Server provider

        A :term:`hosting provider` who does :term:`server hosting`.

        Installs and maintains virgin Linux servers to be used for running
        :term:`Lino sites <Lino site>`.

        Is responsible for root actions, backups, reliable functioning,
        granting access to the server
        and protecting it against unauthorized access.

        Creates one or several SSH user accounts with sudo privileges to be
        used by the :term:`server administrator`.  Grants access to the server via
        SSH.

        Makes the sites on the server available to :term:`end users <end user>` via public
        or local network.

    Server administrator

        Installs and maintains the software on a given :term:`Lino server`,
        either as the :term:`system administrator` of a :term:`site operator`
        or for a :term:`hosting provider` who provides
        :term:`application hosting` to their customers.

        Takes care of the maintenance and security of those servers.
        Plans and executes software updates and data migrations.
        Communicates with the :term:`application developer` if needed.

        As a server administrator you don't need profound knowledge of Lino or
        the Python language, but you are going to install Python packages
        (using `pip <https://pip.pypa.io/en/stable/>`__ into virtual
        environments (using `virtualenv
        <https://virtualenv.pypa.io/en/stable/index.html>`__). Previous
        experience with hosting `Django <https://www.djangoproject.com/>`_
        applications is useful.


        As a server administrator you know
        how Lino is installed on the server  and how to react in certain situations:

        - connection problems caused by the end-user's machine
        - diagnose and fix server-side problems like performance
        - get the server back to work after a technical problem




.. glossary::

    Release notes

        A document which describes the changes introduced by a new version of
        an application.

    Data migration

        The work of adapting the data of a :term:`Lino site` when upgrading the
        application software.

    End-user testing

        The part of testing which can be delegated to selected :term:`end users
        <end user>`.


Server hosting
==============

In case of **server hosting** the server operator has two contracts: one with a
developer and one with a hosting provider.

Your job is to provide and manage the server where the developer will
install and maintain Lino. You make sure that the server is available
and secure. You collaborate with the developer for certain tasks like
mail server setup.

You are *not* reponsible for maintaining the system software on that
server, nor answering end-user questions about how to use or configure
the software. That's the job of the developer.

You are able to act as :term:`server administrator`.

It is also your job to decide whether and when you are able to offer **stable
hosting** for one or several Lino applications.


.. _stable_hosting:

Stable hosting
==============

The difference between development and stable hosting is that your
emergency maintainer has grown into an independent maintainer who can
maintain the system software, give limited end-user support and
install new versions of the application when the customer asks you to
do so.  In stable mode, the customer pays more money to you because
you provide additional services and because they don't need support by
a developer.  With stable hosting, no external developer has access to
your customer's server.

Development hosting
===================

In case of **development hosting** you offer both the hosting and the
development.


..
    A **master machine** is a virtual machine which hosts one or several
    demo sites on different Lino versions.

    customized for you by a
    developer

    You can set up and maintain a docker server and serve one of the
    dockerfiles maintained by the Lino team.  See e.g.
    https://docs.docker.com/engine/installation/linux/ubuntulinux/

    With Docker hosting the customer is always in stable mode and cannot
    switch to development mode.

    The Lino team plans to start this type of hosting as soon as there is
    a first pilot user.
