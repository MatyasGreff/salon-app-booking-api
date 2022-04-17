import uuid

from werkzeug.exceptions import NotFound

from src import dynamo


def save_booking(args):
    email = args['email']
    full_name = args['full_name']
    booking_date = args['booking_date']
    booking_time = args['booking_time']
    service = args['service']
    booking_id = uuid.uuid4().hex #This creates a unique booking ID
    dynamo.save_booking(booking_id, full_name, email, booking_date, booking_time, service)
    # Args are sent to dynamo.py/save_booking

def get_booking(booking_id):
    booking = dynamo.get_booking(booking_id)
    if "Item" not in booking:
        raise NotFound("booking not  found")
    return booking['Item']
    # Query specific booking

def delete_booking(booking_id):
    dynamo.delete_booking(booking_id)


def update_booking(booking_id, args):
    booking = get_booking(booking_id)
    if booking is not None:
        data = set_payload(args=args, booking=booking)
        print(data)
        dynamo.update_booking(booking_id=booking_id, data=data)


def get_bookings():
    return dynamo.get_bookings()
    # Query all bookings

def set_payload(args, booking):
    email = args['email']
    full_name = args['full_name']
    booking_date = args['booking_date']
    booking_time = args['booking_time']
    service = args['service']

    if email is not None:
        booking["email"] = email
    if full_name is not None:
        booking["full_name"] = full_name
    if booking_date is not None:
        booking["booking_date"] = booking_date
    if booking_time is not None:
        booking["booking_time"] = booking_time
    if service is not None:
        booking["service"] = service
    return booking
# This checks what args are in the update request
# If an arg is not provided, the xisting arg will remain the same