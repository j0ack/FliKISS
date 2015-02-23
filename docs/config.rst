FliKISS config
==============

By default FliKISS will look for a config file in your home ``$HOME/.flikissrc``.

You can use an alternate config file using the command's ``config`` parameter (see the :doc:`Run section </run>` for more details).

Settings are configured in the form of a Python module (a file) and need to respect the Python syntax. All the setting identifiers must be set in all-caps, otherwise they will not be processed.

Here is a list of settings you can overwrite : 

+--------------------------------------+-------------------------------------+
|Setting name(default value)           | What does it do                     |
+======================================+=====================================+
| *PASSWORD* (``password``)            | Password to create or edit files    |
+--------------------------------------+-------------------------------------+
| *PAGES_DIR* (``$FliKISS_path/pages``)| Absolute path to store your contents|
+--------------------------------------+-------------------------------------+
| *MEDIA_DIR* (``$FliKISS_path/media``)| Absolute path to store your media   |
+--------------------------------------+-------------------------------------+
| *NAMESPACES* (``[]``)                | You can use namespaces to categorize|
|                                      | your pages. Namespaces are like new |
|                                      | FliKISS instances, with their own   |
|                                      | menu and pages. While pages are     |
|                                      | similar to files, namespaces are    |
|                                      | similar to folders. Each namespace  |
|                                      | will be served on a sub-url using   |
|                                      | its name (for example a namespace   |
|                                      | named `wiki` will be served on      | 
|                                      | `http://your-servername.com/wiki/`) |
+--------------------------------------+-------------------------------------+

Here is an example of valid config file::

    PASSWORD = 'A_password_very_hard_to_find'
    PAGES_DIR = '/home/test/wiki/pages/'
    MEDIA_DIR = '/home/test/wiki/media'
    NAMESPACES = ['wiki','test']


.. warning::
    FliKISS does not need a config file to be run, but you **should** create one to overwrite at least the default password(``password``).
