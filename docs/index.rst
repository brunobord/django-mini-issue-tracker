==================
Mini Issue Tracker
==================

Overview
========

This issue tracker is a very very very small (albeit very efficient) issue
tracker build on top of the automatic Django admin.

.. note::

    Please note that I (Bruno Bord) am not the original author of this piece
    of software. I first saw this on Django Snippets: http://djangosnippets.org/snippets/28/
    It's the work of Paul Bissex - Many thanks to him.

    This snippet was designed for older versions of Django, and I just thought
    it deserved a fresh new start, using the latest Django features.

Installation
============

Simply use pip::

    $ pip install issuetracker

Or you may want to use the github latest source, out of::

    https://github.com/brunobord/django-mini-issue-tracker

Anyway, you can use the application by:

* Add the ``issuetracker`` application in your ``INSTALLED_APPS``
* use ``syncdb`` to create the issue table in your database

If you're already using the automagic Django admin, there you are. You can start
adding your issues, sort them, filter them by priority, etc.

Done!
