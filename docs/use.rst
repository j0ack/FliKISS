Use FliKISS
===========

General 
-------

**Login**

.. image:: /_static/login.png
    :align: center

To create/edit or delete a page, you must be logged in the FliKISS app.

Enter the password you registered in your :doc:`config file</config>`.

To log out, just click the link ``Logout`` at the bottom of your left menu.

**Edit**

To edit a page just click on the ``Edit`` link at the bottom of the page.

.. image:: /_static/edit.png
    :align: center

Once you have finish to edit a page just click on ``Save`` button to save your modifications.

**Create**

To create a new page enter its name in your browser address bar ``http://your-website.com/your-namespace/?page=Test`` and edit it.

To create a menu, create a new page called ``menu``.

.. note::
    Pages served at website and namespaces root are named ``index``
    

**Delete**

To delete a page edit it and remove its content.

Syntax
------

FliKISS supports `Markdown`_ syntax with several extensions.

**Table extension**

You can easily create HTML tables with this extension using the sytax established in `PHP Markdown extra`_.

Thus, the following text

.. code-block:: markdown

    My first header | My second header
    --------------- | ----------------
    Cell 1          | Cell 2
    Cell 3          | Cell 4

will be rendered as

+----------------+-----------------+
|My first header | My second header|
+================+=================+
|Cell 1          | Cell 2          |
+----------------+-----------------+
|Cell 3          | Cell 4          |
+----------------+-----------------+

    
**Codehilite extension**

The CodeHilite extension follows the same syntax as regular Markdown code blocks, with one exception. The hiliter needs to know what language to use for the code block.
It will use `Pygments`_ to highlight syntax.
If the first line begins with three or more colons, the text following the colons identifies the language. The first line is removed from the code block before processing and line numbers are not used::

.. code-block:: markdown

    :::python
    def main(*args) :
        """
            Main function
        """
        if 'i' in 'this is a test' :
            print 'test'
    
will be rendered as::
    
    def main(*args) :
        """
            Main function
        """
        if 'i' in 'this is a test' :
            print 'test'

**Inter pages links**

To make it easier to link content in your pages, FliKISS supports WikiLinks syntax.

It is possible to use a different label suffixing your link with a ``|`` and your label or to make links between namespaces, prefixing your link with your namespace and ``:``.

The following text

.. code_block:: markdown

    [[Index]]
    [[Index|Home]]
    [[wiki:Index|My index]]
    
will be rendered as

.. code_block:: html

    <a href="/?page=Index">Index</a>
    <a href="/?page=Index">Home</a>
    <a href="/wiki/?page=Index">My Index</a>
    
    
**Admonitions**

The Admonition extension adds admonitions to Markdown documents. FliKISS comes with ``Note`` and ``Warning`` classes support.

The following text

.. code_block:: markdown

    !!! Admonition_class "A title"
        My text
    
    !!! Note "A note"
        This is a note
    
    !!! Warning "A warning"
        This is a warning
        
will be rendered as

.. code_block:: html

    <div class="admonition Admonition_class">
      <p class="admonition-title">A title</p>
      <p>My text</p>
    </div>
    <div class="admonition note">
      <p class="admonition-title">A note</p>
      <p>This is a note</p>
    </div>
    <div class="admonition warning">
      <p class="admonition-title">A warning</p>
      <p>This is a warning</p>
    </div>

**Content alignment**

The Markdown syntax does not come with a functionnality to easily align your contents.

FliKISS comes with `Mou`_ syntax to center or right align your contents.

.. code_block:: markdown

    -> A center content <-
    -> A right align content ->

will be rendered as

.. code_block:: html

    <div style="display:block;text-align:center;"> A center content </div>
    <div style="display:block;text-align:right;"> A right align content </div>


**Drad and drop**

FliKISS editor supports HTML5 drag and drop API. If your browser supports it you can drop pictures directly in your editor to upload it.

You can also drop plain text files to fill your editor with its content.

.. _Markdown: http://daringfireball.net/projects/markdown/syntax
.. _PHP Markdown extra: http://www.michelf.com/projects/php-markdown/extra/#table
.. _Pygments: http://pygments.org
.. _Mou: http://25.io/mou/
