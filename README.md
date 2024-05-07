# Coinbase Dashboard using Streamlit

Dashboard to visualize trading product information. Users can look up all the trading symbols in the exchange and select historical prices of symbol based on:
    - Start Date
    - End Date
    - Granularity 

#
Before running dashboard, make an `.env` file in the root directory in one does not exist or add the following to your environment variable:
    - `COINBASE_API_BASE_URL`
    - `COINBASE_API_BASE_URL_WSS`
    - `COINBASE_API_KEY`
    - `COINBASE_API_SECRET`
    - `COINBASE_API_PASSPHRASE`

Make sure all the environment variables are setup properly or else the dashbaord will throw an error.

#
### 2 main ways to run dashboard:

1. To run using **Docker**:
    - Running Dashboard:
        Type `make run` in terminal of root directory where Makefile is present
        This should open a connection at `0.0.0.0:8501`, and so to view dashboard go to `127.0.0.1:8501`
        Make sure the port numbers are the same as the docker one, check DockerFile
    - Stopping docker-compose:
        Type `docker-compose down`

2. To run locally using **Poetry**:
    - Install poetry:
        Type `pip install poetry`
    - Running Dashboard:
        Type `poetry run streamlit run dashboard/Home.py`
        Should start at `localhost`

To run sample tests in `./dashboard/tests`:
    Type `poetry pytest -v`



# Features of App:

1. Landing page:
    - Includes all trading pairs and their information in a scrollable table
    - Includes Number of total trading pairs
2. Historical page:
    - Drop down menu to view and select of all available symbols
    - Date range selection
    - Granularity selection
    - Candle-stick graph of selected symbol
    - Line-plot graph of selected symbol with option to choose linegraph
3. Account:
    - Checks whether AUTH is working
    - Gets all trading accounts of user based on api credentials given

