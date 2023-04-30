.. _running:

*******************************
Running the Server and Clients
*******************************

Starting the Server
-------------------

The server is started by running the following command in the root directory of the framework:

.. code-block:: console

    cd server
    python start_server.py

Arguments that can be passed to the server are:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    --algorithm fedavg
    --clients 4
    --fraction none
    --rounds 8
    --model_path initial_model.pt
    --epochs 1
    --accept_conn 1
    --verify 0
    --threshold 0
    --timeout none
    --resize_size 32
    --batch_size 32
    --net LeNet
    --dataset MNIST
    --niid 2
    --carbon 0