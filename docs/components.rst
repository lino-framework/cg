================================
The components of a Lino project
================================

.. glossary::

    Lino application

        A software product written using the :term:`Lino framework`,
        having a given set of functions, designed to be run on one or several *Lino
        sites*. A *Lino application* consists of a set of source code and documentation
        files which are grouped and published in one or several code repositories.

    Lino framework

        The common knowledge used and shared by all :term:`Lino applications
        <Lino application>`.

        It consists of program code and documentation, stored in :term:`source
        files <source file>` in several :term:`repositories <code repository>`.


    Lino site

        An instance of a given :term:`Lino application` running on a given
        :term:`server <Lino server>`.

        Operated by its :term:`operator <site operator>` who manages the
        :term:`end users <end user>`.

        Every :term:`Lino site` has its own domain or subdomain name, a set of
        local settings and configuration files, and usually its own database.

    Lino server

        A virtual or physical machine used to run one or several :term:`Lino
        sites <Lino site>`.

        Operated by a :term:`server operator`.

    Client device

        Any device used by an :term:`end user` to access a :term:`Lino site`.

        This can be a desktop or notebook computer, or a mobile device.

    Plugin

        A module or logical part of an application which potentially can be
        shared among several applications.

    Front end

        A plugin which defines the web interface for an application.

        A same database can be exposed on different sites, using the same
        application but different front ends.




.. glossary::


    Code repository

        A set of :term:`source files <source file>` that implements a
        given set of functions.

        For example we have different repositories for the *Lino Core*, the
        *Lino Extensions Library* the Lino Book* and the *Community Guide*.

    Source file

        A file which serves as a base for building a executable program code
        or consumable content (e.g. text, image, sound or video).

        Some source file formats commonly used for building executable program
        code are :file:`.py`, :file:`.js` and :file:`.rst`.

        Some consumable content file formats commonly used in a Lino project
        are :file:`.html` and :file:`.pdf`.

    Configuration file

        A file that contains configuration settings to be read by a program.


