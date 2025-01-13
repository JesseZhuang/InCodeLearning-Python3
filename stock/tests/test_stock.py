import dataclasses
import json
from unittest import TestCase

from stock.model.stock import MarketCap, MarketCapType


class TestMarketCap(TestCase):
    m = MarketCap(MarketCapType.MEGA, 1)

    def test_dataclass_to_string(self):
        """dataclass with an enum field"""
        self.assertEqual('MarketCap(category=<MarketCapType.MEGA: 4>, cap=1)', str(self.m), )
        # s = json.dumps(dataclasses.asdict(self.m))
        # print(json.loads(s, MarketCap))

    def test_dataclass_json_serialization(self):
        s = json.dumps(dataclasses.asdict(self.m))
        self.assertEqual('{"category": 4, "cap": 1}', s)
