import platform
import sys

from setuptools import setup

install_requires = [
    'pynvim>=0.1.3',
    'click>=3.0',
    'pygobject'
]
ext_modules = None

# Cythonizing screen.py to improve scrolling/clearing speed. Maybe the
# performance can be improved even further by writing a screen.pxd with
# static type information
try:
    from Cython.Build import cythonize
    ext_modules = cythonize('neovim_gui/screen.py')
except ImportError:
    pass

entry_points = {'console_scripts':  ['nvimgtk=neovim_gui.cli:main']}

setup(
    name='nvimgtk',
    version='1.0.0',
    description='Gtk gui for neovim',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='Apache',
    packages=['neovim_gui'],
    install_requires=install_requires,
    ext_modules=ext_modules,
    entry_points=entry_points,
    zip_safe=False)
