Install FliKISS
===============

You need to have Python installed on your server to use FliKISS. The install script will download for you all the dependencies.

With pip
--------

If you already have ``pip`` installed on your server you can use it to install FliKISS

.. code-block:: bash

    $ pip install flikiss


It will download FliKISS from `Pypi`_

Without pip
-----------

You can install ``pip`` easily using your package manager or install FliKISS manually following these steps :

1. Get the last archive of `FliKISS`_
2. Extract it
3. Change path to extracted archive
4. Run ``python setup.py install``

.. note:: Virtualenvs note
          Keep in mind that OS will otfen require you to prefix the above commands with `sudo` in order to install the app system-wide.
          It is recommended to create a virtual environment for FliKISS via `virtualenv`_

.. _Pypi: http://pypi.python.org
.. _FliKISS: https://github.com/j0ack/flikiss/archive/master.zip
.. _virtualenv: http://www.virtualenv.org/
