# Enigma Public Data Viz Info Session

The goal of the info session is to show a simple pipeline from Public SDK through to a web app data visualization, introducing some interesting and popular tools along the way.

However, there is a lot of scaffolding that goes into getting everything to play nicely together, that we will not have time for in the session. This repo contains a working version of this scaffolding, and the steps below go into how to get everything set up on your personal machine.

It is recommended that you take the time to read on the components set up in this repo. Check the Further Reading section to find links to relevant documentation for everything in this repo, which we may not have time for in the info session.

Also, if you get stuck, or you find there's a missing step somewhere in this document, raise an issue on the Github repo as soon as you can. It's the quickest way to get help, and public enough that once it is solved, anybody else who runs into the same problem will be able to see the discussion.

## Structure

The structure of the project is a fairly simple one, there is a `backend/` directory, and a `frontend/` directory.

`backend/` contains a simple Flask app, which will be our web server. Once our info session is complete, this Flask app will have an endpoint open that retrieves data from Enigma Public using the Python SDK, pushes it through a simple PySpark pipeline, and returns the output in a form that the frontend will be able to render.

`/frontend` contains a React app, upon loading the webpage, it will make a call to our backend's endpoint, and after the response is received, pass it through D3 to get a nice visalization of the data.

## Getting Started

Make sure you have everything installed from the Requirements section. After that, move on to the Setup Guide section.

### Requirements

* [python3 and pip (pip typically comes with python)](https://realpython.com/installing-python/)
* [node.js >=6](https://nodejs.org/en/)
* [npm >= 5.2](https://www.npmjs.com/get-npm)
* [Java8](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) 

### Setup Guide

Setup should be very painless, as long as you have all of the pre-requirements correctly installed.

*NOTE: In some installations of python on Mac OS, `python` points to python2, and you need to use `python3` instead. You can run `python --version` to see whether it's python2 or 3. If it's python2, use `python3 --version`. If that is python3, substitute `python` for `python3` in the below instructions*

Make sure this repository is cloned onto your machine, and with terminal open, do the following **($ are your inputs, > is expected outputs)**

MAC OS / Linux:
```
$ cd /into/root/of/repository
$ pip install virtualenv
$ python manage.py install
    > Installing
    > ...
```
Windows:
```
$ cd /into/root/of/repository
$ py -m pip install virtualenv
$ py manage.py install
    > Installing
```


Once your development environment is finished installing, you can run the backend server in debug mode using the following command:


Mac OS / Linux:
```
$ python manage.py run-backend
    > Launching backend
    > ...
```

Windows:
```
$ py manage.py run-backend
    > Launching backend
    > ...
```

And the frontend server *(note to run both at the same time, will require (for example) two terminal tabs)*:


Mac OS / Linux

```
$ python manage.py run-frontend
    > Launching frontend
    > ...
```

Windows:
```
$ py manage.py run-frontend
    > Launching frontend
    > ...
```

To exit either the backend or frontend server, use `ctrl + c`.

### Smoketest

With the backend server running, hit the following url:

```
http://127.0.0.1:5000/smoketest
```

If you get `Smoke Test PASS`, the backend server is properly configured. For other messages, check the terminal to see what printed out. Make sure you have all the pre-requirements installed. Remember to raise any issues on the [github issues page](https://github.com/sam-the-enigma/publicdataviz/issues).

## Further Reading

* [Enigma SDK documentation](https://docs.enigma.com/public/public_v20_sdk_about.html)
* [Flask documentation](https://flask.readthedocs.io/en/rtd/)
* [Spark documentation](http://spark.apache.org/)
* [ReactJS documentation](https://reactjs.org/)
* [ReactD3 Documentation](http://www.reactd3.org/)