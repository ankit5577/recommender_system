<!-- PROJECT LOGO -->
<p align="center">
    <h1 align="center">Recommender Systems 👨🏼‍💻</h1>

  <p align="center">
    <a href="https://github.com/ankit5577/recommender_system/issues">Report Bug</a>
    ·
    <a href="https://github.com/ankit5577/recommender_system/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This repository holds user & item based recommender systems in python 🧑🏽‍💻. 

### what is a recommender system? 🤔
Recommender systems are the systems that are designed to recommend things to the user based on many different factors

Types of recommender systems:
Collaborative Recommender system, Content-based recommender system, Demographic based recommender system, Utility based recommender system, Knowledge based recommender system and Hybrid recommender system & many more 🐣

### Types covered in this repository
 - Item Based 📱: form of collaborative filtering for recommender systems based on the similarity between items calculated using people's ratings of those items.
 - User Based 🙋‍♂️: model find relation between user to user & check probability of item getting selected by particular user.
 - Hybrid 👽: model find relations between items first then relations b/w users.
    <br>
    in short
   <br>
   It works as a item based recommender system first & after it switches to user based recommender.
   <br>
    still confused?
    <br>
   ```python
   if len(dataset > 100,000,000):
        itemBasedRecommender() # 🤧
   else:
        userBasedRecommender() # 🤡
   ```

### Built With
- Python3
- pandas
- numpy
- scipy
- tensorflow

<!-- GETTING STARTED -->
## Getting Started
you need a computer/laptop 🐒

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python - [https://www.python.org/downloads/](https://www.python.org/downloads/)
* Machine Learning libraries _tensorflow, pandas, numpy, scipy, nltk_:
    ```sh
    pip install tensorflow, pandas, numpy, scipy, nltk
    ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/ankit5577/upgrade-python-packages.git
   ```
2. Go to Folder
    ```
    cd code
    ```
3. Run Python File
   ```
   for user based recommender system
   python user_recommend.py
   
   for item based recommender system
   python item_based_filtering.py
   
   mixed recommender
   python recommender_system.py
   ```
   
<!-- USAGE EXAMPLES -->
## Usage
`clone the repo > run the recommender you want > let it train & run 🧑🏽‍💻`

<!-- CONTRIBUTING -->
## Contributing

**For AiBoost**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@ankit55771](https://twitter.com/ankit_ak1) - ankit@aiboost.in


<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/anki5577/recommender_system/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/anki5577/recommender_system/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/anki5577/recommender_system/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: hhttps://github.com/anki5577/recommender_system/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/anki5577/recommender_system/assets/LICENSE.txt
[linkedin-aiboost]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ankit5577
