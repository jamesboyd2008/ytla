# under normal circumstances, this script would not be necessary. the
# client would have its own setup.py and be properly installed;
# however since it is not bundled in the sdist package, we need some hacks
# to make it work

import os
import sys

sys.path.append(os.path.dirname(__name__))

from client import create_app

# create an app instance
app = create_app()

app.run(debug=True)
