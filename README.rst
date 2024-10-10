==============================
Python Gtk GUI for Neovim
==============================

Description
-----------
Python Gtk GUI for Neovim allows users to interact with Neovim through a graphical user interface (GUI) using the Gtk library.

Running from Source
-------------------
To run the application from the source code, you need to install some required packages. You can do this as follows:

1. Install the necessary dependencies:

   .. code-block:: bash

      sudo apt-get install -y gobject-introspection libgirepository1.0-dev

2. Install the project:

   .. code-block:: bash

      pip install .

3. Run the application:

   .. code-block:: bash

      python -m neovim_gui.cli

License
-------
This project is released under the Apache License 2.0.
