A Sport's website that consumes data from NewsAPI and displays the latest sport's news. The back end is build using Django. 
## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/paulmureithi/news_api_project.git
```

Create a virtual environment to install the packages in and activate it:

```sh
$ mkdir auth_project && cd auth_project
$ python3 -m venv venv
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.


## Screenshots
![image](https://user-images.githubusercontent.com/17989092/210066784-4aefaa00-7456-493f-b65e-81a893ab7988.png)
