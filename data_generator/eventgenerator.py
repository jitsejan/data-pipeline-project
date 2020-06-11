from mimesis.random import Random
from mimesis import Datetime
import json


class EventGenerator:
    """ Defines the EventGenerator """

    MIN_LIVES = 1
    MAX_LIVES = 99
    CHARACTERS = ["Mario", "Luigi", "Peach", "Toad"]

    def __init__(self, num_events, output_type, start_date, end_date, output_file=None):
        """ Initialize the EventGenerator """
        self.datetime = Datetime()
        self.random = Random()
        self.num_events = num_events
        self.output_type = output_type
        self.output_file = output_file
        self.start_date = start_date
        self.end_date = end_date

    def _get_date_between(self, date_start, date_end):
        """ Get a date between start and end date """
        return self.random.choice(self.datetime.bulk_create_datetimes(self.start_date, self.end_date, days=1))

    def _generate_events(self):
        """ Generate the metric data """
        for _ in range(self.num_events):
            yield {
                "character": self.random.choice(self.CHARACTERS),
                "world": self.random.randint(1, 8),
                "level": self.random.randint(1, 4),
                "lives": self.random.randint(self.MIN_LIVES, self.MAX_LIVES),
                "time": str(self._get_date_between(self.start_date, self.end_date)),
            }

    def store_events(self):
        if self.output_type == "jl":
            with open(self.output_file, "w") as outputfile:
                for event in self._generate_events():
                    outputfile.write(f"{json.dumps(event)}\n")
        elif self.output_type == "list":
            return list(self._generate_events())
