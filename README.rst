###########################################
A simple, file-system-based install utility
###########################################

.. image:: https://img.shields.io/travis/oleks/install.py.svg
   :target: https://travis-ci.org/oleks/install.py

Background
==========

An installation makes certain files available under certain directories.

For instance:

1. Making executable files available under a directory listed in your
   ``PATH`` environment variable.
2. Making system libraries available under a directory listed in your
   ``LIBRARY_PATH`` environment variable.
3. Making Python libraries available under a directory listed in your
   ``PYTHON_PATH`` environment variable.
4. Making Git hooks available under a ``.git/hooks`` directory (or
   ``.git\hooks`` on Windows).
5. Making configuration files (e.g., ``.vimrc``) available under your home
   directory.

``install.py`` aims to provide simple, robust, and reusable means to these
ends, and beyond.

Analysis
========

Design Goals
------------

In the following, the keyword "SHOULD" is to be interpreted as described in
`RFC 2119`_.

.. _RFC 2119: http://tools.ietf.org/html/rfc2119

1. ``install.py`` SHOULD be easy to use in, or adapt to a small project.
2. ``install.py`` SHOULD be cross-platform.
3. ``install.py`` SHOULD make it easy to keep installed files up-to-date.

Symbolic Links
--------------

Most file-systems allow for files to be *copied* from one directory to another.
Copying has the down-side that a copy may become out of date with the source.
Some file-systems tackle this by allowing "symbolic links": files that
seamlessly refer to other files.

Symbolic links are generally available in contemporary file-systems for
Unix-like operating systems and on Windows since Windows 6.0 (Vista).

Related Tools
=============

* |install_1|_ |GNU_coreutil|_

.. |install_1| replace:: ``install(1)``
.. _install_1: http://man7.org/linux/man-pages/man1/install.1.html

.. |GNU_coreutil| replace:: GNU/Linux core utility
.. _GNU_coreutil: https://www.gnu.org/software/coreutils/coreutils.html

Implementation
==============

The utility is implemented as a standalone Python file, |install_py|_.

User Guide
==========

Where is the Python script?
---------------------------

To ensure proper accreditation, manage releases, and reduce code
duplication, ``install.py`` is generated from `an m4 template
<install.py.m4>`_. To get the shell script, either:

  1. Fetch the
     `latest <https://github.com/oleks/install.py/releases/latest>`_
     `release <https://github.com/oleks/install.py/releases>`_
     of the shell script, or;
  2. Type ``make`` to build it, if you happen to have the
     `m4 macro processor <https://www.gnu.org/software/m4/m4.html>`_
     installed.

     Please note, the last step of building ``install.py`` is to
     execute ``git-ready-to-deploy.sh``. This ensures a clean release
     of ``install.py``, so long as you mind the exit code of ``make``.

What do I do with the Python script?
------------------------------------

Copy ``install_py`` into the directory containing the files that you would like
to install. Create an INI file, (e.g., called ``config.ini``) having a
``install.py`` section with the properties ``src_dir``, ``dst_dir``, and
``files``. The values of the properties may be arbitrary Python expressions,
evaluating to the types ``str``, ``str``, and ``List[str]``, respectively. This
is to allow you to specify the configuration in a platform-independent way.

For instance, you might have a ``hooks`` directory in your Git repository,
having an |install_py|_, and a ``config.ini`` that looks like this:

.. code:: python

  [install.py]
  src_dir = os.path.dirname(__file__)
  dst_dir = os.path.join(src_dir, '..', '.git', 'hooks')
  files = ['pre-commit', 'pre-push']

This will take the location of the executing |install_py|_ as ``src_dir``, its
sibling directory ``../.git/hooks/`` (or ``..\.git\hooks`` on Windows) as
``dst_dir``, and look for the files ``pre-commit`` and ``pre-push`` to install
from ``src_dir`` into ``dst_dir``.

.. |install_py| replace:: ``install.py``
.. _install_py: install.py
