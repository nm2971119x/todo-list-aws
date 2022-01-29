#!/bin/bash

source todo-list-aws/bin/activate
set -x
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
echo "PYTHONPATH: $PYTHONPATH"
export DYNAMODB_TABLE=todoUnitTestsTable
python test/unit/TestToDo.py
pip show coverage
coverage run --include=src/todoList.py test/unit/TestToDo.py
coverage report
coverage xml
coverage html
#tar vfcz /var/lib/jenkins/workspace/PIPELINE-FULL-STAGING/htmlcov.tgz /var/lib/jenkins/workspace/PIPELINE-FULL-STAGING/htmlcov/
