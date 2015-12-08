# Python Starter Overview

The Python Starter demonstrates a simple, reusable Python web application.

## Run the app locally

1. [Install Python][]
2. Download and extract the starter code from the Bluemix UI
3. cd into the app directory
4. Run `python server.py`
5. Access the running app in a browser at http://localhost:8000



## Dialog upload

`curl -X POST -F "file=@dialog_files/jemboo-dialog-file.xml" -F "name=jemboo" https://gateway.watsonplatform.net/dialog/api/v1/dialogs -u "robdefeo@gmail.com:*password*"`