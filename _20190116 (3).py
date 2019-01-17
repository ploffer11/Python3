from dataclasses import make_dataclass
from dataclasses import dataclass

Stock = make_dataclass("Stock", ["symbol", "current", "high", "low"])
stock = Stock("FB", 150, 190, 170)

class StockRegClass:
    def __init__(self, name, current, high, low):
        self.name, self.current, self.high, self.low = (
            name, current, high, low
        )

# dataclass is convenient
# give you more useful string representation than the regular version (==, ect.)

@dataclass
class StockDecorated:
    name: str
    current: float 
    high: float
    low: float

@dataclass
class StockDefaults:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0
 
@dataclass(order=True)
class StockOrdered:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0

s = StockDefaults('FB')
s = StockDefaults('FB', 1, 2, 3)

stock_ordered1, stock_ordered2, stock_ordered3 = (
    StockDecorated("FB", 177.46, high=178.67, low=175.78),
    StockOrdered("FB"),
    StockDecorated("FB", 178.42, high=179.28, low=176.39)
)

