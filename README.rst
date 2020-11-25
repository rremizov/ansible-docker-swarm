.. sectnum::

Docker Swarm
============

.. image:: https://travis-ci.com/rremizov/ansible-docker-swarm.svg?branch=master

Create and manage Docker Swarm.

Requirements
------------

- Debian 10
- Docker Engine

Role Vars
---------

``docker_swarm_state``
~~~~~~~~~~~~~~~~~~~~~~

Passed as is to the `docker_swarm`_ module.
Set to ``present`` to create a new single-node cluster or ``join`` an existing cluster.

``docker_swarm_advertise_addr``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Passed as is to the `docker_swarm`_ module. Optional.

``docker_swarm_node_role``
~~~~~~~~~~~~~~~~~~~~~~~~~~

Passed as is to the `docker_node`_ module.

``docker_swarm_node_labels``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Passed as is to the `docker_node`_ module. Optional.

``docker_swarm_managers``
~~~~~~~~~~~~~~~~~~~~~~~~~

A list of inventory hostnames of the manager nodes. Used to update the state of worker nodes.

``docker_swarm_remote_addrs``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Passed as is to the `docker_swarm`_ module. Used to join new nodes.

``docker_swarm_secrets``
~~~~~~~~~~~~~~~~~~~~~~~~

List of dictionaries with keys ``key``, ``value``, ``state``. Optional.

Example
-------

Create a new swarm
~~~~~~~~~~~~~~~~~~

.. code:: yaml

    # host_vars/node-0.yml
    docker_swarm_state: present
    docker_swarm_node_role: manager

    # host_vars/node-1.yml
    docker_swarm_state: join
    docker_swarm_node_role: worker
    docker_swarm_managers: ["node-0"]
    docker_swarm_remote_addrs:
      - "{{ hostvars['node-0']['ansible_default_ipv4']['address'] }}"

    # host_vars/node-2.yml
    docker_swarm_state: join
    docker_swarm_node_role: worker
    docker_swarm_managers: ["node-0"]
    docker_swarm_remote_addrs:
      - "{{ hostvars['node-0']['ansible_default_ipv4']['address'] }}"

Set Node Labels
~~~~~~~~~~~~~~~

.. code:: yaml

    docker_swarm_node_labels:
      label0: value0
      label1: value1
      label2: value2

Create secrets
~~~~~~~~~~~~~~

.. code:: yaml

    docker_swarm_secrets:
      - name: secret-name-0
        value: secret-value-0
        state: present
      - name: secret-name-1
        value: secret-value-1
        state: absent

.. _docker_swarm: https://docs.ansible.com/ansible/latest/modules/docker_swarm_module.html
.. _docker_node: https://docs.ansible.com/ansible/latest/modules/docker_node_module.html
