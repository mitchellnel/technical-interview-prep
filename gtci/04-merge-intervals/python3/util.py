def assert_equal_interval(interval1, interval2):
    assert (
        interval1.start == interval2.start
    ), f"Expected start {interval2.start}, but got {interval1.start}"
    assert (
        interval1.end == interval2.end
    ), f"Expected end {interval2.end}, but got {interval1.end}"
