# Trade API

This is a simple FastAPI application that provides endpoints to manage and retrieve trade data. It allows you to filter trades based on various parameters such as asset class, trade date, price, and trade type.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/trade-api.git

2.Change into the project directory:
cd trade-api


3 Install the dependencies:

pip install -r requirements.txt

#Usage
1. Start the FastAPI application:
uvicorn main:app --reload

2. Access the API documentation:

Open your web browser and visit http://localhost:8000/docs to view the Swagger UI documentation. Here, you can explore the available endpoints and test them using the interactive interface.

3. Retrieve trades:

Use the /trades endpoint to retrieve trades based on different query parameters. The available parameters are:

assetClass (optional): Asset class of the trade.
start (optional): The minimum date for the tradeDateTime field.
end (optional): The maximum date for the tradeDateTime field.
minPrice (optional): The minimum value for the tradeDetails.price field.
maxPrice (optional): The maximum value for the tradeDetails.price field.
tradeType (optional): The tradeDetails.buySellIndicator is a BUY or SELL.
For example, to retrieve all trades with asset class "Equity" and trade type "BUY", you can make the following request:

GET /trades?assetClass=Equity&tradeType=BUY

4.Retrieve a trade by ID:

Use the /trades/{trade_id} endpoint to retrieve a specific trade by its ID. Replace {trade_id} with the actual ID of the trade.

For example, to retrieve the trade with ID "123456789", you can make the following request:

GET /trades/123456789







