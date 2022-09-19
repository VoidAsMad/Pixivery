# Pixivery
[<img src="https://img.shields.io/pypi/v/pixivery.svg">](https://pypi.python.org/pypi/pixivery)<br>
## Install
```py
$ pip install pixivery
```

## Example
```py
from pixivery import client

client = client.Pixiv()
print(client.get_ranking()) #limit = 1~50
print(client.get_artwork('100807849'))
```
