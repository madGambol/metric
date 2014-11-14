======
metric
======

A Python library to gather own process metrics.

* Free software: Apache License, Version 2.0

Examples
--------

Get the used memory:

.. sourcecode:: python

    >>> import metric
    >>> metric.used_memory()


Get the used memory in specific units:

.. sourcecode:: python

    >>> metric.used_memory_bytes()
    >>> metric.used_memory_kilobytes()
    >>> metric.used_memory_megabytes()
    >>> metric.used_memory_gigabytes()

