import http

from flask_restful import reqparse, Resource

from src import service
from src.validation import booking_validator, update_booking_validator


class BookingResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)

    def post(self):
        booking_validator(self.parser)
        args = self.parser.parse_args(http_error_code=422)
        service.save_booking(args)
        return {}, http.HTTPStatus.CREATED

    def get(self):
        return service.get_bookings()


class BookingItemResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)

    def get(self, booking_id):
        return service.get_booking(booking_id)

    def delete(self, booking_id):
        service.delete_booking(booking_id)
        return {}

    def put(self, booking_id):
        update_booking_validator(self.parser)
        args = self.parser.parse_args(http_error_code=422)
        service.update_booking(booking_id, args)
        return {},http.HTTPStatus.OK
