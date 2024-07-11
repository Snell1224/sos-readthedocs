.. Copyright 2023 Sandia National Laboratories, LLC
   (c.f. AUTHORS, NOTICE.LLNS, COPYING)

   SPDX-License-Identifier: (LGPL-3.0)

.. Flux documentation master file, created by
   sphinx-quickstart on Fri Jan 10 15:11:07 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome To SOS Documentation!
====================================
.. image:: :ref:`<ovis-hpc:images/ovis-hpc_homepage.png>`
   :width: 1000
   :height: 150

The Scalable Object Store (SOS, pronuounced "sôs") is a high-performance, indexed, object-oriented database designed to efficiently manage structured data on persistent media.
SOS was created to solve performance and scalability problems found with other time series databases such as InfluxDB, OpenTSDB, and Graphite.
SOS is strictly typed and uses schema to define the objects stored in the database. The schema specifies the attributes that comprise the object and which attributes are indexed.

SOS implements its own back-end storage model. This allows SOS to support:

* Very high insert rates
* Superior query performance
* Flexible storage management

The Distributed Scalable Object Store (DSOS) (pronounced "dee-sôs") is a layer on top of SOS to enable distributed, parallel ingests and queries.
DSOS is intended to be used to use SOS databases across multiple devices as a unified database.
Users setup a file, referred to as the cluster configuration file in this context, which names all of the nodes where a SOS database is expected.
Using python API or the command line interface dsosql, users can query these SOS databases for data in the same schema.
DSOS interfaces are installed alongside SOS, starting with SOS v4, with no additional enable arguments required.
The DSOS python API is the currently supported query syntax for the OVIS Web Services Analysis and Visualization framework.

.. toctree::
   :maxdepth: 2
   :caption: Introduction to SOS

   sos-quickstart
   dsos-quickstart
   sos-tutorial

.. toctree::
   :maxdepth: 2
   :caption: SOS Man Pages

   sos_man/index
  
Other Projects
====================================
`ovis <https://github.com/ovis-hpc/ovis>`_
`ovis-publications <https://github.com/ovis-hpc/ovis-publications>`_
`maestro <https://github.com/ovis-hpc/maestro>`_
`baler <https://github.com/ovis-hpc/baler>`_
   








