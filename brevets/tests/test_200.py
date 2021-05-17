import nose
import arrow
from acp_times import open_time, close_time


begin_date = arrow.get("2021-01-01T00:00", "YYYY-MM-DDTHH:mm")
open = arrow.get("2021-01-01T05:53", "YYYY-MM-DDTHH:mm")
close = arrow.get("2021-01-01T13:30", "YYYY-MM-DDTHH:mm")

def test_open_time():
    assert(open_time(0,200,begin_date) == arrow.get("2021-01-01T00:00", "YYYY-MM-DDTHH:mm"))
    assert(open_time(200,200,begin_date) == open)


def test_close_time():
    assert(close_time(0,200,begin_date) == arrow.get("2021-01-01T01:00", "YYYY-MM-DDTHH:mm"))
    assert(close_time(200,200,begin_date) == close)
