# airtable-rest

Minimal Rest API built with Flask and airtable-python-wrapper for deployment on Heroku.

To authenticate add config variable 'AIR_KEY' = <your airtable api key> thru your Heroku dashboard.

To deploy run

    # create Heroku project
    
    # install dependencies
    pipenv install
    
    # login to heroku
    heroku login
