#ifndef UTIL_H
#define UTIL_H

#include <cassert>
#include <vector>

#include "interval.h"

void assert_equal_interval(const Interval& a, const Interval& b) {
    assert(a.start == b.start && a.end == b.end);
}

void assert_equal_intervals(const std::vector<Interval>& a,
                            const std::vector<Interval>& b) {
    assert(a.size() == b.size());
    for (size_t i = 0; i < a.size(); i++) {
        assert_equal_interval(a[i], b[i]);
    }
}

#endif  // UTIL_H
