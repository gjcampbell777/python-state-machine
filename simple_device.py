#!/usr/bin/env python3
# simple_device.py

from my_states import LockedState

available_events= {
    "LockedState": "pin_entered",
    "UnlockedState": "device_locked, make_call, start_game, use_camera",
    "CallingState": "hang_up, main_menu",
    "GamingState": "device_locked, end_game, main_menu",
    "CameraState": "device_locked, close_camera, main_menu",
    "All": "pin_entered, device_locked, make_call, start_game, use_camera, main_menu, hang_up, end_game, close_camera"
}

class SimpleDevice(object):
    """ 
    A simple state machine that mimics the functionality of a device from a 
    high level.
    """

    def __init__(self):
        """ Initialize the components. """

        # Start with a default state.
        self.state = LockedState()
        print("View available events with available_events() and all possible events with all_events()")

    def all_events(self):
        print("All events you can call: " + available_events["All"])

    def available_events(self):
        print("Events you can call: " + available_events[str(self.state)])

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)
