# Google API POC

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Links](#links)

## About <a name = "about"></a>

How to use google API for sheets and Mail.
We will use sheet for logs and mail for password reset, and welcome mail.

## Getting Started <a name = "getting_started"></a>

Create a project and enable API
> https://developers.google.com/workspace/guides/create-project

Get Credentials
> https://developers.google.com/workspace/guides/create-credentials

### Installing

A step by step series of examples that tell you how to get a development env running.

First install modules using pip

```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

And then move credentials.json file in same location as main.py (main.py and credentials.json are siblings)

Now Run 

```
python main.py
```

## Links <a name = "links"></a>

### Sheet Code Source
> https://github.com/googleworkspace/python-samples/tree/master/sheets

### Gmail Code Source
> https://github.com/googleworkspace/python-samples/tree/master/gmail/quickstart

For email use encoding as mentioned
> https://stackoverflow.com/questions/57632950/ 
