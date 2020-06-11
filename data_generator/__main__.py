""" __main__.py """
from eventgenerator import EventGenerator

import argparse
import datetime
from dateutil.relativedelta import relativedelta

DATE_END = datetime.datetime.now()
DATE_START = DATE_END + relativedelta(months=-1)
OUTPUT_CHOICES = ["jl", "list"]


def _get_parser():
    """
    Get the argument parser

    :return: ArgumentParser
    """
    parser = argparse.ArgumentParser(description="Create the events")
    parser.add_argument(
        "-n", "--num-events", type=int, default=10
    )
    parser.add_argument(
        "-o", "--output", nargs="?", choices=OUTPUT_CHOICES, required=True
    )
    return parser


def main():
    """ Defines the main function """
    # Get database from arguments
    parser = _get_parser()
    args = parser.parse_args()
    params = {
        "num_events": args.num_events,
        "output_type": args.output,
        "output_file": "characterdata.jl",
        "start_date": DATE_START,
        "end_date": DATE_END,
    }
    # Create the event generator
    generator = EventGenerator(**params)
    # Create and store the events
    generator.store_events()


if __name__ == "__main__":
    main()
