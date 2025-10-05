import json
import boto3
import os
from datetime import datetime

# Initialize AWS clients
dynamo = boto3.resource('dynamodb')
sns = boto3.client('sns')

# DynamoDB Table Name and SNS Topic ARN from environment variables
TABLE_NAME = os.environ.get('DYNAMO_TABLE', 'CafeOrders')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN', 'YOUR_SNS_TOPIC_ARN_HERE')  # <-- Replace with your SNS ARN

table = dynamo.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        # Parse JSON body
        body = json.loads(event['body'])
        table_number = body.get('tableNumber')
        items = body.get('items')
        custom = body.get('custom', 'None')
        total = body.get('total')

        if not table_number or not items or not total:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Table number, items, and total are required"})
            }

        # Generate order ID
        order_id = str(int(datetime.utcnow().timestamp() * 1000))

        # Prepare DynamoDB item
        order_data = {
            'orderId': order_id,
            'tableNumber': str(table_number),
            'items': items,
            'custom': custom,
            'total': float(total),
            'timestamp': datetime.utcnow().isoformat()
        }

        # Store in DynamoDB
        table.put_item(Item=order_data)

        # Send SNS notification
        message = (
            f"🍽️ New Order #{order_id[-4:]} - Table {table_number}\n"
            f"Items: {items}\n"
            f"Custom: {custom}\n"
            f"Amount: ₹{total}"
        )
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Order placed successfully!", "orderId": order_id})
        }

    except Exception as e:
        print("Error:", e)
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error", "error": str(e)})
        }
