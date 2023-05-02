.. _dataset:

*********
Datasets
*********

The datasets used by **feder** are acquired by fetching them from torchvision.datasets. As of now, feder supports the following datasets:

* MNIST
* FashionMNIST
* CIFAR10
* CIFAR100

Adding support for new datasets
-------------------------------
There are two methods for incorporating support for new datasets in feder. One involves utilizing torchvision.datasets, while the other entails implementing support for a custom dataset.

Using torchvision.datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The torchvision.datasets package consists of popular datasets used in computer vision. The datasets are downloaded and cached automatically. The datasets are subclasses of torch.utils.data.Dataset i.e. they have the same API. This makes it easy to incorporate support for new datasets in feder. All that is required is to add a a few lines of code in the get_data function in the get_data.py file.

.. code-block:: python

    def get_data(config):
    # If the dataset is not custom, create a dataset folder
    if config['dataset'] != 'CUSTOM':
        dataset_path = "client_dataset"
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)  
    
    # Get the train and test datasets for each supported dataset
    if config['dataset'] == 'MNIST':
        # Apply transformations to the images
        apply_transform = transforms.Compose([transforms.Resize(config["resize_size"]), transforms.ToTensor()])
        # Download and load the trainset
        trainset = datasets.MNIST(root='client_dataset/MNIST', train=True, download=True, transform=apply_transform)
        # Download and load the testset
        testset = datasets.MNIST(root='client_dataset/MNIST', train=False, download=True, transform=apply_transform)
    elif config['dataset'] == 'FashionMNIST':
        apply_transform = transforms.Compose([transforms.Resize(config['resize_size']), transforms.ToTensor()])
        trainset = datasets.FashionMNIST(root='client_dataset/FashionMNIST', train=True, download=True, transform=apply_transform)
        testset = datasets.FashionMNIST(root='client_dataset/FashionMNIST', train=False, download=True, transform=apply_transform)
    elif config['dataset'] == 'CIFAR10':
        apply_transform = transforms.Compose([transforms.Resize(config['resize_size']), transforms.ToTensor()])
        trainset = datasets.CIFAR10(root='client_dataset/CIFAR10', train=True, download=True, transform=apply_transform)
        testset = datasets.CIFAR10(root='client_dataset/CIFAR10', train=False, download=True, transform=apply_transform)
    elif config['dataset'] == 'CIFAR100':
        apply_transform = transforms.Compose([transforms.Resize(config['resize_size']), transforms.ToTensor()])
        trainset = datasets.CIFAR100(root='client_dataset/CIFAR100', train=True, download=True, transform=apply_transform)
        testset = datasets.CIFAR100(root='client_dataset/CIFAR100', train=False, download=True, transform=apply_transform)
    elif config['dataset'] == 'CUSTOM':
        apply_transform = transforms.Compose([transforms.Resize(config['resize_size']), transforms.ToTensor()])
        # Load the custom dataset
        trainset = customDataset(root='client_custom_dataset/CUSTOM/train', transform=apply_transform)
        testset = customDataset(root='client_custom_dataset/CUSTOM/test', transform=apply_transform)
    else:
        # Raise an error if an unsupported dataset is specified
        raise ValueError("Unsupported dataset type: {}".format(config['dataset']))
    
    # Return the train and test datasets
    return trainset, testset

For example, to add support for the STL10 dataset, the following lines of code can be added to the get_data function:

.. code-block:: python

    elif config['dataset'] == 'STL10':
        apply_transform = transforms.Compose([transforms.Resize(config['resize_size']), transforms.ToTensor()])
        trainset = datasets.STL10(root='client_dataset/STL10', split='train', download=True, transform=apply_transform)
        testset = datasets.STL10(root='client_dataset/STL10', split='test', download=True, transform=apply_transform)

