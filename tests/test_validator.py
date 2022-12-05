from w3c_validator import validate
from unittest.mock import Mock
import os


def test_valiates0(mocker):
    filename = os.path.join(os.path.dirname(__file__), "test0.html")
    messages = validate(filename)["messages"]
    for m in messages:
        if "lastLine" in m:
            print("Type: %(type)s, Line: %(lastLine)d, Description: %(message)s" % m)
        else:
            print("Type: %(type)s,  Description: %(message)s" % m)

    # with open(filename, "rb") as f:
    #     test_content = f.read()
    # mocker.patch("requests.get", return_value=Mock(content=test_content))

    # messages = validate("http://www.google.com")["messages"]
    # for m in messages:
    #     print("Type: %(type)s, Line: %(lastLine)d, Description: %(message)s" %
    #           m)


def test_valiates(mocker):
    filename = os.path.join(os.path.dirname(__file__), "test.html")
    messages = validate(filename)["messages"]
    for m in messages:
        if "lastLine" in m:
            print("Type: %(type)s, Line: %(lastLine)d, Description: %(message)s" % m)
        else:
            print("Type: %(type)s,  Description: %(message)s" % m)

    # with open(filename, "rb") as f:
