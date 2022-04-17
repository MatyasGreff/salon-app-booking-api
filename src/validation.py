from flask_restful import inputs

# These are the validators called from booking_resource.py
def non_empty_string(s):
    if not s:
        raise ValueError("Must not be empty string")
    return s


def booking_validator(parser):

    parser.add_argument('email', help='valid email required',
                        type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"), nullable=False)

    parser.add_argument('full_name', help='valid fullname required', required=True, nullable=False, type=non_empty_string,
                        trim=True)

    parser.add_argument('service', help='service name required', required=True, nullable=False,
                        type=non_empty_string)

    parser.add_argument('booking_date', help='valid booking date required',
                        type=inputs.regex(
                            r"^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$"),
                        nullable=False,
                        required=False)

    parser.add_argument('booking_time', help='valid booking time required', required=False, nullable=False,
                        type=non_empty_string)


def update_booking_validator(parser):

    parser.add_argument('email', help='valid email required',
                        type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"), nullable=False)

    parser.add_argument('full_name', help='valid fullname required', required=False, nullable=False, type=non_empty_string,
                        trim=True)

    parser.add_argument('service', help='service name required', required=False, nullable=False,
                        type=non_empty_string)

    parser.add_argument('booking_date', help='valid booking date required - dd/mm/yyyy format',
                        type=inputs.regex(
                            r"^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$"),
                        nullable=False,
                        required=False)

    parser.add_argument('booking_time', help='valid booking time required', required=False, nullable=False,
                        type=non_empty_string)
