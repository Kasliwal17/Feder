.. _overview:

*****************
Overview of Feder
*****************

Introduction
============

Federated Learning is a machine learning technique for training models on distributed data without sharing it. In traditional machine learning, large datasets must first be collected and then sent to one location where they can be combined before the model is trained on them. However, this process can cause privacy concerns as sensitive personal data may become publicly available. Federated learning attempts to address these concerns by keeping individual user's data local while still allowing for powerful powerful statistical analysis that can be used to create accurate models at scale.

**FedAvg** is one of the foundational blocks of federated learning. A single communication round of FedAvg includes:

* Waiting for a number of clients to connect to a server (Step 0)
* Sending the clients a  global model (Step 1)
* Train the model with locally available data (Step 2)
* Send the trained models back to the server (Step 3)

The server then averages the weights of the models and calculates a new aggregated model. This process constitutes a single communication round and several such communication rounds occur to train a model.

.. image:: ../imgs/fedavg_steps.png
   :align: center
..    :class: only-light

Overview
========

Feder is a highly dynamic and customizable framework that can accommodate many use cases with flexibility by implementing several functionalities over vanilla FedAvg, and essentially creating a plug-and-play architecture to accommodate different use cases.

Phases involved in Feder
------------------------

Feder is composed of 4 phases, each phase building upon the last.

1. **Phase 1: FedAvg.** The framework will be able to efficiently coordinate a server and some clients for a specific number of communication rounds, with granularity in selection of clients included.

2. **Phase 2: Verification.** Before aggregating, the server will perform a special verification round to determine which models to accommodate during aggregation.

3. **Phase 3: Timeout.** Instead of waiting indefinitely for a client to finish training, the server will be able to issue a timeout, upon the completion of which, even if it hasn’t completed all epochs, the client will stop training and return the results.

4. **Phase 4: Intermediate client connections.** New clients will be able to join the server anytime and may even be included in a round that is already live.

Phase 1: FedAvg
---------------

.. image:: ../imgs/phase1.png
   :align: center

|
|

Establishing Connection between Server and Clients
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../imgs/connection.png
   :align: center

|
|

Communication with clients
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../imgs/communication.png
   :align: center

|
|

Fractional and random subsampling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The Client_Manager can be used to sample the already connected clients.
* A minimum number of clients can be provided, upon which the Client_Manager will wait for that many clients to connect before returning a reference to them. 

   * If a fraction is provided, the Client_Manager will return that fraction of available clients.
   * The Client_Manager can sample the clients based on their connection order or a random order. A function can also be provided to determine the selection of clients.

Phase 2: Verification module
----------------------------

* After the server receives the trained weights, it aggregates all of them to form the new model. However, the selection of models for aggregation can be modified.
* Before aggregation, the server passes the models to a Verification module, which then uses a predefined procedure to generate scores for models, and then returns only those models that have performed above a defined threshold.
* The Verification module can be easily customized.

Steps in the Verification module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../imgs/verification_steps.png
   :align: center

Modified Federated Learning architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../imgs/verification.png
   :align: center

.. image:: ../imgs/verification1.png
   :align: center