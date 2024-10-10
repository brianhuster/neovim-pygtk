## Python Gtk GUI for Neovim

### Description
Python Gtk GUI for Neovim allows users to interact with Neovim through a graphical user interface (GUI) using the Gtk library.

### Running from Source
To run the application from the source code, you need to install some required packages. You can do this as follows:

#### Install the necessary dependencies:

```sh
sudo apt-get install -y gobject-introspection libgirepository1.0-dev
pip install .
```

#### Run the application:
```sh
python -m neovim_gui.cli
```

### License
This project is released under the Apache License 2.0.
