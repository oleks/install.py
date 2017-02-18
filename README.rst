############################################################
``install.py`` — A simple, file-system-based install utility
############################################################

An installation makes certain files available under certain directories.

For instance:

1. Making executable files available in a directory listed in your ``PATH``
   environment variable.
2. Making system libraries available in a directory listed in your
   ``LIBRARY_PATH`` environment variable.
3. Making Python libraries available in a directory listed in your
   ``PYTHON_PATH`` environment variable.
4. Making git hooks available under a ``./.git/hooks`` directory.
5. Making configuration files (e.g., ``.vimrc``) available under your home
   directory.

``install.py`` aims to provide simple, reusable means to these ends.

Design Goals
============

In the following, the keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be
interpreted as described in [RFC 2119](http://tools.ietf.org/html/rfc2119)
(Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP
14, RFC 2119, March 1997).

1. ``install.py`` SHOULD be easy to use in (or adapt to) a small project.
2. ``install.py`` SHOULD be cross-platform.
3. ``install.py`` SHOULD make it easy to keep installed files up-to-date.

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
