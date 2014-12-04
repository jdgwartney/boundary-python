#!/usr/bin/env python
import statsd
from time import sleep
c = statsd.StatsClient('localhost', 8125)

while True:
   c.incr('foo')  # Increment the 'foo' counter.
   c.timing('stats.timed', 320)  # Record a 320ms 'stats.timed'.
   sleep(1)
