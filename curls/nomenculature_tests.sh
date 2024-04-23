#! /bin/bash

curl http://127.0.0.1:5000/api/get_nomenculature/$1

curl -X PATCH -H "Content-Type: application/json" -d @Tests/nomen.json http:/127.0.0.1:5000/api/patch_nomenculature/$1

curl -X DELETE http://127.0.0.1:5000/api/del_nomenculature/11d55140-326f-4ed4-9994-ea1f6aa35934

curl -X POST -H "Content-Type: application/json" -d @Tests/nomen.json http:/127.0.0.1:5000/api/add_nomenculature