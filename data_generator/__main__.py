""" __main__.py """
from eventgenerator import EventGenerator

import argparse
import datetime
from dateutil.relativedelta import relativedelta

CHARACTERS = ["Mario", "Luigi", "Peach", "Toad"]
DATE_END = datetime.datetime.now()
DATE_START = DATE_END + relativedelta(months=-1)
OUTPUT_CHOICES = ["jl", "csv", "list"]    


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
        "-ot", "--output_type", nargs="?", choices=OUTPUT_CHOICES, default="list"
    )
    parser.add_argument(
        "-of", "--output_file", default="data.output"
    )
    parser.add_argument(
        "-ch", "--characters", nargs='+', default=CHARACTERS
    )
    return parser


def main():
    """ Defines the main function """
    # Get database from arguments
    parser = _get_parser()
    args = parser.parse_args()
    params = {
        "characters": args.characters,
        "num_events": args.num_events,
        "output_type": args.output_type,
        "output_file": args.output_file,
        "start_date": DATE_START,
        "end_date": DATE_END,
    }
    print(params)
    # Create the event generator
    generator = EventGenerator(**params)
    # Create and store the events
    result = generator.store_events()


if __name__ == "__main__":
    main()
