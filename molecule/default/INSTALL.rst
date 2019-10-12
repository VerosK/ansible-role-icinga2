*******
Docker driver installation guide
*******

Requirements
============

* Docker Engine

Install
=======

Please refer to the `Virtual environment`_ documentation for installation best
practices. If not using a virtual environment, please consider passing the
widely recommended `'--user' flag`_ when invoking ``pip``.

.. _Virtual environment: https://virtualenv.pypa.io/en/latest/
.. _'--user' flag: https://packaging.python.org/tutorials/installing-packages/#installing-to-the-user-site

If you are using Python Virtual environment on SELinux enable system, don't forget
to add  `selinux` to the Virtual environemnt. Or use `togglesystempackages`.

.. code-block:: bash

    $ pip install 'molecule[docker]'
