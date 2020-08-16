#!/bin/bash

project_dir="/home/qt/Desktop/654_test/"

source $project_dir/venv/bin/activate
cd $project_dir/test_project/
pytest --html=$project_dir/test_project/report/report.html $project_dir/test_project/cases/log_page
deactivate
