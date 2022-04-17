import http

from flask_restful import reqparse, Resource

from src import service
from src.validation import booking_validator, update_booking_validator


class BookingResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)

    def post(self):
        # When /api/bookings is hit with a json Post request is sent to the validator in validation.py
        # If valid, service.save_bookings makes the DynamoDB entry
        booking_validator(self.parser)
        args = self.parser.parse_args(http_error_code=422)
        service.save_booking(args)
        return {}, http.HTTPStatus.CREATED

    def get(self):
        return service.get_bookings() # Query every booking in the database


class BookingItemResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)

    def get(self, booking_id):
        return service.get_booking(booking_id)    # When /api/bookings/<booking_id> is hit  
                                                  # Booking details are returned
    def delete(self, booking_id):
        service.delete_booking(booking_id)   # Another booking_id specific request
        return {}                            # Deletes the booking

    def put(self, booking_id):
        # Put requests that update the booking, same idea as the booking creation
        update_booking_validator(self.parser)
        args = self.parser.parse_args(http_error_code=422)
        service.update_booking(booking_id, args)
        return {},http.HTTPStatus.OK
