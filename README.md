# 公司形象官網 主程式
- - -

## 開發環境 ##
Linux

Python 3.5.3

PostgreSQL 9.6.3

## 初始化套件 ##

    pip install -r path/requirements.txt

## 常用設定檔 ##

主設定檔 /cyber/cyber/settings.py

路由設定 /cyber/cyber/urls.py

## 初始化設定 ##

建立資料表所需之 migrate 文件

    ./manage.py makemigrations

透過 migrate 建立資料表

    ./manage.py migrate

建立後台管理員

    ./manage.py createsuperuser

## 啟用Server ##

    ./manage.py runserver 0.0.0.0:8000
