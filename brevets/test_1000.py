import nose
import arrow
from acp_times import open_time, close_time


begin_date = arrow.get("2021-01-01T00:00", "YYYY-MM-DDTHH:mm")

def test_open_time():
    assert(open_time(0,1000,begin_date) == arrow.get("2021-01-01T00:00", "YYYY-MM-DDTHH:mm"))
    assert(open_time(200,1000,begin_date) == arrow.get("2021-01-01T05:53", "YYYY-MM-DDTHH:mm"))
    assert(open_time(300,1000,begin_date) == arrow.get("2021-01-01T09:00", "YYYY-MM-DDTHH:mm"))
    assert(open_time(400,1000,begin_date) == arrow.get("2021-01-01T12:08", "YYYY-MM-DDTHH:mm"))
    assert(open_time(600,1000,begin_date) == arrow.get("2021-01-01T18:48", "YYYY-MM-DDTHH:mm"))
    assert(open_time(1000,1000,begin_date) == arrow.get("2021-01-02T09:05", "YYYY-MM-DDTHH:mm"))

def test_close_time():
    assert(close_time(0,1000,begin_date) == arrow.get("2021-01-01T01:00", "YYYY-MM-DDTHH:mm"))
    assert(close_time(200,1000,begin_date) == arrow.get("2021-01-01T13:20", "YYYY-MM-DDTHH:mm"))
    assert(close_time(300,1000,begin_date) == arrow.get("2021-01-01T20:00", "YYYY-MM-DDTHH:mm"))
    assert(close_time(400,1000,begin_date) == arrow.get("2021-01-02T02:40", "YYYY-MM-DDTHH:mm"))
    assert(close_time(600,1000,begin_date) == arrow.get("2021-01-02T16:00", "YYYY-MM-DDTHH:mm"))
    assert(close_time(1000,1000,begin_date) == arrow.get("2021-01-04T03:00", "YYYY-MM-DDTHH:mm"))
