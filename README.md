# python-state-machine

### Python State Machine

This is a state machine used to emulate a locked/unlocked device that I created by following a [tutorial](https://dev.to/karn/building-a-simple-state-machine-in-python) that I came across while going through Godot documentation.
However after I finished the tutorial I expanded on it and will continue to expand upon it 
since I find state machines fun and interesting to play around with.

### Setup

To start it boot into python CLI `python3` 
(you should be able to run this with old `python` but I want to keep it up to date and the output will come out weird)

Then run `from simple_device import SimpleDevice` and `device=SimpleDevice()`
to import the functionality and then initalize a state machine you can mess around with.

### Calls

The calls you can make with `device` are `state()`, `all_events()`, `available_events()` and `on_event(event)`

`state()` displays the state you are currently in.

`all_events()` displays all possible events you can call.

`available_events()` displays all events that you can call with in your current state that won't be ignored.

`on_event(event)` sends the event to your current state to be handled accordingly.
