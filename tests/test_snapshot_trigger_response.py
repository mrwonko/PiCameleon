import sys
sys.path.append("/picameleon")
from datetime import datetime
import unittest
from unittest.mock import MagicMock, patch, call, ANY


class TestSnapshot(unittest.TestCase):

    @patch("picamerax.PiCamera.capture")
    def test_trigger_response(self, mocked_capture):
        from trigger_responses.snapshot import Snapshot
        trigger_reponse = Snapshot(port=0,
                                   format="jpeg",
                                   destination_path="/tmp/")
        trigger_reponse._trigger_response()
        mocked_capture.assert_called_once_with(ANY,
                                               format='jpeg',
                                               resize=None,
                                               splitter_port=0,
                                               use_video_port=True)


if __name__ == '__main__':
    unittest.main()
