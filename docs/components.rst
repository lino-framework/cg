==========
Components
==========

.. glossary::

    Lino framework

        The common :term:`source code` used and shared by all :term:`Lino
        applications <Lino application>`.

        It consists of the core, the extensions library, the technical docs and
        this community guide.

        The Lino framework as :term:`software product` is governed and
        maintained by the :ref:`lsf`.

    Lino application

        A :term:`software product` written using the :term:`Lino framework`,
        having a given set of functions, governed and maintained by its
        :term:`application operator`.

    Lino site

        An instance of a given :term:`Lino application` running on a given
        :term:`server <Lino server>`, operated by its :term:`operator <site
        operator>`.

        Every :term:`Lino site` has a web :term:`front end` under a domain or
        subdomain name, a set of local settings and configuration files, and
        usually its own database.  Several sites can share a same database in
        order to provide different frond ends.

    Lino server

        A virtual or physical machine used to run one or several :term:`Lino
        sites <Lino site>`.

        Operated by a :term:`server operator`.


.. glossary::


    Client device

        Any device used by an :term:`end user` to access a :term:`Lino site`.

        This can be a desktop or notebook computer, or a mobile device.

    Software product

        A set of program code and documentation, stored in :term:`source
        files <source file>` in several :term:`repositories <code repository>`.



    Plugin

        A module or logical part of an application which potentially can be
        shared among several applications.

    Front end

        A plugin which defines the web interface for an application.

        A same database can be exposed on different sites, using the same
        application but different front ends.



    Code repository

        A set of :term:`source files <source file>` that implements a
        given set of functions.

        For example we have different repositories for the *Lino Core*, the
        *Lino Extensions Library* the Lino Book* and the *Community Guide*.

    Source code

        Content to be edited by a :term:`programmer` and to be built (compiled)
        into an executable program file or consumable content (e.g. text,
        image, sound or video).

    Source file

        A file which contains :term:`source code`.

        Some source file formats commonly used for building executable program
        code are :file:`.py`, :file:`.js` and :file:`.rst`.

        Some consumable content file formats commonly used in a Lino project
        are :file:`.html` and :file:`.pdf`.

    Configuration file

        A file that contains configuration settings to be read by a program.


    Database application

        A computer program used for entering and retrieving information from a
        database.

    Customized database application

        A :term:`database application` which is tailor-made to the needs of a
        :term:`application operator`.