# airtable-rest

Minimal Rest API built with Flask and airtable-python-wrapper for deployment on Heroku.

To authenticate add config variable 'AIR_KEY' = 'your airtable api key' thru your Heroku dashboard.

Clone the repository, navigate to it and run:
    
    python3 -m venv venv/
    source venv/bin/activate
    
    pipenv install
    
Create a .env file and add AIR_KEY=YOUR AIRTABLE KEY to the .env file. Next run:
    
    heroku local

## Built on top of

[airtable-python-wrapper](https://github.com/gtalarico/airtable-python-wrapper)
