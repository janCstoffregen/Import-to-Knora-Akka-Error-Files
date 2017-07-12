import requests, json

# a Python dictionary that will be turned into a JSON object
resourceParams = {
   'restype_id': 'http://www.knora.org/ontology/anything#ThingPicture',
   'properties': {

   },
   'label': "Zuerich",
   'project_id': 'http://data.knora.org/projects/anything'
}

# the name of the file to be submitted
filename = "/Users/system/Desktop/logo.jpg"

# a tuple containing the file's name, its binaries and its mimetype
file = {'file': (filename, open(filename, 'rb'), "image/jpeg")} # use name "file"

# do a POST request providing both the JSON and the binaries
r = requests.post("http://130.60.24.65:3333/v1/resources",
                  data={'json': json.dumps(resourceParams)}, # use name "json"
                  files=file,
                  auth=('anything.user02@example.org', 'test'))

#r.raise_for_status()
print (r.text)
