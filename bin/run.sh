#!/bin/sh

######################################
# Launch the mind map web service    #
#                                    #
# This script should be ran from the #
# root folder of the project         #
######################################

export FLASK_APP=./service/main
flask run
