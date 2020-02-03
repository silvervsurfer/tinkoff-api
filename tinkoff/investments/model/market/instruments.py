from dataclasses import dataclass
from typing import Optional

from tinkoff.investments.model.base import BaseModel, Currency


FigiName = str
TickerName = str


@dataclass
class MarketInstrument(BaseModel):
    figi: FigiName
    ticker: TickerName
    lot: int
    name: str
    currency: Optional[Currency] = None
    isin: Optional[str] = None
    minPriceIncrement: float = None
