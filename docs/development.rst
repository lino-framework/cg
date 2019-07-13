.. _developers:

===========
Development
===========

Some concepts used in software development business.


.. glossary::


    Development operator

        An :term:`actor` who manages a team of :term:`developers <developer>`
        and provides infrastructure for their collaboration.

        Provides :term:`developer support` to their customers in order to help
        them with using the software.


    Developer

        A physical person who writes, publishes, maintains and optimizes
        :term:`source files <source file>` of a :term:`code repository`
        according to the requirements of a :term:`development operator`.

        The Lino community differentiate between :term:`application developers
        <application developer>` and :term:`core developers <core developer>`.

    Core developer

        A :term:`developer` working for the :term:`core team`.


    Application developer

        A :term:`developer` of a given :term:`Lino application`. Communicates
        with the :term:`application expert`.


.. glossary::


    Developer support

        The explanations given by the developer about his work.

        This includes **interactive support** in response to specific customer requests
        and **writing documentation** for the community.

        Analysis, specifications, release notes, end-user documentation.

        See also :term:`end-user support`.

    Analysis

        The work of analyzing the needs of a :term:`project operator` in order
        to implement a software solution which helps them to work more
        efficiently.



.. glossary::


    Development project

        A project where a new :term:`Lino site` is being developed.
        Usually regulated by a :term:`development contract`.

    Maintenance project

        A project where a new :term:`Lino application` is being developed.

    Pilot project

        A project where the :term:`site operator` is
        also the :term:`application operator`.

        the only user of a given
        :term:`Lino application` running on their :term:`server <Lino server>`.

    Maintenance contract

        Usually regulated by a :term:`maintenance contract`.

    Development contract

        An agreement
        between a customer acting as :term:`site operator` and a
        provider acting as :term:`developer` regarding a given
        :term:`development project`.

        In a The customer designates and provides a :term:`system administrator`,
        a :term:`server maintainer` a *site coordinator* and *key users*.

    Application expert

        The contact person between the :term:`project operator`, :term:`server
        maintainer` and :term:`application developer` of a given :term:`Lino
        application`.

        Communicates the requirements of the :term:`site operator` to the developer.
        Collects the support requests reported by :term:`end users <end user>`.
        Introduces :term:`developer support` requests.
        Answers the developer's callback questions.

        Coordinates the activities before and after a :term:`site upgrade`.

        Collaborates with the users in order to
        analyze their needs, and who then explains to the *application
        developer* how to make the application better (or how to make it at
        all, in case of a new :term:`development project`).


    Core team

        The :term:`developer` team at :doc:`rumma` who is responsible for
        improvement and maintenance of the :term:`Lino framework` in general.

        Testing, specs, quality control, continuous integration,

.. glossary::


    Code repository

        A set of :term:`source files <source file>` that implements a
        given set of functions.

    Source file

        A file which serves as a base for building a executable program code
        or consumable content (e.g. text, image, sound or video).

        Some source file formats commonly used for building executable program
        code are :file:`.py`, :file:`.js` and :file:`.rst`.

        Some consumable content file formats commonly used in a Lino project
        are :file:`.html` and :file:`.pdf`.

    Configuration file

        A file that contains configuration settings to be read by a program.

