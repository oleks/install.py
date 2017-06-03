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
4. Making git hooks available under a ``./.git/hooks`` directory.
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

Copy |install_py|_ into the directory containing the files that you would like
to install. Create an INI file, (e.g., called ``install.ini``) having a
``default`` section with the properties ``src_dir``, ``dst_dir``, and
``files``. The values of the properties may be arbitrary Python values. This is
to allow you to specify the configuration in a platform-independent way.

For instance, you might have a ``hooks`` directory in your Git repository,
having an |install_py|_, and an ``install.ini`` that looks like this:

.. code:: python

  [default]
  src_dir = os.path.dirname(__file__)
  dst_dir = os.path.join(src_dir, '..', '.git', 'hooks')
  files = ['pre-push']

.. |install_py| replace:: ``install.py``
.. _install_py: install.py
