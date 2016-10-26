# Project Title

Check the duration of you lecture using python module.


### Prerequisites

What things you need to install the software and how to install them

```
1. You will need Python 3.5.
2. moviepy 0.2.2.11
3. pip is recommended for installing dependencies.
```

### Installing

Let us see the installation so that you can use it in your local machine.

you must have pip and python installed in your system.


```
https://pypi.python.org/pypi/pip
```

```
pip install moviepy
```


## Running the tests

using command line
```
python final_length.py
```


## Usage

```
from moviepy.editor import VideoFileClip

video = VideoFileClip("myHolidays.mp4").subclip(50,60)
video.duration


```


## Built With

* [Python 3.5](https://www.python.org/downloads/release/python-350/) - programming language used
* [moviepy 0.2.2.11](https://pypi.python.org/pypi/moviepy) - Video editing with Python


## Motivation

* check how many hours you have to study for any course.
* Make your Routine on the basis of this



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details





