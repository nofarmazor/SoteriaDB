__author__ = 'nofar'

import json,httplib,urllib, ssl

# STATIC DEFAULTS:
PARSE_APPLICATION_ID = "iLN1v3zqIM8mXfsbdqhZbTFjvYOwXZzHDXteGc3j"
PARSE_REST_API_KEY = "8M71FShn7tgq8Fih7WNGAclbxVABhNyNLrpaMXqJ"
PARSE_API_URL = 'api.parse.com'
HTTPS_PORT=443
COMMAND_SOURCE = 'Soteria Web WINK Simulator'

def handle_ssl():
    # Added to resolve SSL certificate issues with python 2.7.9:
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

def get_device_by_cloud_id(cloud_id):

    handle_ssl()
    connection = httplib.HTTPSConnection(PARSE_API_URL, HTTPS_PORT)
    connection.connect()
    params = urllib.urlencode({"where": json.dumps({
        "CloudID": cloud_id
        }
        )})

    connection.request('GET', '/1/classes/Devices?%s' % params, '', {
           "X-Parse-Application-Id": PARSE_APPLICATION_ID,
           "X-Parse-REST-API-Key": PARSE_REST_API_KEY
     })
    result = json.loads(connection.getresponse().read())
    return result

def get_device_by_zigbee_id(zigbee_id):

    handle_ssl()
    connection = httplib.HTTPSConnection(PARSE_API_URL, HTTPS_PORT)
    connection.connect()
    params = urllib.urlencode({"where": json.dumps({
        "ZigbeeID": zigbee_id
        }
        )})

    connection.request('GET', '/1/classes/Devices?%s' % params, '', {
           "X-Parse-Application-Id": PARSE_APPLICATION_ID,
           "X-Parse-REST-API-Key": PARSE_REST_API_KEY
     })
    result = json.loads(connection.getresponse().read())
    return result

def save_command(device_cloud_id, command_type):

    handle_ssl()
    connection = httplib.HTTPSConnection(PARSE_API_URL, HTTPS_PORT)
    connection.connect()
    connection.request('POST','/1/classes/Command',json.dumps({
       "commandType": command_type,
       "DstDeviceCloudID": device_cloud_id,
       "source": COMMAND_SOURCE
     }), {
       "X-Parse-Application-Id": PARSE_APPLICATION_ID,
       "X-Parse-REST-API-Key": PARSE_REST_API_KEY
 })

def get_sent_commands(start_time, end_time, device_zigbee_id):
    handle_ssl()


def print_result(result):
    print "{0} results".format(len(result))
    print "     First result:"
    print "         CloudID: {0}".format(result['results'][0]['CloudID'])
    print "         ZigbeeID: {0}".format(result['results'][0]['ZigbeeID'])
    print "         DeviceName: {0}".format(result['results'][0]['DeviceName'])
    print "         DeviceType: {0}".format(result['results'][0]['DeviceType'])
