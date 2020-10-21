import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
myTableName = os.environ['dbName']
table = dynamodb.Table(myTableName)

def lambda_handler(event, context):    
    table.update_item(
            Key={
                'personalSite': 'vistorCount'
            },
     
           UpdateExpression="set numVisit = numVisit + :val",
           ExpressionAttributeValues={
            ':val': 1
            }
        )
    theCountIs = table.get_item(
            Key={
                'personalSite': 'vistorCount'
            }
        )
    data = {"vistorCount": int(theCountIs['Item']['numVisit'])}
   
    return{
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': json.dumps(data)
    }
