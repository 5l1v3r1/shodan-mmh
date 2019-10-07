# Simple Shodan Osint with Mumur Hash


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


# New Features!

  - Search Service Redis and Mongodb 
# Next Development!
  - Comunicate with maltego C2 to create OSINT monitor
 



### Tech


* [python3] - python3


### Installation

Add the shodan key in file config ..

```sh
[TOKEN]
shodan_key = qxxxxxxxxxxxxxx # change me with your shodan key 
```


Install the dependencies and devDependencies and start the server.

```sh
$ pip install -r mod.txt 
```

How to run 

```sh
$ python3 shodan.py -h
```

Search by favicon-url

```sh
$ python3 shodan.py --fav=https://localhost.com/favicon.ico
```
Search By Mumur Hash
```sh
$ python3 shodan.py --mmh=3133331313313
```

&copy; [Rahmat Wahyu Hadi](https://github.com/wahyuhadi/) - 2019