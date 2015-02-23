Run FliKISS
===========

Command
-------

FliKISS comes with the command ``flikiss`` to launch a `CherryPy`_ server to serve the application. 
    
If you have installed it in a virtualenv you need to prefix it with your virtualenv path : ``$PATH_TO_VIRTUALENV/bin/flikiss``

.. code-block:: bash

    $ flikiss --ip 127.0.0.1 --port 8000 --url / --config /home/test/.flikissrc
  
.. option:: -i, --ip

            determine the host to serve the application (default=127.0.0.1)
    
.. option:: -p, --port

            determine the port to serve the application (default=8000)
    
.. option:: -u, --url

            determine the url to serve the application (default=/)
    
.. option:: -c, --config

            alternate config file

That's it, FliKISS now run on the port given in argument you can then access it at ``http://ip:port/url/``

Run in background
-----------------

FliKISS does not come with something build for this. You have several solutions.

Shell background process
^^^^^^^^^^^^^^^^^^^^^^^^

To run a command in background you can run it in a shell background process with ``nohup``

.. code-block:: bash

    $ nohup your_app [-options]
    
Or run it in a `screen`_

.. code-block:: bash

    $ screen
    $ flikiss [-options]

Press ``Ctrl`` + ``A`` then ``d``. Your session keep going on in background.

Supervisor
^^^^^^^^^^

`Supervisor`_ is a program to manage processes, it can be easily installed using your package manager or ``pip``.

Create a configuration file ``/etc/supervisor/conf.d/your-app.conf``

.. code-block:: ini

    [program:your-app]
    command=your-app [-options]
    directory=/path-to-home/
    environment=HOME='/path-to-home/'
    autostart=true
    autorestart=true
    
Then you need to enable your config file using as root

.. code-block:: bash

    # supervisorctl update
    # supervisorctl start your-app

.. _CherryPy: http://cherrypy.org
.. _screen: http://linuxcommand.org/man_pages/screen1.html
.. _Supervisor: https://pypi.python.org/pypi/supervisor
