Online W3C Validator
====================

Pure Python command line for HTML validation using W3C online validator.
It could be very handy for using it in a CI pipline.

Installation
------------

.. code:: bash

   pip install -U Online-W3C-Validator

How to use
----------

You can user the CLI command:

.. code:: bash

   w3c_validator http://www.google.com some_file.html

Example output:

::

   INFO:w3c_validator.validator:Files to validate:
     http://www.google.com
   INFO:w3c_validator.validator:Number of files: 1
   INFO:w3c_validator.validator:validating: http://www.google.com ...
   error: line 2: CSS: “display”: “inline-box” is not a “display” value in “inline-box” in “.ds”.
   error: line 2: The “bgcolor” attribute on the “body” element is obsolete. Use CSS instead.
   error: line 5: Element “nobr” not allowed as child of element “div” in this context. (Suppressing further errors from this subtree.)
   error: line 5: Attribute “width” not allowed on element “div” at this point.
   error: line 5: Element “nobr” not allowed as child of element “div” in this context. (Suppressing further errors from this subtree.)
   error: line 5: The “center” element is obsolete. Use CSS instead.
   error: line 5: The “clear” attribute on the “br” element is obsolete. Use CSS instead.

Or you can use the fuction **validdate** provied by the package, that
thakes either HTML file name or URL as a single parameter an returns
JSON object with the validation output.

.. code:: py

   from w3c_validator import validate

   messages = validate("http://www.google.com")["messages"]
   for m in messages:
       print("Type: %(type)s, Line: %(lastLine)d, Description: %(message)s" % m)

Example output:

::

   Type: error, Line: 2, Description: CSS: “display”: “inline-box” is not a “display” value in “inline-box” in “.ds”.
   Type: error, Line: 2, Description: The “bgcolor” attribute on the “body” element is obsolete. Use CSS instead.
   Type: error, Line: 5, Description: Element “nobr” not allowed as child of element “div” in this context. (Suppressing further errors from this subtree.)
   Type: error, Line: 5, Description: Attribute “width” not allowed on element “div” at this point.
   Type: error, Line: 5, Description: Element “nobr” not allowed as child of element “div” in this context. (Suppressing further errors from this subtree.)
   Type: error, Line: 5, Description: The “center” element is obsolete. Use CSS instead.
   Type: error, Line: 5, Description: The “clear” attribute on the “br” element is obsolete. Use CSS instead.
   Type: error, Line: 5, Description: The “align” attribute on the “div” element is obsolete. Use CSS instead.
   Type: error, Line: 5, Description: Attribute “nowrap” not allowed on element “div” at this point.
   ...

Contact
-------

For bugs please use `GitHub issues`_. For other matters feel free to
contact me at nad2000@gmail.com.

.. _GitHub issues: https://github.com/RonenNess/html_validator/issues
