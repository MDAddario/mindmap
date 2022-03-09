#!/bin/sh

####################################
# Launch the mind map web service  #
#                                  #
# This script should be ran in the #
# root folder of the proeject      #
####################################

export FLASK_APP=./service/main
flask run
