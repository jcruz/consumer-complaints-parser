import collections
import copy
import pprint
from typing import DefaultDict
from typing import Dict
from typing import List
from typing import Set

import dateutil.parser

from library.models.consumer_complaint import ConsumerComplaint

pp = pprint.PrettyPrinter()


class Session:
    def __init__(self, consumer_complaints: List[ConsumerComplaint]) -> None:
        """
        Session has three data members:
        1. consumer complaints - list of complaints
        2. lookup - dictionary (state/year -> set of indexes in consumer complaints)
        3. history - list of previous search requests
        """
        self.consumer_complaints = consumer_complaints
        self.lookup = self._generate_lookup(consumer_complaints)
        self.history: List[str] = []

    def show_results(self, keywords: List[str], save: bool=True) -> None:
        """
        Pretty prints search results and saves search to history.
        """
        pp.pprint(self._search(keywords))
        if save:
            self.history.append(' '.join(keywords))

    def show_history(self) -> None:
        """
        Prints previous searches in the format: {index}. {keywords}
        """
        for index, value in enumerate(self.history):
            print('{}: {}'.format(index, value))

    def show_history_item(self, index: int) -> None:
        """
        Prints search results from history item at given index.
        """
        if not 0 <= index < len(self.history):
            print('Invalid index')
            return
        self.show_results(self.history[index].split(), save=False)

    def remove_history_item(self, index: int) -> None:
        """
        Remove history item at given index.
        """
        if not 0 <= index < len(self.history):
            print('Invalid index')
            return
        del self.history[index]

    def _search(self, keywords: List[str]) -> List[ConsumerComplaint]:
        """
        Searches lookup dictionary for keywords.
        """
        if any(keyword not in self.lookup for keyword in keywords):
            return []
        result_indexes = copy.copy(self.lookup[keywords[0]])
        # get intersection if additional keywords
        for keyword in keywords[1:]:
            result_indexes &= self.lookup[keyword]
        return [self.consumer_complaints[i] for i in result_indexes]

    @staticmethod
    def _generate_lookup(consumer_complaints: List[ConsumerComplaint]) -> Dict[str, Set[int]]:
        """
        Generate lookup dictionary with keys as states/years and values as a set of indices
        in the complaints list. Year taken from complaint date received.
        """
        lookup: DefaultDict[str, Set[int]] = collections.defaultdict(set)
        for index, consumer_complaint in enumerate(consumer_complaints):
            date_received = dateutil.parser.parse(consumer_complaint.date_received)
            lookup[str(date_received.year)].add(index)
            lookup[consumer_complaint.state].add(index)
        return dict(lookup)
