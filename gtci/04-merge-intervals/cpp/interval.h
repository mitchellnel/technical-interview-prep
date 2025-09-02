#ifndef INTERVAL_H
#define INTERVAL_H

class Interval {
   public:
    int start = 0;
    int end = 0;

    Interval(int start, int end) {
        this->start = start;
        this->end = end;
    }

    bool operator==(const Interval& other) const {
        return start == other.start && end == other.end;
    }
};

#endif  // INTERVAL_H
