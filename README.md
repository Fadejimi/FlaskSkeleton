#Flask App Development
###Create Virtual Environment

_Run the script that adds the environemnt and installs the dependencies._

    ./install.sh

###Activate Virtual Environment

_Run the activate script for the virtual environment._

    . env/bin/activate

###Start The Application

_Run the main python appilcation to start the web server._

    python main.py

Connect to http://localhost:5000 in your browser.

###Resetting The Database

_This will remove the database, and then initialize with the most basic values required to test the app._

    ./scripts/dbsetup.sh

###Unit Testing

_Run the unit tests._

	python tests.py

###References

####Framework
* http://flask.pocoo.org/docs/
* http://jinja.pocoo.org/docs/

####Javascript Libraries
* http://twitter.github.com/bootstrap/
* http://documentcloud.github.com/backbone/
* http://docs.jquery.com/Main_Page
* http://documentcloud.github.com/underscore/

