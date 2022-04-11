import os

from boto3 import resource
from dotenv import load_dotenv
from werkzeug.exceptions import InternalServerError

load_dotenv()

AWS_ACCESS_KEY_ID = os.environ["ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["SECRET_ACCESS_KEY"]
REGION_NAME = os.environ["REGION_NAME"]

resource = resource(
    'dynamodb',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)

BookingTable = resource.Table('S_BOOKINGS')


def save_booking(booking_id: str, full_name: str, email: str, booking_date: str, booking_time: str, service: str):
    try:
        return BookingTable.put_item(
            Item={
                'id': booking_id,
                'full_name': full_name,
                'email': email,
                'booking_date': booking_date,
                'booking_time': booking_time,
                'service': service,

            }
        )
    except Exception as e:
        print(e)
        raise InternalServerError("Internal server error")


def update_booking(booking_id: str, data: dict):
    try:
        full_name_ = data['full_name']
        email_ = data['email']
        booking_date_ = data['booking_date']
        booking_time_ = data['booking_time']
        service_ = data['service']
        response = BookingTable.update_item(
            Key={
                'id': booking_id,
            },
            UpdateExpression='SET full_name=:full_name, email=:email ,booking_date=:booking_date ,'
                             'booking_time=:booking_time, service=:service',
            ExpressionAttributeValues={
                ':full_name': full_name_,
                ':email': email_,
                ':booking_date': booking_date_,
                ':booking_time': booking_time_,
                ':service': service_,
            },
            ReturnValues="UPDATED_NEW"
        )
        print(response)
    except Exception as e:
        print(e)
        raise InternalServerError("Internal server error")


def delete_booking(booking_id: str):
    try:
        return BookingTable.delete_item(
            Key={
                'id': booking_id
            }
        )
    except Exception as e:
        print(e)
        raise InternalServerError("Internal server error")


def get_bookings():
    try:
        response = BookingTable.scan()
        data = response['Items']
        while 'LastEvaluatedKey' in response:
            response = BookingTable.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])
        return data
    except Exception as e:
        print(e)
        raise InternalServerError("Internal server error")


def get_booking(booking_id: str):
    try:
        return BookingTable.get_item(
            Key={'id': booking_id},
            AttributesToGet=['id', 'full_name', 'email', 'booking_date', 'booking_time', 'service']
        )

    except Exception as e:
        print(e)
        raise InternalServerError("Internal server error")
