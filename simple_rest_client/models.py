from collections import namedtuple

Request = namedtuple(
    'Request', ['url', 'method', 'params', 'body', 'headers', 'timeout', 'verify', 'kwargs']
)
Response = namedtuple(
    'Response', ['url', 'method', 'body', 'headers', 'status_code', 'client_response']
)
