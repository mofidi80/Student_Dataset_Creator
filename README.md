<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


 
<!-- PROJECT LOGO -->
<!-- <br />
<div align="center">
  <a href="https://github.com/mofidi80/Student_Dataset_Creator">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> 
  -->

<h3 align="center">Student Dataset Creator</h3>

  <p align="center">
    Making a sql dataset to keep track of student data.
    <br />
    <a href="https://github.com/mofidi80/Student_Dataset_Creator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
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
<!-- 
[![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Simple python script for creating a sql dataset to store student data along with a webcam picture of said student with coresponding name and id.

In the second year of my undergraduate degree one of my professors wanted to get to know the students of the class and asked us to take a selfie and send it to her; I thought it would be difficult to keep the data from all her classes organized so I wrote this script. She seemed to really like it though I don't know if she ended up using it later.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![opencv][opencv]][opencv-url]
* [![sqlite][sqlite]][sqlite-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
 
### Prerequisites

* Numpy
* sqlite3 (only in python ver < 2.5)
* opencv

### Installation

1. First you should install the following libraries for python.
* Numpy
  ```console
  pip install numpy
  ```

* opencv
  ```console
  pip install opencv-python
  ```

2. Download "haarcascade_frontalface_default.xml" from the repository.

3. Create a file named "face detection database.db"


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

As stated above this script is for creating a sql dataset to store student data along with a webcam picture of said student with coresponding name and id.


### Possible usage
This may be used to train a facial detection software for instance with python face_recognition library.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/mofidi80/Student_Dataset_Creator/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=mofidi80/Student_Dataset_Creator" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Mohammad Mofidi - https://www.instagram.com/_mohammadmofidi/ -- mohammad.mofidi.k@gmail.com


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/mofidi80/Student_Dataset_Creator.svg?style=for-the-badge
[contributors-url]: https://github.com/mofidi80/Student_Dataset_Creator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mofidi80/Student_Dataset_Creator.svg?style=for-the-badge
[forks-url]: https://github.com/mofidi80/Student_Dataset_Creator/network/members
[stars-shield]: https://img.shields.io/github/stars/mofidi80/Student_Dataset_Creator.svg?style=for-the-badge
[stars-url]: https://github.com/mofidi80/Student_Dataset_Creator/stargazers
[issues-shield]: https://img.shields.io/github/issues/mofidi80/Student_Dataset_Creator.svg?style=for-the-badge
[issues-url]: https://github.com/mofidi80/Student_Dataset_Creator/issues
[license-shield]: https://img.shields.io/github/license/mofidi80/Student_Dataset_Creator.svg?style=for-the-badge
[license-url]: https://github.com/mofidi80/Student_Dataset_Creator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mohammad-mofidi-khajeh-2715832b8/
[product-screenshot]: images/screenshot.png
[opencv]: https://img.shields.io/badge/opencv-brightgreen

[opencv-url]: https://opencv.org/
[sqlite]: https://img.shields.io/badge/sqlite-blue


[sqlite-url]: https://www.sqlite.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
# Student_Dataset_Creator
