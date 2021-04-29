from collections import OrderedDict
import io
import shutil
import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- Preparation ----------------------------------------------------------

import httpolice
import httpolice.inputs
import httpolice.reports.html

# Special page:
# ``bugcrowd.html``


with io.open('bugcrowd.html', 'wb') as notices_file:
    httpolice.reports.html.list_notices(notices_file)
