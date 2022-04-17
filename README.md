# Salon booking api

This is the repository for the booking API used in the Salon application.

## To run the API locally

The API sends requests to a DynamoDB instance called S_BOOKINGS.
In order to make the API work locally, make sure to create this instance.
Also set up an IAM user with DynamoDB access.
Then clone this repo and create a .env file in the root directory, fill with your details
```
ACCESS_KEY_ID=
SECRET_ACCESS_KEY=
REGION_NAME=
```

Save the file and create a python virtual environment
```
python3 -m venv ./venv
```
Activate the environment, then from the root directory, run this command to install required python libraries
```
pip install -r requirements.txt
```
Make sure NodeJS and Serverless framework are installed and run:
```
npm install
```
Then, to run the service:
```
serverless wsgi serve
```
The API service is now running on localhost/5000


## Interaction with the API
To query all, send a GET request to 
```
localhost:5000/api/bookings
```
To create a new entry, send a POST request to the same address, with a valid json (example)
```
{
    "booking_date": "2022-04-15",
    "service": "nails",
    "booking_time": "10AM-11AM",
    "full_name": "Test User",
    "email": "test@test.com"
}
```
To remove an entry, send a DELETE request to
```
localhost:5000/api/bookings/[id to be deleted]
```
To update a booking, send a PUT request with valid json
```
localhost:5000/api/bookings/[id to be updated]
```
