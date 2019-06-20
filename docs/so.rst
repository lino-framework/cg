====================
The project operator
====================

A Lino project needs somebody who acts as its :term:`project operator`.
This is usually the **customer** in a :term:`development contract`.


.. glossary::


    Project operator

        Decides about the destiny of a given :term:`software project`.
        Brings the idea into life,
        decides which features to add or to remove,
        decides promotes it and use the application.
        Does strategic decisions like delegating responsibilities to actors.


A small Lino project can be a single site on a single server. In that case the
project operator is both :term:`server operator` and :term:`site operator`.

.. glossary::


    Server operator

        Operates a :term:`Lino server`.

        Takes care for the reliable operation of the sites on a given server.

    Site operator

        Operates a :term:`Lino site`.
        The owner of the data stored on that site.
        Legally responsible for protecting that data against privacy issues.
        Manages access permissions to individual :term:`end users <end user>`.

    Application expert

        The contact person between the :term:`project operator`, :term:`site maintainer` and
        :term:`application developer` of a :term:`Lino application`.

        Communicates the requirements of the :term:`site operator` to the developer.
        Collects the support requests reported by :term:`end users <end user>`.
        Introduces :term:`developer support` requests.
        Answers the developer's callback questions.

        Coordinates the activities before and after a :term:`site upgrade`.

        Collaborates with the users in order to
        analyze their needs, and who then explains to the *application
        developer* how to make the application better (or how to make it at
        all, in case of new development projects).


    End-user support

        Gives first-level support to :term:`end users <end user>`.

        The support provider is always available when end users need them.
        Forwards the request other actors if they cannot help directly.
        Organizes trainings for :term:`end users <end user>` and :term:`key users <key user>`.

    Site manager

        Manages a :term:`Lino site` via its web interface. Creates accounts for
        :term:`end users <end user>` and can change site-wide configuration
        settings. Has full access to all functions provided via the web
        interface.

    End user

        A human who uses a given :term:`Lino site` for their work.

    Key user

        An experienced :term:`end user` who knows every detail about how to use
        a given part of the application, who can explain this to their colleagues and
        who can give first-level support.

    Client device

        Any device used by an :term:`end user` to access a :term:`Lino site`.

        This can be a desktop or notebook computer, or a mobile device.

    System administrator

        Manages the IT system of a :term:`project operator`. Installs, configures
        and maintains :term:`client devices <client device>` as required.

        Installs a :term:`Lino server`, makes it available in a public or local
        network to the :term:`application developer` and :term:`end users <end
        user>`, cares for its reliability and protects it against unauthorized
        access.

