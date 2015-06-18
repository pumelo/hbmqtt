# Copyright (c) 2015 Nicolas JOUANIN
#
# See the file license.txt for copying permission.
import unittest

from hbmqtt.mqtt.suback import SubackPacket, SubackPayload
from hbmqtt.mqtt.packet import PacketIdVariableHeader
from hbmqtt.codecs import *

class SubscribePacketTest(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()

    def test_from_stream(self):
        data = b'\x90\x06\x00\x0a\x00\x01\x02\x80'
        stream = asyncio.StreamReader(loop=self.loop)
        stream.feed_data(data)
        stream.feed_eof()
        message = self.loop.run_until_complete(SubackPacket.from_stream(stream))
        self.assertEqual(message.payload.return_codes[0], SubackPayload.RETURN_CODE_00)
        self.assertEqual(message.payload.return_codes[1], SubackPayload.RETURN_CODE_01)
        self.assertEqual(message.payload.return_codes[2], SubackPayload.RETURN_CODE_02)
        self.assertEqual(message.payload.return_codes[3], SubackPayload.RETURN_CODE_80)

    def test_to_stream(self):
        variable_header = PacketIdVariableHeader(10)
        payload = SubackPayload(
            [SubackPayload.RETURN_CODE_00, SubackPayload.RETURN_CODE_01, SubackPayload.RETURN_CODE_02, SubackPayload.RETURN_CODE_80
            ])
        publish = SubackPacket(variable_header=variable_header, payload=payload)
        out = publish.to_bytes()
        self.assertEqual(out, b'\x90\x06\x00\x0a\x00\x01\x02\x80')