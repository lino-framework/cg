.. _about.business:

=============
Lino projects
=============

Life cycle of a Lino project
============================

Initiation
----------

A Lino project starts when a physical or legal person decides to use the
:term:`Lino framework` for their purposes.

The future :term:`project operator` meets with a :term:`Lino consultant` in
order to check whether their problem is something for Lino. One aspect is the
**technical side**: whether a Lino style application makes sense. Lino as a
framework has features and limitations. Another aspect is the **financial
side**: what budget is available for (1) development and (2) for maintenance of
the production site. Yet another aspect is the **legal side**:  Does the project
operator want a proprietary application for which they hold the copyright?  Or
do they agree to share the development work by publishing source code and
documentation as Free Software using a BSD license?

The :term:`project operator` then designates
an :term:`application expert`, a :term:`development provider`
and a :term:`hosting provider`.

Planning
--------

During planning we differentiate four phases:

(1) A series of meetings where the :term:`application expert` analyses what the
:term:`project operator` wants and explains the requirements to the
:term:`development provider`.  This step will produce meeting reports and maybe
a functional project specification. This step ends when the :term:`development
provider` declares to be ready to write a prototype.

(2) During :term:`alpha phase`, the :term:`development provider` sets up a
:term:`prototype`. This phase may include a series of dialogues and meetings
between :term:`development provider` and :term:`application expert` where the
developer shows their work in progress and collects feedback from the
:term:`application expert`. The phase ends when the :term:`application expert`
declares that the site is ready to go into :term:`beta phase`.

(3) During :term:`beta phase`, the :term:`application expert` meets with the
:term:`key users <key user>`, explains them how to use the application and
collects their feedback.  The :term:`key users <key user>` start using the
application and report their questions and problems to the :term:`application
expert`. This phase ends (a) either when the :term:`application expert` declares
that the site can go into production mode or (b) submits a series of change
requests.

(4) If there were change requests during the beta phase, the :term:`development
provider` executes the requested changes, updates the site (taking care of
:term:`data migration`) and explains the new version to the :term:`application
expert`.  This phase may again include a series of dialogues and meetings between
:term:`development provider` and :term:`application expert` where the developer
shows their work in progress and collects feedback from the :term:`application
expert`. This phase ends when the :term:`application expert` declares that the
site is ready for another :term:`beta phase`.

..
    The prototype can be used for site visits in order to help with the
    analysis process.

    The prototype is part of our marketing work. It is easier and more
    efficient to write a prototype than to write a full analysis.

    Internal development ends when the customer accepts to enter the
    :term:`interactive development` phase.

Execution
---------

This is when the site runs in :term:`production` mode.

The :term:`site operator` of a site in :term:`production` mode can request at
any time a :term:`site upgrade` in order to fix a series of change requests.

Closure
-------

The :term:`site operator` of a Lino project can stop the project at any time for
diverse reasons.




.. _team.workflow:

Operation modes of a Lino site
==============================

Stable
------

The normal state of a production site. The primary goal of a site in this state
is that it just works: the server is always available, no changes in behaviour
which would confuse users.

Any issues reported by the site operator are collected as change requests

The developer works on the reported issues.

The developer publishes and maintains **release notes** for the coming version.

This document describes the issues that will be fixed by the coming version.

The release notes also explains any **non-requested changes** which will come
with the new version.  These can be caused by changes in dependencies, by
technology choices, changes in external services, ...

Users can ask at any moment to start a release. They decided that the advantage
of having these issues fixed is worth the work and risks caused by a release.

Preview testing
---------------

The :term:`server administrator` may set up a :term:`preview site` at any time.

For each preview site the developer usually writes a migration script which
copies the content of the production database into the preview database and
applies any changes in the database schema.

The :term:`key users <key user>` must now test that preview and to report their
observations.

This phase ends when the :term:`application expert` declares that the preview is
okay and that they want it to go into production.

After release
-------------

The :term:`server administrator` upgrade the production environment to use the
site which has been in preview so far. During some time the :term:`server
administrator` and the :term:`application expert` concentrate on removing any
side effects and keep ready to react to potential regression reports which might
occur. There may be additional minor updates to fix such problems.

When there are no more regressions and side effects reported, the site returns
to the Stable_ operation mode. This is the moment make an official release (on
PyPI) of the involved packages.

Glossary
========

.. glossary::

    Internal development

      When the :term:`application developer` works for a longer lapse of time
      without feedback.

    Interactive development

        A suite of site visits.  The :term:`site operator` actively contributes
        to the development process by testing and using the site, providing
        feedback, reporting issues.

    Stable maintenance

        The primary goal during the maintenance phase is to ensure stable and
        reliable operation of the site.

    Site upgrade

        A phase where the :term:`server administrator` applies new versions of the
        software running on a :term:`Lino site` in order to develop or optimize
        its functions according to the requirements of the :term:`site
        operator`.

        Activities during a :term:`site upgrade` include
        :term:`data migration`, :term:`end-user testing`,
        writing :term:`release notes`.

        A production site can move from one server to another server.


.. glossary::


    Alpha phase

        A working mode during the Planning_ phase of a Lino project where the
        :term:`application developer` sets up a :term:`prototype`.

    Prototype

        A :term:`Lino site` with publicly visible volatile fictive data.

    Beta phase

        A working mode during the Planning_ phase of a Lino project where the
        application is considered feature complete but likely to contain a
        number of known or unknown bugs. The :term:`Lino site` has protected
        data, potentially imported from legacy sources.

    Production

        A :term:`Lino site` with protected data, used for stable operation.

    Preview site

        A copy of the :term:`production` site as it would look when using some
        newer version of the software.

        It is made available to end users so they can preview and test their
        coming version before a :term:`site upgrade`.

        The primary goal of a preview site is to help the site owner to test
        new features and to reduce stress caused by unexpected results after an
        upgrade.

    Lino project

        A simple Lino project is when you develop a :term:`Lino application` and run it
        on a :term:`site <Lino site>` of your own.

        Or you may employ an :term:`application expert`,
        operate a :term:`Lino server` and share these
        to several :term:`site operators <site operator>`.

    End-user documentation

        Documentation written for end users.
