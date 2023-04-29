.. _overview:

Overview
========

Introduction
^^^^^^^^^^^^

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

Feder is a highly dynamic and customizable framework that can accommodate many use cases with flexibility by implementing several functionalities over vanilla FedAvg, and essentially creating a plug-and-play architecture to accommodate different use cases.
