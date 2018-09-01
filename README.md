# Parsing Consumer Complaints

## Installation
Python 3 required. Recommended to install pip packages within a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/#creating-a-virtualenv).
```bash
$ pip install -r requirements.txt
```

## Get Started
```bash
$ python consumer_complaint_parser.py
you're in the consumer complaints parser cli! type `help` to get started.
>
```

## Example Usage
```bash
# Make a search request for a state (two-letter abbreviation) and/or year
> search CA
[...]
> search 2018
[...]
> search CA 2018
[...]

# Display list of all previous search requests
> history
0: CA
1: 2018
2: CA 2018

# Select one and see the results from that search
> show 0
[...]

# Specify to remove one of the search requests from the history
> remove 0
> history
0: 2018
1: CA 2018
```
