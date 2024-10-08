.. PyNinja documentation master file, created by
   sphinx-quickstart on Sat Aug 10 21:49:31 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyNinja's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   README

PyNinja - Main
==============

.. automodule:: pyninja.main

PyNinja - Executors
===================

API Authenticator
-----------------
.. automodule:: pyninja.executors.auth

Database
--------
.. automodule:: pyninja.executors.database

API Routes
----------
.. automodule:: pyninja.executors.routes

Squire
------
.. automodule:: pyninja.executors.squire

PyNinja - Features
==================

CPU
---
.. automodule:: pyninja.features.cpu

Disks
-----
.. automodule:: pyninja.features.disks

Docker
------
.. automodule:: pyninja.features.dockerized

GPU
---
.. automodule:: pyninja.features.gpu

Operations
----------
.. automodule:: pyninja.features.operations

Process
-------
.. automodule:: pyninja.features.process

Service
-------
.. automodule:: pyninja.features.service

PyNinja - Modules
=================

Exceptions
----------
.. automodule:: pyninja.modules.exceptions

Models
------
.. autoclass:: pyninja.modules.models.Payload(BaseModel)
   :exclude-members: _abc_impl, model_config, model_fields, model_computed_fields

====

.. autoclass:: pyninja.modules.models.ServiceStatus(BaseModel)
   :exclude-members: _abc_impl, model_config, model_fields, model_computed_fields

====

.. autoclass:: pyninja.modules.models.DiskLib(BaseModel)
   :exclude-members: _abc_impl, model_config, model_fields, model_computed_fields

====

.. autoclass:: pyninja.modules.models.ServiceLib(BaseModel)
   :exclude-members: _abc_impl, model_config, model_fields, model_computed_fields

====

.. autoclass:: pyninja.modules.models.ProcessorLib(BaseModel)
   :exclude-members: _abc_impl, model_config, model_fields, model_computed_fields

====

.. autoclass:: pyninja.modules.models.Session(BaseModel)
   :exclude-members: _abc_impl, model_config, model_fields, model_computed_fields

====

.. autoclass:: pyninja.modules.models.RateLimit(BaseModel)
   :exclude-members: _abc_impl, model_config, model_fields, model_computed_fields

====

.. autoclass:: pyninja.modules.models.EnvConfig(BaseModel)
   :exclude-members: _abc_impl, model_config, model_fields, model_computed_fields

====

.. automodule:: pyninja.modules.models
   :exclude-members: Payload, ServiceStatus, DiskLib, ServiceLib, ProcessorLib, EnvConfig, Session, RateLimit, env, database

RateLimit
---------
.. automodule:: pyninja.modules.rate_limit

Secure
---------
.. automodule:: pyninja.modules.secure

PyNinja - Monitor
=================

Authenticator
-------------
.. automodule:: pyninja.monitor.authenticator

Configuration
-------------
.. automodule:: pyninja.monitor.config

Resources
---------
.. automodule:: pyninja.monitor.resources

Routes
------
.. automodule:: pyninja.monitor.routes

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
