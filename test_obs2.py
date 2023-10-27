# ref: https://support.huaweicloud.com/intl/en-us/sdk-python-devg-obs/obs_22_0002.html

#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
This sample demonstrates how to list objects under specified bucket
from OBS using the OBS SDK for Python.
'''

import configparser

conf = configparser.ConfigParser()
conf.read('config.ini')
obs_credentials = dict(conf.items('OBS'))
print(obs_credentials)

AK = obs_credentials['ak']
SK = obs_credentials['sk']
server = obs_credentials['endpoint']
bucketName = obs_credentials['bucketname']
objectKey = ''

from obs import *
# Constructs a obs client instance with your account for accessing OBS
obsClient = ObsClient(access_key_id=AK, secret_access_key=SK, server=server)


# List the first 10 objects
print('List the first 10 objects :\n')
resp = obsClient.listObjects(bucketName, max_keys=10)
for content in resp.body.contents:
    print('\t' + content.key + ' etag[' + content.etag + ']')

print('\n')

theSecond10ObjectsMarker = resp.body.next_marker



