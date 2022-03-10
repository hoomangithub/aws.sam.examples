import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('ORDERS_TABLE')


def lambda_handler(event, context):
    # order is a dict (https://docs.python.org/3/library/json.html#py-to-json-table)
    order = json.loads(event['body'])
    table = dynamodb.Table(table_name)
    response = table.put_item(TableName=table_name, Item=order)
    print(response)
    return{
        'statusCode': 201,
        'headers': {},
        # json.dumps serializes a object
        'body': json.dumps({'message': 'Order Created'})
    }