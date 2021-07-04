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

        if event == 'make_call' or event == 'start_game' or event == 'use_camera':
            print("Device is locked")

        if event == 'hang_up' or event == 'end_game' or event == 'close_camera':
            print("That program is currently not in use")

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

        if event == 'make_call':
            return CallingState()

        if event == 'start_game':
            return GamingState()

        if event == 'use_camera':
            return CameraState()

        return self

class CallingState(State):
    """
    The state which indicates that you are making a call.
    """

    def on_event(self, event):
        if event == 'device_locked':
            print("That's rude, you should hang up first")

        if event == 'pin_entered':
            print("Device already unlocked")

        if event == 'hang_up' or event == 'main_menu':
            return UnlockedState()

        return self

class GamingState(State):
    """
    The state which indicates that you are playing a game.
    """

    def on_event(self, event):
        if event == 'device_locked':
            return LockedState()

        if event == 'pin_entered':
            print("Device already unlocked")

        if event == 'end_game' or event == 'main_menu':
            return UnlockedState()

        return self

class CameraState(State):
    """
    The state which indicates that you are taking a photo/video.
    """

    def on_event(self, event):
        if event == 'device_locked':
            return LockedState()

        if event == 'pin_entered':
            print("Device already unlocked")

        if event == 'close_camera' or event == 'main_menu':
            return UnlockedState()

        return self
# End of our states.
