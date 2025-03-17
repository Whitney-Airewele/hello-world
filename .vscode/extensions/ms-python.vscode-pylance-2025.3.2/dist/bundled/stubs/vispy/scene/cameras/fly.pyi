import math

import numpy as np

from ...util import keys
from ...util.event import Event
from ...util.quaternion import Quaternion
from .perspective import PerspectiveCamera

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

class FlyCamera(PerspectiveCamera):
    # Using _rotation1 and _rotation2 for camera states instead of _rotation
    _state_props = ...

    def __init__(self, fov: float = 60, rotation: None | float = None, **kwargs): ...
    @property
    def rotation(self): ...
    @rotation.setter
    def rotation(self, value): ...
    @property
    def rotation1(self): ...
    @rotation1.setter
    def rotation1(self, value): ...
    @property
    def rotation2(self): ...
    @rotation2.setter
    def rotation2(self, value): ...
    @property
    def auto_roll(self): ...
    @auto_roll.setter
    def auto_roll(self, value): ...
    @property
    def keymap(self): ...
    def _set_range(self, init): ...
    def _get_directions(self): ...
    def on_timer(self, event: Event): ...
    def viewbox_key_event(self, event: Event): ...
    def viewbox_mouse_event(self, event: Event): ...
    def _update_projection_transform(self, fx, fy): ...
