# This script creates and runs an instance of the application.

import os
import sys

sys.path.append(os.path.dirname(__name__))

from client import create_app

# create an app instance
app = create_app()

app.run(debug=True)
