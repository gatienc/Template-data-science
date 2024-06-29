<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- [![Contributors][contributors-shield]][contributors-url] -->
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-border.json)](https://github.com/copier-org/copier)
[![GitHub license](https://img.shields.io/github/license/gatienc/{{project_name}})](https://github.com/gatienc/{{project_name}}/blob/master/LICENSE)
[![GitHub commits](https://badgen.net/github/commits/gatienc/{{project_name}})](https://GitHub.com/gatienc/{{project_name}}/commit/)
[![GitHub latest commit](https://badgen.net/github/last-commit/gatienc/{{project_name}})](https://gitHub.com/gatienc/{{project_name}}/commit/)
[![Author](https://img.shields.io/badge/author-@gatienc-blue)](https://github.com/gatienc)


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/gatienc/# {{project_name}}
">
    <!-- <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center"># {{project_name}}
</h3>

  <p align="center">
    
    {{description}}

  <br />
    <!-- <a href="https://github.com/gatienc/# {{project_name}}
"><strong>Explore the docs »</strong> -->
    </a> 
    <br />
    <br />
    <!-- <a href="https://github.com/gatienc/# {{project_name}}
">View Demo</a> -->
    
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href=#project-organization>Project Organization</a></li>
    <li><a href=#acknowledgements> Acknowledgements</a></li>
    <li><a href="#contact">Contact</a></li>
      </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<!--
[![Product Name Screen Shot][product-screenshot]](https://example.com) -->

{{description}}

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Python

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/gatienc/{{project_name}}
   ```
2. Install dependencies
    ```sh
    {% if virtual_env=="venv" %}
    pip install -r requirements.txt
    {% elif virtual_env=="poetry" %}
    poetry install
    {% endif %}
   ```
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project Organization

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <- Data folder for the project
    │
    ├── docs               <- A MkDocs documentation
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks.
    │                         
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── ? requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │  
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make predictions
        │                   
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py

## Contact

Gatien Chenu - gatien_dev@chenu.me

Project Link: https://github.com/gatienc/{{project_name}}/issues

<p align="right">(<a href="#readme-top">back to top</a>)</p>

