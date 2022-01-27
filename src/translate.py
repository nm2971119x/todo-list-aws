import json
import decimalencoder
import todoList


def get(event, context):
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])
    lang = todoList.get_item(event['pathParameters']['lang'])
    if not item:
        response = {
            "statusCode": 404,
            "body": "ID incorrecta"
        }
        return response
    item['translate'] = todoList.translate(item['text'], "fr")
    response = {
        "statusCode": 200,
        "body": json.dumps(item,
                           cls=decimalencoder.DecimalEncoder)
    }
    return response
