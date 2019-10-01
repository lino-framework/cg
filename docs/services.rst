========
Services
========

.. glossary::

    Support

        When a support provider helps their customer with using a given software
        product.

        This includes **interactive support** in response to specific customer requests
        and **writing documentation**.

        It includes analysis as well as authoring specifications, release notes,
        end-user documentation.

    End-user support

        Gives first-level support to :term:`end users <end user>`.

        The support provider is always available when end users need them.
        Forwards the request other actors if they cannot help directly.
        Organizes trainings for :term:`end users <end user>` and :term:`key users <key user>`.

    End-user documentation

        Documentation written for :term:`end users <end user>` of a given
        :term:`Lino application`.


    Developer service

        One of the services provided by a :term:`development provider`.
        Developer services usually include
        :term:`analysis`,
        :term:`programming`,
        :term:`testing`,
        :term:`deployment`,
        :term:`maintenance` and
        :term:`expert support`.

    Server hosting

      The service provided by a :term:`server provider`.

      In this type of collaboration the :term:`hosting provider` is not responsible for
      :term:`server administration <server administrator>` and  :term:`end-user
      support`. The :term:`site operator` usually organizes their own
      :term:`end-user support` and designates a third-party :term:`server
      administrator`.

    Application hosting

      A variant of :term:`server hosting` where the provider also acts as the
      :term:`application carrier`.
..
    The :term:`hosting provider` is also the :term:`application carrier`.
    i.e. they answer end-user questions about how to use or configure the
    software, and they are able upgrade the site when new versions of the
    software are available. They forward any reported
    problems to the responsible application or core developer.

.. Development hosting

..      The :term:`hosting provider` additionally provides :term:`expert support` and
        :term:`server administration <server administrator>`

..
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

  The difference between development and application hosting is that your
  emergency maintainer has grown into an independent maintainer who can
  maintain the system software, give limited end-user support and
  install new versions of the application when the customer asks you to
  do so.  In stable mode, the customer pays more money to you because
  you provide additional services and because they don't need support by
  a developer.  With stable hosting, no external developer has access to
  your customer's server.

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



Support sales models
====================

There are two fundamentally different sales models for services :
:term:`flat-rate support` and :term:`per-hour support`.

.. glossary::

  Flat-rate support

    A support sales mode where the customer pays a given sum for a given period
    and gets unlimited support.  The only limit are human resources. The
    provider promises that they give their best to help the customer with any
    problem. Upon agreement the provider can write additional invoices for extra
    work which deserves more money than usual.  This model works well when
    provider and customer trust each other and want a long-term relationship.
    The project is seen as a cooperation where both partners contribute their
    work. Advantage is reduced administrative cost and increased communication.

  Per-hour support

    A support sales mode where the customer pays for every hour of work required
    by the provider.  The provider is responsible for writing service reports
    and methods for protecting against cost overflow.
