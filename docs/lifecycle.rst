.. _about.business:

============================
Life cycle of a Lino project
============================

This document describes the life cycle of a Lino project.


The four phases of a Lino project
=================================


.. glossary::


    Initiation

        A future :term:`project operator` meets with a :term:`Lino consultant` in
        order to check whether their problem is something for Lino.

        One aspect is the technical side: whether a Lino style application makes sense.
        Lino as a framework has features and limitations. Another aspect is the
        financial side: what budget is available for (1) development and (2) for
        maintenance of the production site.

        A developer may decide to work for free during some time, but a sustainable
        solution needs maintenance and support.  Free software is free as in "free
        speech", not as in "free beer".


    Planning

        The planning phase can be divided into :term:`internal development` and
        :term:`interactive development`.

        site visits, estimations, agreements.

    Execution

        This is when the site runs in :term:`production` mode.

    Closure

        A Lino project can stop for diverse reasons.


Development modes
=================

.. glossary::

    Internal development

        The :term:`application developer` installs a prototype of the
        application to be used. This consists of setting up a :term:`Lino site`
        in :term:`prototype` mode.

        The prototype can be used for site visits in order to help with the
        analysis process.

        The prototype is part of our marketing work. It is easier and more
        efficient to write a prototype than to write a full analysis.

        Internal development ends when the customer accepts to enter the
        :term:`interactive development` phase.

    Interactive development

        A suite of site visits.  The site owner actively contributes to the
        development process by testing and using the site, providing feedback,
        reporting issues.

    Stable maintenance

        The primary goal during the maintenance phase is to ensure stable and
        reliable operation of the site.

    Site upgrade

        A phase where the :term:`server maintainer` applies new versions of the
        software running on a :term:`Lino site` in order to develop or optimize
        its functions according to the requirements of the :term:`site
        operator`.

        Activities during a :term:`site upgrade` include
        :term:`data migration`, :term:`end-user testing`,
        writing :term:`release notes`.

        A production site can move from one server to another server.


Operation modes of a Lino site
==============================

A Lino site runs in one of the following operation modes.

.. glossary::


    Prototype

        Publicly visible fictive data. Used for analysis, testing, visiting during an
        :term:`interactive development` phase.

    Production

        Protected data. Stable operation.

    Preview site

        A copy of the :term:`production` data as it would look when using some
        newer version of the software.

        It is made available to end users so they can preview and test their
        coming version before a :term:`site upgrade`.

        The primary goal of a preview site is to help the site owner to test
        new features and to reduce stress caused by unexpected results after an
        upgrade.




There are different models for selling our work
on Lino. During the first 15 years we worked successfully by offering fixed
yearly flat-rate contracts: the customer pays a given sum per year and for this
they get unlimited support and upgrades.  The only limit are our human
resources. We promise to our flat-rate customers that we give our best (but not
more) to help them with any problem. We can write additional invoices for extra
work if the customer agrees that some project deserves more money than usual.
Since 2016 we also offer per-hour service where the customer pays for every
minute of our time (including support, analysis, code changes, write
documentation).

There are other things that should be clear after the interview:

- Who will act as the single contact person responsible for analyzing the
  needs of the project operator and training the end-users.  Depending on the project operator size this can
  quickly become a full-time job on its own.

Another aspect is the legal side:

Does the project operator want a proprietary application for which they hold the
copyright?  Or do they agree to share the development work by publishing source
code and documentation as Free Software using a BSD license?

Offer and prototype
===================

Now the *consultant* must find a developer who agrees to write an offer and a prototype
for the project.

They don't need to pay for this.

(To be continued)

Active development phase
========================

Production sites
================

End-user documentation
======================

