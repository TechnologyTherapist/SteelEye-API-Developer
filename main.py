from typing import List, Optional
from datetime import datetime
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

# Mocked database or in-memory data structure
trades_db = []

class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")
    price: float = Field(description="The price of the Trade.")
    quantity: int = Field(description="The amount of units traded.")

class Trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded.")
    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with.")
    instrument_id: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded.")
    instrument_name: str = Field(alias="instrumentName", description="The name of the instrument traded.")
    trade_date_time: datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")
    trade_details: TradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")
    trade_id: str = Field(alias="tradeId", default=None, description="The unique ID of the trade")
    trader: str = Field(description="The name of the Trader")

@app.get("/trades")
def get_trades(
    assetClass: Optional[str] = Query(None, description="Asset class of the trade."),
    start: Optional[datetime] = Query(None, description="The minimum date for the tradeDateTime field."),
    end: Optional[datetime] = Query(None, description="The maximum date for the tradeDateTime field."),
    minPrice: Optional[float] = Query(None, description="The minimum value for the tradeDetails.price field."),
    maxPrice: Optional[float] = Query(None, description="The maximum value for the tradeDetails.price field."),
    tradeType: Optional[str] = Query(None, description="The tradeDetails.buySellIndicator is a BUY or SELL")
) -> List[Trade]:
    filtered_trades = trades_db
    
    if assetClass:
        filtered_trades = [trade for trade in filtered_trades if trade.asset_class == assetClass]
    
    if start:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_date_time >= start]
    
    if end:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_date_time <= end]
    
    if minPrice:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_details.price >= minPrice]
    
    if maxPrice:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_details.price <= maxPrice]
    
    if tradeType:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_details.buySellIndicator == tradeType]
    
    return filtered_trades

@app.get("/trades/{trade_id}")
def get_trade_by_id(trade_id: str) -> Trade:
    trade = next((trade for trade in trades_db if trade.trade_id == trade_id), None)
    if trade:
        return trade
    else:
        raise HTTPException(status_code=404, detail="Trade not found.")

# Mock data for testing purposes
trade1 = Trade(
    asset_class="Equity",
    counterparty="ABC Corp",
    instrument_id="TSLA",
    instrument_name="Tesla",
    trade_date_time=datetime(2023, 6, 1, 10, 30),
    trade_details=TradeDetails(buySellIndicator="BUY", price=100.0, quantity=10),
    trade_id="123456789",
    trader="John Doe"
)
trade2 = Trade(
    asset_class="Equity",
    counterparty="XYZ Corp",
    instrument_id="AAPL",
    instrument_name="Apple",
    trade_date_time=datetime(2023, 6, 2, 15, 45),
    trade_details=TradeDetails(buySellIndicator="SELL", price=150.0, quantity=5),
    trade_id="987654321",
    trader="Jane Smith"
)
trades_db = [trade1, trade2]

@app.get("/trades")
def get_trades(
    assetClass: Optional[str] = Query(None, description="Asset class of the trade."),
    start: Optional[datetime] = Query(None, description="The minimum date for the tradeDateTime field."),
    end: Optional[datetime] = Query(None, description="The maximum date for the tradeDateTime field."),
    minPrice: Optional[float] = Query(None, description="The minimum value for the tradeDetails.price field."),
    maxPrice: Optional[float] = Query(None, description="The maximum value for the tradeDetails.price field."),
    tradeType: Optional[str] = Query(None, description="The tradeDetails.buySellIndicator is a BUY or SELL")
) -> List[Trade]:
    filtered_trades = trades_db
    
    if assetClass:
        filtered_trades = [trade for trade in filtered_trades if trade.asset_class == assetClass]
    
    if start:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_date_time >= start]
    
    if end:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_date_time <= end]
    
    if minPrice:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_details.price >= minPrice]
    
    if maxPrice:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_details.price <= maxPrice]
    
    if tradeType:
        filtered_trades = [trade for trade in filtered_trades if trade.trade_details.buySellIndicator == tradeType]
    
    return filtered_trades

@app.get("/trades/{trade_id}")
def get_trade_by_id(trade_id: str) -> Trade:
    trade = next((trade for trade in trades_db if trade.trade_id == trade_id), None)
    if trade:
        return trade
    else:
        raise HTTPException(status_code=404, detail="Trade not found.")
