=================
Hosting providers
=================

As a :term:`Lino hosting provider <hosting provider>` you assume the following
**responsibilities**:

- You set up a virtual machine running with a virgin Debian operating system and
  grant SSH access to a :term:`site maintainer`.

- You care about registering a domain name and SSH certificates if the
  customer needs it.

- You care about security and protect the server against hackers

- You make backups of the server to make sure it doesn't get lost in
  case of a serious accident.

- You care about scaling. When a customer's site grows, then they
  might want to move to a bigger machine.

- you care about reliability and make sure that the Lino site is
  always available to respond when your customer needs it.

- you help end-users with certain problems.

If you are able to provide these services, you should ask for being listed in
our directory of recommended Lino hosting providers.

We differentiate three types of :term:`hosting providers <hosting provider>`,
depending on the additional services they provide:


.. glossary::

  Server provider

    A :term:`hosting provider` who does :term:`server hosting`.

    Installs and maintains virgin Linux servers to be used for running
    :term:`Lino sites <Lino site>`.

    Is responsible for root actions, backups, reliable functioning,
    granting access to the server and protecting it against unauthorized access.

    Creates one or several SSH user accounts with sudo privileges to be
    used by the :term:`server administrator`.  Grants access to the server via
    SSH.

    Makes the sites on the server available to :term:`end users <end user>` via public
    or local network.

  Production server

    A dedicated server designed to host one or several :term:`production sites
    <production site>`.

  Demo server

    A dedicated server designed to host a series of demo sites.


.. glossary::

    Release notes

        A document which describes the changes introduced by a new version of
        an application.

    Data migration

        The work of adapting the data of a :term:`Lino site` when upgrading the
        application software.

    End-user testing

        The part of testing which can be delegated to selected :term:`end users
        <end user>`.
