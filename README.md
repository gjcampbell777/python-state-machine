# python-state-machine

### Python State Machine

This is a simple state machine that I created by following a [tutorial](https://dev.to/karn/building-a-simple-state-machine-in-python) that I came across while going through Godot documentation.
However after I finished the tutorial I expanded on it and will continue to expand upon it 
since I find state machines fun and interesting to play around with.

### Setup

To start it boot into python CLI `python3` 
(you should be able to run this with old `python` but I want to keep it up to date and the output will come out weird)

Then run `from simple_device import SimpleDevice` and `device=SimpleDevice()`
to import the functionality and then initalize a state machine you can mess around with.

### Calls

The calls you can make with `device` are `list_events()` and `on_event(event)`

`list_events()` lists all the events you can use with `on_event()` and `on_event()` send that's event info to the state machine.

The events that you can use with `on_event()` are `pin_entered` and `device_locked`
