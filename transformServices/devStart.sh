#! /bin/bash
export FLASK_APP=app/main.py
export FLASK_DEBUG=1
export PYTHONPATH=/home/dhenry/Dev/mohub_glean/transformationServices/app
export LIB_DEST=$PYTHONPATH
export DAGS_DEST=/home/dhenry/Dev/gleanomatic/dags
export LOG_DEST=/var/logs/gleanomatic/logs
export LOG_FILE=gleanomatic.log
export LOG_LEVEL=INFO
export USER_AGENT=Mozilla/5.0

/usr/local/bin/flask run --host=0.0.0.0 --port=81
