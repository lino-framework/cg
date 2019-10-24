=================
Hosting providers
=================

.. glossary::

  Hosting provider

    A :term:`service provider` who runs and maintains one or several :term:`Lino
    servers <Lino server>`. See :doc:`/hp`.



As a :term:`Lino hosting provider <hosting provider>` you assume the following
responsibilities:

- You set up a virtual machine running with a virgin Debian operating system and
  grant SSH access to a :term:`site maintainer`.

- You care about registering a domain name and SSH certificates if the
  customer needs it.

- You care about security and protect the server against hackers

- You make backups of the server to make sure it doesn't get lost in
  case of a serious accident.

- You care about scaling. When a customer's site grows, they might want to move
  to a bigger machine.

- You care about reliability and make sure that the Lino site is
  always available to respond when your customer needs it.

- You help end users with problems caused by issues with the server or its
  connection.

If you are able to provide these services, you should ask for being listed in
our directory of recommended Lino hosting providers.


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

  Server operator

    Operates a given :term:`Lino server`.

    Takes care for the reliable operation of the sites on a given server.

  Release notes

      A document which describes the changes introduced by a new version of
      an application.

  Data migration

      The work of adapting the data of a :term:`Lino site` when upgrading the
      application software.

  End-user testing

      The part of testing which can be delegated to selected :term:`end users
      <end user>`.

  Site maintainer

    Installs and maintains application software on a given :term:`Lino
    site`.

    Communicates with the :term:`site operator`,
    the :term:`server provider`
    and the :term:`application carrier`.

    As a site maintainer you know how to install Python packages
    (using `pip <https://pip.pypa.io/en/stable/>`__ into virtual
    environments (using `virtualenv
    <https://virtualenv.pypa.io/en/stable/index.html>`__).
    You don't need profound knowledge of Lino or the Python language.
    Previous
    experience with hosting `Django <https://www.djangoproject.com/>`_
    applications is useful.


  Server administrator

    Installs and maintains the system software on a given :term:`Lino server`.

    Takes care of the maintenance and security of the server.
    Plans and executes software updates and data migrations.

    Communicates with the :term:`site maintainers <site maintainer>` who use
    the server.
