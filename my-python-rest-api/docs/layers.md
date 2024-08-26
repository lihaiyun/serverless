# create layer for google api
md my_layers\python-layer-google-api\python
cd my_layers\python-layer-google-api\python
pip install google-api-python-client google-auth -t .
# zip layer for upload
cd ..\..
7z a python-layer-google-api.zip ".\python-layer-google-api\*"
