from flask_restful import Api

from src.booking_resource import BookingResource, BookingItemResource


def register_routes(app):
    api = Api(app)

    api.add_resource(BookingResource, '/api/bookings')
    api.add_resource(BookingItemResource, '/api/bookings/<string:booking_id>')

# Adds routes for empty and booking_id specific requests