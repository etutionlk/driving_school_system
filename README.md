# Sri Lankan Driving School System
***
This System can be used for manage all the candidates and their transactions during their vehicle training period.



### Run the Project

Create Virtual Environment

```virtualenv venv /usr/bin/python3.10```

Activate the virtual env

```source venv/bin/activate```

Install required python packages

```pip3 install -r requirements.txt```

Run flask app
``` flask --app application run```


### Seed the Database

Initialize the db migrations

```flask --app applicaation db init```

Start database migration

```flask --app application db migrate```

Upgrade the database

```flask --app application db upgrade```

Downgrade the database

```flask --app application db downgrade```

Additional Commands to install packages in linux env (ubuntu)
```
sudo apt-get install python3-mysqldb

sudo apt-get install libmysqlclient-dev


flask --app application run --host=0.0.0.0 --port=8001 --debug

```


### Build Docker image

```sudo docker buildx build --no-cache --file Dockerfile --tag core-driving-school-system-gen1-srv:v0.4.0 .
```