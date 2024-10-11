## Python Gtk GUI for Neovim

### Description
Python Gtk GUI for Neovim allows users to interact with Neovim through a graphical user interface (GUI) using the Gtk library. Fork of [neovim/python-gui](https://github.com/neovim/python-gui).

### Dependencies
A [Neovim](https://github.com/neovim/neovim) that must be executable via `nvim` command

### Install
```sh
pip install nvimgtk
```

If you are using Ubuntu 23.10 and later, you must use pipx instead of pip. Make sure you have pipx installed, and run
```sh
pipx install nvimgtk
```
If you encounter some issues, make sure to install the dependencies `gobject-introspection` and `libgirepository1.0-dev` first

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
