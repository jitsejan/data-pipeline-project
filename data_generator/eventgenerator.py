from faker import Faker
import json


class EventGenerator:
    """ Defines the EventGenerator """

    MIN_LIVES = 1
    MAX_LIVES = 99
    CHARACTERS = ["Mario", "Luigi", "Peach", "Toad"]

    def __init__(self, num_events, output_type, output_file, start_date, end_date):
        """ Initialize the EventGenerator """
        self.faker = Faker()
        self.num_events = num_events
        self.output_type = output_type
        self.output_file = output_file
        self.start_date = start_date
        self.end_date = end_date

    def _get_date_between(self, date_start, date_end):
        """ Get a date between start and end date """
        return self.faker.date_between_dates(date_start=date_start, date_end=date_end)

    def _generate_events(self):
        """ Generate the metric data """
        for _ in range(self.num_events):
            yield {
                "character": self.faker.random_element(self.CHARACTERS),
                "world": self.faker.random_int(min=1, max=8, step=1),
                "level": self.faker.random_int(min=1, max=8, step=1),
                "lives": self.faker.random_int(
                    min=self.MIN_LIVES, max=self.MAX_LIVES, step=1
                ),
                "time": str(self._get_date_between(self.start_date, self.end_date)),
            }

    def store_events(self):
        if self.output_type == "jl":
            with open(self.output_file, "w") as outputfile:
                for event in self._generate_events():
                    outputfile.write(f"{json.dumps(event)}\n")
