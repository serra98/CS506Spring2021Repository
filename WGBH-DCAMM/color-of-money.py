import unittest
from sys import argv
from parsers.pdfparser import import_pdf

def main(arg):
    debug = False
    print("================================")
    rows = import_pdf("data/WorkforceUtilizationSummaryReportApril2019.pdf", debug)

    print("================================")

if __name__ == "__main__":
    main(argv)
    unittest.main(argv)

