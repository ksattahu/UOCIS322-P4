# UOCIS322 - Project 4 #
Brevet time calculator.

## Author: Kale Satta-Hutton, ksattahu@uoregon.edu ##

## Overview

Implementation of the RUSA ACP controle time calculator with Flask and AJAX.

### ACP controle times

The algorithm for calculating controle times is described here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). Additional background information is given here [https://rusa.org/pages/rulesForRiders](https://rusa.org/pages/rulesForRiders).

The algorithm does not account past 20% of each brevet, uses the French
calculation for KM 0-60, each brevet has the same open and close time up to 20%
past. Each specific brevet has a unique max, these are :(in hours and minutes, HH:MM)
3:30 for 200 KM, 20:00 for 300 KM, 27:00 for 400 KM, 40:00 for 600 KM, and 75:00 for 1000 KM
Each starting time is relative to the previous starting times, similar to the closing times.

Test suite can be ran inside the docker container use nosetests .

The test suite is not verbose but does account for unique use cases for the ACP
it specifically shows the cases listed above.

#

## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.
