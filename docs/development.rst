.. _developers:

===========
Developers
===========

Some concepts used in software development business.


.. glossary::

    Development provider

        An organization who employs a team of :term:`developers <developer>` or
        other :term:`software engineers <software engineer>` and operates an
        infrastructure for their collaboration.

        Provides :term:`developer services <developer service>` to their
        customers in order to help them with using the software.

    Application developer

        The :term:`development provider` responsible for developing and maintaining a given
        :term:`Lino application` according to the requirements formulated by the
        :term:`application operator`.

        Provides :term:`expert support` to :term:`application experts
        <application expert>`.

    Core developer

        The :term:`development provider` responsible for developing and
        maintaining the :term:`Lino framework`. This includes the :term:`Lino
        Core`, the :term:`Extensions library` and their documentation.

        Provides :term:`developer support` to :term:`application developers
        <application developer>`.


Support sales models
====================

A :term:`development provider` lives from selling :term:`developer services
<developer service>`. There are two fundamentally different sales models :
:term:`flat-rate support` and :term:`per-hour support`.

.. glossary::

  Flat-rate support

    A support sales mode where the customer pays a given sum per year and for this
    they get unlimited support and upgrades.  The only limit are human resources.
    The provider promises that they give their best to help the customer with any
    problem. Upon agreement the provider can write additional invoices for extra
    work which deserves more money than usual.  This model works well when
    provider and customer trust each other and want a long-term relationship.  The
    project is seen as a cooperation where both partners contribute their work.
    Advantage is reduced administrative cost and increased communication.

  Per-hour support

    A support sales mode where the customer pays for every minute of service,
    including support, analysis, code changes, write documentation).


Developer services
==================

.. glossary::

    Developer service

        One of the services provided by a :term:`development provider`.
        Developer services usually include
        :term:`analysis`,
        :term:`programming`,
        :term:`testing`,
        :term:`deployment`,
        :term:`maintenance` and
        :term:`expert support`.

    Analysis

        The work of analysing the needs of a :term:`project operator` in order
        to implement a software solution which helps them to work more
        efficiently.

    Programming

        Apply changes to a :term:`source file`. Publish the changes.

    Testing

        Quality Control. Make sure that a new version does not introduce
        regressions or other side effects.

    Deployment

        Installing the software on a remote site, either public or for a
        :term:`site operator`.

    Developer support

        Support given by the :term:`core developer` to an :term:`application
        developer`.

    Expert support

        Support given by the :term:`application
        developer` to the :term:`application expert`.

        The explanations given by the :attr:`application developer` about his work.
        This is more technical and specialized than :term:`end-user support`.

        This includes **interactive support** in response to specific customer requests
        and **writing documentation**.

        It includes analysis as well as authoring specifications, release notes,
        end-user documentation.

    Maintenance

        Minor changes in the software which are required by technological
        evolutions.


People
======


.. glossary::


    Developer

        A physical person who writes, publishes, maintains and optimizes
        :term:`source files <source file>` of a :term:`source repository`
        according to the requirements of a :term:`development provider`.

        The Lino community differentiates between :term:`application developers
        <application developer>` and :term:`core developers <core developer>`.

    Programmer

        A :term:`developer` specialized in writing :term:`source code`.

    Software engineer

        A person who is not a :term:`developer` but is part of a developer team.

    Application expert

        The contact person between the :term:`project operator`, :term:`server
        administrator` and :term:`application developer` of a given :term:`Lino
        application`.

        Communicates the requirements of the :term:`site operator` to the developer.
        Collects the support requests reported by :term:`end users <end user>`.
        Introduces :term:`expert support` requests.
        Answers the developer's callback questions.

        Coordinates the activities before and after a :term:`site upgrade`.

        Collaborates with the users in order to analyse their needs, and then
        explains to the :term:`application developer` how to make or improve the
        application.
