.. _cg.components:

==========
Components
==========

The :term:`Lino framework` is defined by a set of :term:`source repositories
<source repository>` : the :term:`Lino core`, the :term:`extensions library`, a
series of :term:`Lino applications <Lino application>` maintained by the core
team, a series of :term:`front ends <front end>`, the technical docs and this
:term:`community guide`.


.. glossary::


    Client device

        Any device used by an :term:`end user` to access a :term:`Lino site`.

        This can be a desktop or notebook computer, or a mobile device.

    Lino core

        A :term:`source repository` containing core functionality used by every
        :term:`Lino application`.

    Extensions library

        A :term:`plugin library` with shared plugins that are used by many
        :term:`Lino applications <Lino application>` and maintained by the
        :doc:`/lsf`.

    Plugin

        A module or logical part of an application which potentially can be
        shared among several applications.

    Plugin library

        A collection of :term:`plugins <plugin>` grouped into a single
        :term:`source repository` and maintained by a given :term:`development
        provider`.

    Front end

        A :term:`plugin` which defines the web interface for an application.

        A same database can be exposed on different sites, using the same
        application but different front ends.


    Source repository

        A set of :term:`source files <source file>` that implements a
        given set of functions.

        For example we have different repositories for the *Lino Core*, the
        *Lino Extensions Library* the Lino Book* and the *Community Guide*.

    Source code

        Content to be edited by a :term:`developer` and to be built (compiled)
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

        A computer program used by humans for entering and retrieving
        information from a database.

    Customized database application

        A :term:`database application` which is tailor-made to the needs of an
        :term:`application carrier`.

    Framework

        A suite of software tools used by developers who write and maintain
        applications for their employer or their customers.

    End-user documentation

        Documentation targeted at :term:`end users <end user>` of a given
        :term:`Lino application`.  Written in the language requested by the
        :term:`site operator`.

    Technical documentation

        Documentation written for :term:`developers <developer>` and motivated
        :term:`site experts <site expert>`. Only in English. Includes tested source code
        snippets and part of the :term:`test suite`.

    Test suite

      A set or :term:`source code` files that don't add any functionality and is
      used only for running :term:`automated tests`.

    Automated tests

      A part of the development process which verifies that a change in the
      software doesn't break any existing functionality.



    Preview site

        A copy of the :term:`production site` as it would look when using some
        newer version of the software.

        It is made available to end users so they can preview and test their
        coming version before a :term:`site upgrade`.

        The primary goal of a preview site is to help the site owner to test
        new features and to reduce stress caused by unexpected results after an
        upgrade.
