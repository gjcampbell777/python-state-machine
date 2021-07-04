#!/usr/bin/env python3
# my_states.py

from state import State

# Start of our states
class LockedState(State):
    """
    The state which indicates that there are limited device capabilities.
    """

    def on_event(self, event):
        if event == 'pin_entered':
            return UnlockedState()

        if event == 'device_locked':
            print("Device already locked")

        return self


class UnlockedState(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """

    def on_event(self, event):
        if event == 'device_locked':
            return LockedState()

        if event == 'pin_entered':
            print("Device already unlocked")

        return self
# End of our states.
