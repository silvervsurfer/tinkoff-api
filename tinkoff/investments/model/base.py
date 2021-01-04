from enum import Enum
from typing import Optional
from datetime import datetime
from dataclasses import dataclass

import ciso8601
from mashumaro import DataClassJSONMixin
from mashumaro.types import SerializableType


FigiName = str
TickerName = str


class BaseModel(DataClassJSONMixin):
    pass


@dataclass
class Error(BaseModel):
    message: Optional[str] = None
    code: Optional[str] = None


class Status(Enum):
    OK = 'Ok'
    ERROR = 'Error'


class Currency(Enum):
    RUB = 'RUB'
    USD = 'USD'
    EUS = 'EUR'
    GBP = 'GBP'
    HKD = 'HKD'
    CHF = 'CHF'
    JPY = 'JPY'
    CNY = 'CNY'
    TRY = 'TRY'


class InstrumentType(Enum):
    STOCK = 'Stock'
    CURRENCY = 'Currency'
    BOND = 'Bond'
    ETF = 'Etf'


@dataclass
class MoneyAmount(BaseModel):
    currency: Currency
    value: float
