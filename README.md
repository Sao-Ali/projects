# Commute Time Notification

This project calculates the estimated commute time from your home to work using the Google Maps API and sends you a notification with the estimated commute time via SMS using the Twilio API.

## Features
- Calculate commute time from home to UCI
- Send SMS notification with commute details
- Provides estimated arrival time

## Requirements
- Python 3.x
- `googlemaps` library
- `twilio` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/commute-time-notification.git
    cd commute-time-notification
    ```

2. Install the required packages:
    ```sh
    pip install googlemaps twilio
    ```

## Configuration

1. **Google Maps API:**
    - Obtain an API key from the [Google Cloud Console](https://console.cloud.google.com/).
    - Replace `XXXXXXXXXXXXXXXXXXXXX` in the code with your actual Google Maps API key.

2. **Twilio API:**
    - Sign up for a Twilio account and obtain your Account SID, Auth Token, and Twilio phone number from the [Twilio Console](https://www.twilio.com/console).
    - Replace `XXXXXXXXXXXXXXXXXXXXXXXXXX` with your Twilio Account SID.
    - Replace `XXXXXXXXXXXXXXXXXXXXX` with your Twilio Auth Token.
    - Replace `+18444960233` with your Twilio phone number.
    - Replace `+XXXXXXXXXXXXXXXXXX` with your phone number to receive the SMS.

## Usage

1. Define your home address and Destination address in the `get_commute_duration` function.
    ```python
    home_address = 'your_home_address'
    UCI_address = '653 E Peltason Dr, Irvine, CA 92617'
    ```

2. Run the script:
    ```sh
    python commute_time_notification.py
    ```

## How It Works

1. The `get_commute_duration` function calculates the commute duration using the Google Maps API.
2. The `send_twilio_message` function sends the calculated commute duration via SMS using the Twilio API.
3. The `main` function orchestrates the process by calling the above functions and formats the message to include the estimated arrival time.


## Acknowledgements

- [Google Maps API](https://developers.google.com/maps/documentation)
- [Twilio API](https://www.twilio.com/docs/usage/api)

## Contact

For any questions or suggestions, please contact [Ali Sao](italisao@gmail.com).

