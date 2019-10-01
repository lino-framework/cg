======
People
======

The people who make up the Lino community :term:`community members <community
member>` can be categorized into different types of actors, each having their
own set of motivations, skills and responsibilities.

.. toctree::
   :maxdepth: 1


   so
   ac
   dp
   hp



.. glossary::

  End user

      A human who uses a given :term:`Lino site` for their work.

  Key user

      An experienced :term:`end user` who knows every detail about how to use a
      given part of the application, who can explain this to their colleagues
      and who can give first-level support.

  Site administrator

      Manages a :term:`Lino site` via its web :term:`front end`.
      Manages accounts and access permissions to individual :term:`end users <end user>`.
      Can change site-wide configuration settings.
      Has full access to all functions provided via the web interface.

  Site manager

      At the moment this is a synonym for :term:`site administrator`.

  Application programmer

    A :term:`programmer` who writes and maintains the :term:`source code` of a
    given application in response to support requests introduced by the
    :term:`site experts <site expert>` of the sites that run the application.

    Writes and maintains :term:`technical documentation` and a :term:`test
    suite` for the application.

    Writes :term:`release notes` for :term:`site experts <site expert>`.

    Centralizes the requirements of all users and negotiates priority conflicts.

  Server operator

    Operates a given :term:`Lino server`.

    Takes care for the reliable operation of the sites on a given server.

  Service provider

    A juridical or natural person who sells services to another :term:`community
    member`.

  Development provider

    A :term:`service provider` who provides :term:`developer services <developer
    service>` to their customers in order to help them with using a given
    :term:`software product`.  See :doc:`/dp`.

  Hosting provider

    A :term:`service provider` who runs and maintains one or several :term:`Lino
    servers <Lino server>`. See :doc:`/hp`.

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

  System administrator

      Manages the general IT system of a :term:`site operator`. Installs,
      configures and maintains :term:`client devices <client device>` as
      required.

  Release manager

      The contact person between the :term:`site operator` and the :term:`site
      maintainer`.

      Coordinates the activities before and after a :term:`site upgrade`.

  Site expert

    The contact person between the :term:`site operator` and the service
    providers involved with the :term:`Lino site`.

    Responds to support requests reported by :term:`key users <key user>`.

    :term:`server provider`
    :term:`application carrier`
    :term:`application programmer`.

    Formulates and explains the requirements of the :term:`site operator`
    regarding the :term:`Lino application`.

    Introduces :term:`expert support` requests to the :term:`application
    carrier` and answers to callback questions.

    Collaborates with the users in order to analyse their needs, and then
    explains to the :term:`application carrier` how to make or improve the
    application.

    Organizes training for :term:`key users <key user>`.

  Lino consultant

    Knows the possibilities and limitations of the :term:`Lino framework` and
    gives neutral advice about whether or not to choose Lino as a solution.
    Helps you with analyzing and formulating your needs and finding the right
    business partners who will implement a solution.

  Developer

      A physical person who develops a given :term:`software product`.

      A developer can act independently as a :term:`development provider`,
      or work for a legal person acting as :term:`development provider`.

  Programmer

      A physical person who writes, publishes, maintains and optimizes
      :term:`source files <source file>` of a :term:`source repository`
      according to the requirements of a :term:`development provider`.

  Software engineer

      A person who is not a :term:`developer` but is part of a developer team.

  Core developer

    A :term:`developer` who works for the :term:`core team`.

  Core team

    The team responsible for developing and maintaining the :term:`Lino
    framework`. Provides :term:`developer support` to :term:`application
    programmers <application programmer>`.
