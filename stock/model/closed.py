import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class ClosedPosition:
    """
    closed positions
    can evaluate gains and losses
    """
    acquired: datetime.date
    """acquired/purchase date"""
    end: datetime.date
    """sold date"""
    quantity: float
    """shares, can be fractional"""
    stock: str
    """stock ticker"""
    cost: float
    """purchase price per share"""
    sold: float
    """sold price per share"""
    gpd: float
    """gain/loss per day"""
    long: float = 0.0
    """long term gain/loss"""
    short: float = 0.0
    """short term gain/loss"""
