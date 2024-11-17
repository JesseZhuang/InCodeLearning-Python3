"""
stock in watchlist
"""
import datetime
import enum
from dataclasses import dataclass


class MarketCapType(enum.IntEnum):
    MEGA = 4
    """200B or more"""
    LARGE = 3
    """30B or more"""
    MID = 2
    """5B,30B"""
    SMALL = 1
    """250M,5B"""
    MICRO = 0
    """<250M"""


@dataclass
class MarketCap:
    category: MarketCapType
    cap: int


@dataclass
class Stock:
    _id: str
    """ticker"""
    name: str
    pe: float
    """price/earning ratio"""
    industry: str
    sector: str
    volatility: float
    cap_enum: int
    """use enum value defined above"""
    cap: int
    """unit million"""
    rating: float
    """analyst rating"""
    shares: int
    short: float
    """short percentage"""
    created: datetime.date
