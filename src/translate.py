import os
import json
import decimalencoder
import todoList


def get(event, context):
    item = todoList.get_item(event['pathParameters']['id'])
    if not item:
        response = {
            "statusCode": 404,
            "body": "ID incorrecta"
        }
        return response

    lang = event['pathParameters']['lang']
    if not lang:
        response = {
            "statusCode": 200,
            "body": "Lang not defined"
        }
        return response
    if not len(lang) == 2:
        response = {
            "statusCode": 200,
            "body": "Invalid ISO Country code"
        }
        return response
    item['translate'] = todoList.translate(item['text'], lang)
    item['source_lang'] = os.environ['DEFAULT_LANG']
    item['target_lang'] = lang
    if item['translate']:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
            }
        return response
    else:
        response = {
            "statusCode": 200,
            "body": "Error translate"
        }
        return response
