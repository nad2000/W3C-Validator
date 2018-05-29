#!/usr/bin/env python
"""W3C Validator - Validate HTML and CSS files using the WC3 validators."""

from __future__ import print_function

import argparse
import logging
import shutil
import sys
import tempfile
import time

import requests

from w3c_validator import __version__

LOGGER = logging.getLogger(__name__)

HTML_VALIDATOR_URL = "http://validator.w3.org/nu/?out=json"
CSS_VALIDATOR_URL = "http://jigsaw.w3.org/css-validator/validator"


def print_msg(msg):
    """Print validation result message."""
    if "lastLine" in msg:
        print("%(type)s: line %(lastLine)d: %(message)s" % msg)
    else:
        print("%(type)s: %(message)s" % msg)


def validate(filename, verbose=False):
    """
    Validate file and return JSON result as dictionary.

    "filename" can be a file name or an HTTP URL.
    Return "" if the validator does not return valid JSON.
    Raise OSError if curl command returns an error status.
    """
    # is_css = filename.endswith(".css")

    is_remote = filename.startswith("http://") or filename.startswith(
        "https://")
    with tempfile.TemporaryFile() if is_remote else open(
            filename, "rb") as f:

        if is_remote:
            r = requests.get(filename, verify=False)
            f.write(r.content)
            f.seek(0)

        # if is_css:
        #     cmd = (
        #         "curl -sF \"file=@%s;type=text/css\" -F output=json -F warning=0 %s"
        #         % (quoted_filename, CSS_VALIDATOR_URL))
        #     _ = cmd
        # else:
        r = requests.post(
            HTML_VALIDATOR_URL,
            files={"file": (filename, f, "text/html")},
            data={
                "out": "json",
                "showsource": "yes",
            },
            verify=False)

    return r.json()


def main():
    """Parser the command line and run the validator."""
    parser = argparse.ArgumentParser(
        description="[v" + __version__ + "] " + __doc__,
        prog="w3c_validator",
    )
    parser.add_argument(
        "--log",
        default="INFO",
        help=("log level: DEBUG, INFO or INFO "
              "(default: INFO)"))
    parser.add_argument(
        "--version", action="version", version="%(prog)s " + __version__)
    parser.add_argument(
        "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument(
        "source", metavar="F", type=str, nargs="+", help="file or URL")
    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, args.log))

    LOGGER.info("Files to validate: \n  {0}".format("\n  ".join(args.source)))
    LOGGER.info("Number of files: {0}".format(len(args.source)))

    errors = 0
    warnings = 0
    for f in args.source:
        LOGGER.info("validating: %s ..." % f)
        retrys = 0
        while retrys < 2:
            result = validate(f, verbose=args.verbose)
            if result:
                break

            time.sleep(2)
            retrys += 1
            LOGGER.info("retrying: %s ..." % f)
        else:
            LOGGER.info("failed: %s" % f)
            errors += 1
            continue

        # import pdb; pdb.set_trace()
        if f.endswith(".css"):
            errorcount = result["cssvalidation"]["result"]["errorcount"]
            warningcount = result["cssvalidation"]["result"]["warningcount"]
            errors += errorcount
            warnings += warningcount
            if errorcount > 0:
                LOGGER.info("errors: %d" % errorcount)
            if warningcount > 0:
                LOGGER.info("warnings: %d" % warningcount)
        else:
            for msg in result["messages"]:
                print_msg(msg)
                if msg["type"] == "error":
                    errors += 1
                else:
                    warnings += 1
    sys.exit(min(errors, 255))


if __name__ == "__main__":
    main()
