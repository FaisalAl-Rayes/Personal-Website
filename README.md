<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- CONTACT ME -->
You can connect with me through LinkedIn using the link the following link: [![LinkedIn][linkedin-shield]][linkedin-url]

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
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#prometheus">Prometheus</a></li>
        <li><a href="#grafana">Grafana</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![website-preview][website-preview]<!-- (https://mydomain.com) -->

This is a project to share my approach to building my own website using many different technologies that can be seen in the <a href="#built-with">Built With</a> section. I have used  <a href="https://www.html5up.net/">HTML5UP</a> for the HTML templates and some images from <a href="https://www.unsplash.com/">Unsplash</a>. The motivation behind this project is to illustrate some experience working with the technologies involved in building this project as well as managing it.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* [![Docker][Docker]][Docker-url]
* [![Gunicorn][Gunicorn]][Gunicorn-url]
* [![PostgreSQL][PostgreSQL]][PostgreSQL-url]
* [![Prometheus][Prometheus]][Prometheus-url]
* [![Grafana][Grafana]][Grafana-url]
* [![Nginx][Nginx]][Nginx-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Here are the sequential steps to up and running!

### Prerequisites

* Ensure that you have docker installed on your machine. To install docker please follow the instructions of installation in <a href="https://www.docker.com/">Docker's Official Website</a>
respectively.

* Ensure that docker and docker compose work by getting a response that looks like this
  ```sh
  ~$ docker --version
  Docker version XX.XX.XX ...
  ```
  ```sh
  ~$ docker compose version
  Docker Compose version vX.XX.X ...
  ```

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/FaisalAl-Rayes/Personal-Website.git
   ```

2. Remove the suffix of ".example" from all files that have it. For instance
   ```sh
   ".env.example" file should be renamed to ".env"
   "db_password.secret.example" file should be renamed to "db_password.secret"
   ```

3. Enter your desired values to these former "*.example" files for example in `web_project/web/.env` (Should be done to all the *.example files)
   ```sh
   "DATABASE_NAME=YOUR_DB_NAME" ---> "DATABASE_NAME=somename"
   ```
   NOTE:  If you want to run it with the dummy values in the *.example files then just step 2 should be enough.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

In this section you can see how to check how to use some additions to the website such as prometheus and grafana.

### Prometheus
* Go to `http://localhost:9090/targets?search=` and you should see the following
   ![prometheus-targets][prometheus-targets]

### Grafana
1. Go to `http://localhost:3000` and you should see the following
   ![grafana-login][grafana-login]

2. Login with username `admin` and password `admin` (yes the username and password are the same)
    ```sh
    Email or username: admin
    Password: admin
    ```

3. You will be prompted to change the password so do so
    ```sh
    New password: YOUR_PASSWORD
    Confirm new password: YOUR_PASSWORD
    ```

4. Now you should be in the welcome panel
    ![grafana-welcome-page][grafana-welcome-page]

5. Click on `DATA SOURCES` and the select `Prometheus`

6. Set `Prometheus server URL` to `http://prometheus:9090` then scroll down and click on `Save & test`

7. Click on the `Import dashboard` shown below
    ![grafana-datasources][grafana-datasources]

8. Enter `17658` in the `Import via grafana.com` section to get the <a href="https://grafana.com/grafana/dashboards/17658-django/">django prometheus dashboard</a> then click on the `Load` button as shown below
    ![grafana-import-dashboard][grafana-import-dashboard]

9. Select `Prometheus (default)` in the `Select a Prometheus data source` dropdown menu and then click on `Import` and you will see the dashboard displayed as seen below
    ![grafana-django-prometheus-dashboard][grafana-django-prometheus-dashboard]



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



<!-- LICENSE 
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- CONTACT -->
## Contact
Connect with me on 

[![LinkedIn][linkedin-shield]][linkedin-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template/)
* [HTML5 UP](https://www.html5up.net/)
* [Django Prometheus Exporter Dashboard for Grafana](https://www.grafana.com/grafana/dashboards/17658-django/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/linkedin-0769AD?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/faisalalrayyess

[website-preview]: readme_images/Website/preview.png
[prometheus-targets]: readme_images/Prometheus/targets.png
[grafana-login]: readme_images/Grafana//login.png
[grafana-dashboard]: readme_images/Grafana//dashboard.png
[grafana-welcome-page]: readme_images/Grafana//welcome_page.png
[grafana-datasources]: readme_images/Grafana//datasources.png
[grafana-import-dashboard]: readme_images/Grafana//import_dashboard.png
[grafana-django-prometheus-dashboard]: readme_images/Grafana//django_prometheus_dashboard.png

[Python]: https://img.shields.io/badge/python-306998?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Django]: https://img.shields.io/badge/django-092e20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/

[Docker]: https://img.shields.io/badge/docker-0769AD?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/

[Prometheus]: https://img.shields.io/badge/prometheus-f4581e?style=for-the-badge&logo=prometheus&logoColor=white
[Prometheus-url]: https://www.prometheus.io/

[Nginx]: https://img.shields.io/badge/ngnix-009900?style=for-the-badge&logo=nginx&logoColor=white
[Nginx-url]: https://www.nginx.com/

[Grafana]: https://img.shields.io/badge/grafana-000000?style=for-the-badge&logo=grafana&logoColor=orange
[Grafana-url]: https://www.grafana.com/

[PostgreSQL]: https://img.shields.io/badge/postgresql-0064a5?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/

[Gunicorn]: https://img.shields.io/badge/gunicorn-309421?style=for-the-badge&logo=gunicorn&logoColor=white
[Gunicorn-url]: https://jquery.com 