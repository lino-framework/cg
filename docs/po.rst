=========
Operators
=========

A :term:`Lino project` needs somebody who acts as its :term:`project operator`.


.. glossary::


    Project operator

        A legal or physical person who brings a :term:`Lino project` into life.
        Plans the project and decides about its destiny.
        Decides which features to add or to remove.
        Does strategic decisions.
        Organizes :term:`end-user support`.

        Delegates responsibilities to other actors:
        a :term:`system administrator`,
        a :term:`server provider`,
        a :term:`server administrator`
        and an :term:`application expert`.

        In a small Lino project with a single site on a single server, the
        project operator can be :term:`server operator`, :term:`site operator`
        and :term:`application operator` in one person.  In bigger projects
        these roles can be distributed among independent legal persons.

    Application operator

        A legal or physical person who
        When a same :term:`Lino application` is being used on several sites,
        the :term:`operators <site operator>` of these sites collaborate and
        maintain the application as their shared :term:`Lino project`.

    Server operator

        Operates a given :term:`Lino server`.

        Takes care for the reliable operation of the sites on a given server.

    Site operator

        Operates a given :term:`Lino site`.
        Is the owner of the data stored on that site.
        Is legally responsible for protecting that data against privacy issues.
        Manages access permissions to individual :term:`end users <end user>`.

    Framework operator

      The legal or physical person who develops and maintains the :term:`Lino
      framework` as a :term:`software product` and provides :term:`developer
      services <developer service>` for it.

People
======

.. glossary::

    System administrator

        Manages the general IT system of a :term:`project operator`. Installs,
        configures and maintains :term:`client devices <client device>` as
        required.

    Site manager

        Manages a :term:`Lino site` via its web :term:`front end`. Creates
        accounts for :term:`end users <end user>` and can change site-wide
        configuration settings. Has full access to all functions provided via
        the web interface.

    End user

        A human who uses a given :term:`Lino site` for their work.

    Key user

        An experienced :term:`end user` who knows every detail about how to use
        a given part of the application, who can explain this to their colleagues and
        who can give first-level support.
