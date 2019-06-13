========
Concepts
========

The components of a Lino project
================================

A **Lino application** is a software product written using the Lino framework,
having a given set of functions, designed to be run on one or several *Lino
sites*. A *Lino application* consists of a set of source code and documentation
files which are grouped and published in one or several code repositories.

The **Lino framework** consists of the *source code* and *documentation* that
are used and shared by several *Lino applications*. It consists of the *Lino
Core*, the *Lino Extensions Library* the  *Lino Book* and of the *Community
Guide*.

A **Lino site** is an instance of a *Lino application* which runs on a server
operated by a *site operator* and used by its *end users*.  Every *Lino site*
has its own domain or subdomain name, its own database, a set of local settings
and configuration files.

A **Lino server** is a virtual or physical machine used to run one or several
*Lino sites*.

Actors and their roles
======================

A **site operator** operates (runs) a given *Lino site*.  They are the owner of
the data stored on that site.  They are responsible for granting or revoking
access permissions to individual *end users* and for protecting that data
against leaking or other privacy issues.

An **application owner** decides about the destiny of a given Lino
application*.  They bring the idea into life, they decide which features to add
or to remove. they do strategic decisions like delegating responsibilities to
actors.  See also `Application ownership and copyright`_.

A **site administrator** manages a site via its web interface. They create
accounts for end users and can change configuration settings.

An **application developer** writes, maintains, optimizes and publishes the
source code and documentation of a *Lino application*.


A **core developer** writes, maintains , optimizes and publishes the source
code and documentation of the *Lino framework*.

A **system manager** is an actor who manages the IT system of his/her
employer or customer, who installs virgin Linux servers, cares about their
availability in a public or local network, who protects them against attacks
from the outside.


A **site administrator** is a person who installs and maintains a given

A **site manager** is a person who has full access to all functions provided
via the web interface

A **site coordinator** is a physical person who coordinates the requirements of
the *site operator* with the activities of developers and key users.

An **end user** is

A **key user** is

A **hosting provider** installs and maintain a server where

A **server provider** installs and maintain a server where your Lino
application will be running.  They care about reliability and make sure that
your Lino is always available to respond when you need it. They care about
security and protect your system against hackers. They make backups of your
data to make sure it doesn't get lost in case of a serious accident.  They care
about scaling. As your site will grow in terms of number of users and the
amount of data stored, you might want to move to a bigger machine.



Contracts
=========

A **development contract** is an agreement between a customer acting as *site
operator* and a provider acting as *developer*.

The customer designates and provides a *system administrator*, a *server
administrator* and a *site coordinator*.

Developers
==========

A **maintainer** is a person who maintains and increases the quality of a Lino
application

A **coder** is a person who modifies source code


Application ownership and copyright
===================================

All parts of the Lino framework are published as Free Software using the BSD
license.

The BSD license is more liberal than the GPL licenses in that it allows to
write even proprietary (non-free) extensions, applications, documentation or
otherwise derivated work.  Such work is not considered part of the *Lino
framework*. The Lino Community does neither prohibit nor support such work.


The **copyright holder** of source code or documentation is the actor who wrote
and published it. This is not the same as the *application owner* because all
source code and documentation is published as Free Software using the BSD
license.

Any other actor may decide at any moment to start a fork of application or to
use your application for their own purpose without even asking your permission.

Application ownership is not a legally defined term unless you use it in an
agreement, e.g. a maintenance contract.  Such documents should clearly state
who is the application owner and who is the copyright holder.



Miscellaneous
=============

An **actor** is a physical or legal person who assumes one or several roles
within our community.


An **end user** is a human who uses a given *Lino site* for their daily work.
As a Lino end user you should know how to contact your *support provider*.

A **support provider** is somebody who helps end users if they have a question.
The support provider is always available when end users need them. If they
cannot help directly, then they know how to ask other actors.


A **client device** is a device used by an *end user* to access a *Lino site*.


A **consultant** is somebody who knows the possibilities and limitations of the
Lino framework and helps you with analyzing your needs. They can give you
professional advice about whether or not to choose Lino as a solution.

A **hoster** is somebody who sets up a server with a Lino site and who helps
users to connect to that server.
A **hosting provider** does the same, but as a third-party company and not as
employee of the site owner.

An **application developer** is somebody who writes or maintains Lino
applications.  A **core developer** is somebody who writes or
maintains general core features of the Lino framework.

An **analyst** is somebody who collaborates with users in order to
analyze their needs, and who then explains to the *application
developer* how to make the application better (or how to make it at
all, in case of new development projects).

A **trainer** is somebody who can explain a given Lino application to
its users. Trainers also write documentation for users.




Lino hosting contracts
======================

There are three types of hosting services:

- in case of **server hosting** the hoster is *not reponsible* for
  *end-user support* and *regular maintenance*.  The site owner needs a
  second agreement with a *developer* or *deployer* for these.

- in case of **stable hosting** the hoster also offers these services,
  i.e. they answer end-user questions about how to use or configure the
  software, and they are able upgrade the site when new versions of the
  software are available. They forward any reported
  problems to the responsible application or core developer.

- in case of **development hosting** the hoster additionally provides
  end-user support and maintenance of a Lino application.


Server hosting
==============

In case of **server hosting** the site operator has two contracts: one with a
developer and one with a hoster.

Your job is to provide and manage the server where the developer will
install and maintain Lino. You make sure that the server is available
and secure. You collaborate with the developer for certain tasks like
mail server setup.

You are *not* reponsible for maintaining the system software on that
server, nor answering end-user questions about how to use or configure
the software. That's the job of the developer.

You are able to act as **emergency maintainer**.  An emergency maintainer knows
how Lino is installed on the server  and how to react in certain situations:

- connection problems caused by the end-user's machine
- diagnose and fix server-side problems like performance
- get the server back to work after a technical problem

It is also your emergency maintainer who will decide whether and when
you are able to offer **stable hosting** for one or several Lino
applications.

.. _stable_hosting:

Stable hosting
==============

The difference between development and stable hosting is that your
emergency maintainer has grown into an independent maintainer who can
maintain the system software, give limited end-user support and
install new versions of the application when the customer asks you to
do so.  In stable mode, the customer pays more money to you because
you provide additional services and because they don't need support by
a developer.  With stable hosting, no external developer has access to
your customer's server.

Development hosting
===================

In case of **development hosting** you offer both the hosting and the
development.


..
    A **master machine** is a virtual machine which hosts one or several
    demo sites on different Lino versions.

    customized for you by a
    developer

    You can set up and maintain a docker server and serve one of the
    dockerfiles maintained by the Lino team.  See e.g.
    https://docs.docker.com/engine/installation/linux/ubuntulinux/

    With Docker hosting the customer is always in stable mode and cannot
    switch to development mode.

    The Lino team plans to start this type of hosting as soon as there is
    a first pilot user.
