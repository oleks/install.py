############################################################
``install.py`` — A simple, file-system-based install utility
############################################################

An installation makes certain files available under certain directories.

For instance:

1. Making an executable file available in a directory listed in your ``PATH``
   environment variable.
2. Making a library available in a directory listed in your ``LIBRARY_PATH``
   environment variable.
3. Making a git hook available under a ``./.git/hooks`` directory.
4. Making configuration files (e.g., ``.vimrc``) available under your home
   directory.

Design Goals
============

The ``install.py`` command-line utility aims to be a simple, file-system-based
installation utility that:

1. Is easy to use in a small project.
2. Is cross-platform.
3. Makes it easy to keep installed files up-to-date.

Related Tools
=============

``install.py`` takes inspiration from the |install_1|_ |GNU_coreutil|_, both in
terms of functionality, and the API.

.. |install_1| replace:: ``install(1)``
.. _install_1: http://man7.org/linux/man-pages/man1/install.1.html

.. |GNU_coreutil| replace:: GNU/Linux core utility
.. _GNU_coreutil: https://www.gnu.org/software/coreutils/coreutils.html

Implementation
==============

Most file-systems allow for files to be *copied* from one directory to another.
Copying has the down-side that a copy may become out of date with the source.
Some file-systems tackle this by allowing "symbolic links": files that
seamlessly refer to other files.
