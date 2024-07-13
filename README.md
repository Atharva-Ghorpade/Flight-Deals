# Flight Price Alert System

A Python application that searches for the cheapest flights and sends notifications via SMS, WhatsApp, and email.

## Overview

This project helps users find the best flight deals from a specified origin city to various destinations, using an external flight search API. If a cheaper flight is found compared to a specified lowest price, the user is notified through multiple channels.

## Getting Started

### Requirements

- **Python 3.x**: Ensure you have Python installed on your computer.
- Required libraries (install using `pip`):

   ```bash
   pip install pandas requests
### Installation Steps

1. Clone the Repository:
   ```bash
   git clone https://github.com/atharva-ghorpade/Flight-Price-Alert.git
   cd Flight-Price-Alert
   
2. Setting Up Environment Variables

   Create a .env file in the project directory to store sensitive details. Use the following format for your .env file:

   - SHEETY_USERNAME="your_username"
   - SHEETY_PASSWORD="your_password"
   - AMADEUS_API_KEY="your_api_key"
   - AMADEUS_SECRET="your_api_secret"
   - TWILIO_SID="your_twilio_sid"
   - TWILIO_AUTH_TOKEN="your_twilio_auth_token"
   - TWILIO_VIRTUAL_NUMBER="your_twilio_virtual_number"
   - TWILIO_VERIFIED_NUMBER="your_verified_number"
   - TWILIO_WHATSAPP_NUMBER="your_whatsapp_number"
   - EMAIL="your_email"
   - EMAIL_PASSWORD="your_email_password"

3. Run the Application:
   ```bash
   python main.py


Feel free to fill in your LinkedIn and Twitter links, or adjust any sections as needed!
