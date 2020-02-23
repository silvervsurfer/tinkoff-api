from aiohttp import ClientWebSocketResponse
from tinkoff.base import BaseHTTPClient
from tinkoff.investments.model.base import FigiName
from tinkoff.investments.model.streaming import BaseEvent, BaseEventKey, EventName
from tinkoff.investments.model.market.candles import CandleResolution
from typing import Any, Callable, Dict, List, Optional

class CandleEventStream:
    _subscribers: Dict[BaseEventKey, Callable] = ...
    def __call__(self, figi: FigiName, interval: CandleResolution): ...
    async def subscribe(self, callback, figi: FigiName, interval: CandleResolution) -> None: ...
    async def unsubscribe(self, figi: FigiName, interval: CandleResolution) -> None: ...

class OrderBookEventStream:
    _subscribers: Dict[BaseEventKey, Callable] = ...
    def __call__(self, figi: FigiName, depth: int): ...
    async def subscribe(self, callback, figi: FigiName, depth: int) -> None: ...
    async def unsubscribe(self, figi: FigiName, depth: int) -> None: ...

class InstrumentInfoEventStream:
    _subscribers: Dict[BaseEventKey, Callable] = ...
    def __call__(self, figi: FigiName): ...
    async def subscribe(self, callback, figi: FigiName) -> None: ...
    async def unsubscribe(self, figi: FigiName) -> None: ...

class EventsBroker:
    candles: CandleEventStream = CandleEventStream()
    orderbooks: OrderBookEventStream = OrderBookEventStream()
    instrument_info: InstrumentInfoEventStream = InstrumentInfoEventStream()
    _routes: Dict[EventName, Any] = ...
    def __init__(self) -> None: ...
    def add_publisher(self, client: TinkoffInvestmentsStreamingClient) -> None: ...
    async def publish(self, event: BaseEvent) -> None: ...

class TinkoffInvestmentsStreamingClient(BaseHTTPClient):
    events: EventsBroker = EventsBroker()
    _receive_timeout: Optional[float]
    _heartbeat: Optional[float]
    _reconnect_timeout: float
    def __init__(
            self,
            token: str,
            events: EventsBroker = None,
            receive_timeout: Optional[float] = 5,
            heartbeat: Optional[float] = 3,
            reconnect_timeout: float = 3
    ) -> None: ...
    async def run(self) -> None: ...
    async def _run(self, ws: ClientWebSocketResponse) -> None: ...
    async def _subscribe_to_streams(self, ws: ClientWebSocketResponse) -> None: ...
    @property
    def _event_streams(self):
        return (self.events.candles, self.events.orderbooks,
                self.events.instrument_info)
    def _subscription_keys(self) -> List[Dict[str, Any]]: ...