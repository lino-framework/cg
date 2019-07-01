===================
The server provider
===================

.. glossary::


    Server provider

        Installs and maintains virgin Debian servers to be used for running
        :term:`Lino sites <Lino site>`.

        Is responsible for root actions, backups, reliable functioning,
        granting access to the server
        and protecting it against unauthorized access.

        Creates one or several SSH user accounts with sudo privileges to be
        used by the :term:`server maintainer`.  Grants access to the server via
        SSH.

        Makes the sites on the server available to :term:`end users <end user>` via public
        or local network.

    Server maintainer

        Installs and maintains the software on a given server.
        Plans and executes software updates and data migrations.
        Communicates with the :term:`application developer` if needed.



