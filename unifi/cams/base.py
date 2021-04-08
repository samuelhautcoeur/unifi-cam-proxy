import logging
from typing import Tuple


class UnifiCamBase(object):
    def __init__(self, args, logger=None):
        self.args = args
        if logger is None:
            self.logger = logging.getLogger(__class__)
        else:
            self.logger = logger

    def get_snapshot(self):
        raise NotImplementedError("You need to write this!")

    def get_video_settings(self):
        return {}

    def change_video_settings(self, options):
        pass

    def start_video_stream(
        self, stream_index: str, stream_name: str, destination: Tuple[str, int]
    ):
        raise NotImplementedError("You need to write this!")
