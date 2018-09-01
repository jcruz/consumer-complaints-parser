"""
ConsumerComplaint namedtuple is modeled after columns in data/Consumer_Complaints_sm.csv.
Used for parsing data from that csv file.
"""
import collections

ConsumerComplaint = collections.namedtuple('ConsumerComplaint', [
    'date_received',
    'product',
    'sub_product',
    'issue',
    'sub_issue',
    'consumer_complaint_narrative',
    'company_public_response',
    'company',
    'state',
    'zip_code',
    'tags',
    'consumer_consent_provided',
    'submitted_via',
    'date_sent_to_company',
    'company_response_to_consumer',
    'timely_response',
    'consumer_disputed',
    'complaint_id',
])
