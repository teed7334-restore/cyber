# 公司形象官網 主程式
- - -

## 開發環境 ##
Linux

Python 2.7.13

PostgreSQL 9.6.3

## 初始化套件 ##

    pip install -r path/requirements.txt

PS.本機沒有切virtualenv，所以有一些套件如果沒用到可以自行評估拿掉

## 常用設定檔 ##

主設定檔 /cyber/cyber/settings.py

路由設定 /cyber/cyber/urls.py

## 啟用Server ##

    ./manage.py runserver 0.0.0.0:8000
