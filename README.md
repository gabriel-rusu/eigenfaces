<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="./assets/face-scan.png" alt="Project logo"></a>
</p>

<h3 align="center">Eigenfaces</h3>


<p align="center"> 
    Face recognition algorithm that follows the observations from the research paper <i>Face Recognition Using Eigenfaces</i> to build a face space and find the projections of the train and test faces.
</p>

## 📝 Table of Contents
- [About](#about)
- [Quick Start](#quick_start)
- [Getting Started](#getting_started)
- [Built Using](#built_using)
- [Documentation](#documentation)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>
An eigenface is the name given to a set of eigenvectors when used in the computer vision problem of human face recognition. The approach of using eigenfaces for recognition was developed by Sirovich and Kirby and used by Matthew Turk and Alex Pentland in face classification. The eigenvectors are derived from the covariance matrix of the probability distribution over the high-dimensional vector space of face images.

In this repo, I reimplement the first face recognition algorithm from scratch to better understand the core concept behind eigenvectors and eigenfaces. I tried to keep the code well-organised and clean to make it helpful for others interested in the implementation
of this paper.

## ⚡ Quick Start <a name="quick_start"></a>

Want to play with these notebooks online without having to install anything? Use any of the following services.

<b>WARNING:</b> Please be aware that these services provide temporary environments: anything you do will be deleted after a while, so make sure you download any data you care about.

  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabriel-rusu/eigenfaces/blob/main/src/notebooks/collab-training.ipynb)

## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites
In order to locally run the repo you should have the following:
- [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html)


### Installing
If you want to run the code on your local machine, you need to follow the next steps.

 1. First you need to create a conda environment with the following command:

```bash
conda create --name eigenfaces --file requirements.txt python=3.10
```

  2. Secondly, you need to activate the environment:

```bash
conda activate eigenfaces
```
  3. Open in the editor of your choice the notebook eigenfaces from the folder src/notebooks


## ⛏️ Built Using <a name = "built_using"></a>
- [Jupyter Notebook](https://jupyter.org/) - web application for creating and sharing computational documents
- [Visual Studio Code](https://code.visualstudio.com/Download) - code editor
- [Python](https://www.python.org/downloads/) - programming language

## 📑 Documentation <a name="documentation"></a>
- The papers studied in order to implement the model are:
  - [Turk, Matthew & Pentland, A.P.. (1991). Face Recognition Using Eigenfaces. Proceedings IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR). 586 - 591. 10.1109/CVPR.1991.139758.](https://sites.cs.ucsb.edu/~mturk/Papers/mturk-CVPR91.pdf)
  - [Pentland, Moghaddam and Starner, "View-based and modular eigenspaces for face recognition," 1994 Proceedings of IEEE Conference on Computer Vision and Pattern Recognition, Seattle, WA, USA, 1994, pp. 84-91, doi: 10.1109/CVPR.1994.323814.](https://ieeexplore.ieee.org/abstract/document/323814)

## ✍️ Authors <a name = "authors"></a>
- [@gabriel-rusu](https://github.com/gabriel-rusu) - Idea & Initial work
