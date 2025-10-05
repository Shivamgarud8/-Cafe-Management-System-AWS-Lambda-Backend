**# Cafe-Management-System-AWS-Lambda-Backend**

Serverless backend system to manage cafe orders in real-time. Orders are stored in DynamoDB and chefs receive SMS notifications instantly via SNS

**🚀 Project Overview**
Users place orders with table number, items, and customizations.
Orders are stored in DynamoDB.
Chefs get real-time SMS notifications via SNS.
Fully serverless using AWS Lambda.

| Service        | Purpose                                      |
| -------------- | -------------------------------------------- |
| **AWS Lambda** | Backend order handler                        |
| **DynamoDB**   | Stores all order records                     |
| **SNS**        | Sends SMS notifications to chefs             |
| **IAM Roles**  | Grants Lambda permissions for DynamoDB & SNS |


| Attribute   | Type   | Description              |
| ----------- | ------ | ------------------------ |
| orderId     | String | Unique ID for each order |
| tableNumber | String | Table number             |
| items       | String | Items ordered            |
| custom      | String | Customizations           |
| total       | Number | Order total              |
| timestamp   | String | ISO timestamp of order   |

| Variable Name   | Description                          |
| --------------- | ------------------------------------ |
| `DYNAMO_TABLE`  | DynamoDB table name (`CafeOrders`)   |
| `SNS_TOPIC_ARN` | SNS topic ARN for chef notifications |


**📱 SNS Configuration**
Topic Name: sns-for-sms
Message Example:
🍽️ New Order #1234 - Table 5
Items: Masala Dosa x2, Soda x1
Custom: Extra Spicy
Amount: ₹150


**🔐 IAM Roles & Policies**
Role Name Suggestion: CafeOrdersLambdaRole
Required Policies:
AmazonDynamoDBFullAccess (or least privilege with PutItem on CafeOrders)
AmazonSNSFullAccess (or least privilege with Publish to SNS
AWSLambdaBasicExecutionRole

🌐 Lambda Trigger Setup
Create API Gateway HTTP API.
Add a POST method pointing to Lambda.
Enable CORS for frontend requests.
Lambda processes the order and sends SNS notification.

**📝 Folder Structure**
cafe-management-system/
│
├─ lambda/
│   └─ cafe_order_lambda.py
├─ frontend/
│   └─ index.html
└─ README.md


🌟 Contributors
 **Trupti Mane Ma`am** – ⭐ AWS wizard & hands-on support, made testing and deployment seamless! [@iamtruptimane](https://github.com/iamtruptimane)

** 🔗 Links & Contact**
GitHub: https://github.com/shivamgarud8
LinkedIn: https://www.linkedin.com/in/shivam-garud-371b5a307


![Home Page](images/home.png)
![Order Form](images/order-form.png)
![Table Selection](images/table-selection.png)
![Order Confirmation](images/order-confirmation.png)
