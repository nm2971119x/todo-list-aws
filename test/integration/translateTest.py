import http.client
import os
import unittest
from urllib.request import urlopen
import requests
import json

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 3


#@pytest.mark.api
class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")
    
    def test_api_translate(self):
        print('---------------------------------------')
        print('Starting - integration test Translate TODO')
        #Add TODO
        url = BASE_URL+"/todos"
        data = {
         "text": "Integration text example - GET"
        }
        response = requests.post(url, data=json.dumps(data))
        json_response = response.json()
        print('Response Add Todo: '+ str(json_response))
        jsonbody= json.loads(json_response['body'])
        ID_TODO = jsonbody['id']
        print ('ID todo:'+ID_TODO)
        self.assertEqual(
            response.status_code, 200, "Error en la petición API a : "+url
        )
        self.assertEqual(
            jsonbody['text'], "Integration text example - GET", "Error en la petición API a "+url
        )
        # Test GET TODO
        url = BASE_URL+"/todos/"+ID_TODO+"/fr"
        response = requests.get(url)
        json_response = response.json()
        print('Response Get Todo: '+ str(json_response))
        self.assertEqual(
            response.status_code, 200, "Error en la petición API a : "+url
        )
        self.assertEqual(
            json_response['text'], "Integration text example - GET", "Error en la petición API a "+url
        )
        # Delete TODO to restore state
        response = requests.delete(url)
        self.assertEqual(
            response.status_code, 200, "Error en la petición API a : "+url
        )
        print('End - integration test Translate TODO')
