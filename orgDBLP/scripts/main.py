from orgDBLP import *
import argparse


def process_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url",
                        nargs="?",
                        default="",
                        type=str,
                        help="The URL to use (typically to an open access version)")
    parser.add_argument("-q", "--query",
                        type=str,
                        help="The query to send to DBLP")
    return parser.parse_args()


def main_cli():
    args = process_arguments()
    res = search_DBLP(args.query)
    print("* Query:", args.query)
    if len(res) == 0:
        print("No paper found")
    else:
        for x in res:
            print(org_format(x, url=args.url))
            print()
        

