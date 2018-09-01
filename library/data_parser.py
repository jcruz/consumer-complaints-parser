import csv
from typing import List

from library.models.consumer_complaint import ConsumerComplaint


def parse(input_file: str) -> List[ConsumerComplaint]:
    """
    Parse input csv file to a list of consumer complaints.
    """
    consumer_complaints: List[ConsumerComplaint] = []
    with open(input_file) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip headers
        for consumer_complaint in map(ConsumerComplaint._make, reader):
            consumer_complaints.append(consumer_complaint)
    return consumer_complaints
