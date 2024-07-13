import googlemaps
from datetime import datetime
from twilio.rest import Client

def get_commute_duration():
    # Define your home and work locations
    home_address = 'home'
    UCI_address = '653 E Peltason Dr, Irvine, CA 92617'

    # Set up Google Maps API client
    google_maps_api_key = 'XXXXXXXXXXXXXXXXXXXXX'
    gmaps = googlemaps.Client(key=google_maps_api_key)

    # Get the directions
    directions = gmaps.directions(home_address, UCI_address, departure_time='now')

    # Get the duration of the first leg
    duration = directions[0]['legs'][0]['duration']['text']
    return duration

def send_twilio_message(message):
    # Set up Twilio client
    twilio_account_sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
    twilio_auth_token = 'XXXXXXXXXXXXXXXXXXXXX'
    twilio_phone_number = '+18444960233'
    your_phone_number = '+XXXXXXXXXXXXXXXXXX'
    client = Client(twilio_account_sid, twilio_auth_token)

    client.messages.create(
        to=your_phone_number,
        from_=twilio_phone_number,
        body=message
    )

def main():
    duration = get_commute_duration()
    # Calculate the estimated arrival time
    now = datetime.now()
    arrival_time = (now + duration).strftime('%I:%M %p')

    # Send the estimated commute time
    message = (
    f"Good morning!\n\n"
    f"Estimated commute time from home to work at 9 am: {duration}.\n\n"
    f"Leave now for work at 9am to arrive at approximately {arrival_time}.\n"
    )
    send_twilio_message(message)

if __name__ == "__main__":
    main()
