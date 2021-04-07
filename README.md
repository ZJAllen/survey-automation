# SurveyMonkey Automation

Automate a simple SurveyMonkey form. I try not to make any assumptions about what you do or don't know, so this should be a pretty thorough overview.

# Getting started

1. Navigate to a folder on your system, for example `Documents` or `Desktop`, where you want to save these files.
2. If you have `git` installed:
   1. Open a terminal window.
   2. Type `git clone https://github.com/ZJAllen/survey-automation.git`, which will download all of the files into a folder called `survey-automation`.
3. If you want to download the `zip` package:
   1. Click the `Code` dropdown and select `Download ZIP`.
   2. Unzip the folder and move it to wherever you'd like.
4. In your terminal, navigate into the just-created folder: `cd survey-automation`
5. Open the current directory in VS Code: `code .`

# Installation

## 1. Get the Chrome webdrivers

Head to [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) and follow the link according to your Chrome driver.

For example, if your Chrome version is 89, go [here](https://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/) and download the driver for your machine.

Unzip the file, and copy the `chromedriver.exe` file to somewhere on your machine's `PATH`. For example, if you are on Windows, copy it to `C:\Windows`. This way, Selenium will be able to find the correct driver without any further setup.

## 2. Create a virtual enviroment

Steps 2-4 are optional but recommended.

The exact syntax depends on how you start Python on your machine. It could be either of the following:

1. `python -m venv venv`
2. `py -m venv venv`
3. `python3 -m venv venv`
4. `py3 -m venv venv`

## 3. Activate your virtual environment

On Windows: `venv\Scripts\activate`
On Mac/Linux: `source venv/bin/activate`

(At any time, you can deactivate the virtual environment by typing `deactivate` in the terminal or by closing the terminal instance)

## 4. Upgrade pip...because it'll ask you to

`python -m pip install --upgrade pip`

## 5. Install the packages from the `requirements.txt`

`python -m pip install -r requirements.txt`

---

# Make sure you're all set

This is optional but will be a quick way to make sure your driver is ready to go.

While your virtual environment is activated start a Python shell and run the first import statement.
`>>> from selenium.webdriver import Chrome`

If you don't get any errors, you're good to go!

---

# Running the program

1. Update the `open_time` and `submit_time` variable according to your use case.
2. Update the `survey_url` variable to fit your survey. The default value is a simple test survey that I made.
3. In your terminal, run `python survey_automation.py`
4. Once the current time matches the `open_time`, a Chrome browser window will open. You must stay in this window since it is the only window the program has ahold of.
5. Fill out the information.
6. Once the current time matches the `submit_time` the form will be submitted and the window will be closed.
