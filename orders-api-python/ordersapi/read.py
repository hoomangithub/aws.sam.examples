
import simplejson as json
import boto3
import os
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('ORDERS_TABLE')


def lambda_handler(event, context):
    table = dynamodb.Table(table_name)
    # defenierte request parameter in template.yaml (/orders/{id}) ist in 'pathParameters'
    order_id = int(event['pathParameters']['id'])
    # table.query ist wie SELECT und KeyConditionExpression ist wie WHERE
    response = table.query(KeyConditionExpression=Key('id').eq(order_id))

    return{
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Items'])
    }
