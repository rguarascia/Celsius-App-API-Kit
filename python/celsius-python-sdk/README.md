
# Celsius SDK API Starter Kit for Python

So you want to pull data from your Celsius account via an API? And you prefer Python over Javascript? This library has got your back and will get you setup in no time.

There are four basic functionalities that the API can do.

 - Get Balances
 - Get Total Interest Earned
 - Get Statistics
 - Get All Transactions (Deposits, Withdraws & Interest)

Let's break these down.

# Preheat

- **First** thing you need to do is generate an API key from the app. [View instructions here](https://developers.celsius.network/createAPIKey.html)
- **Second** thing you need to do is email [partners@celsius.network](mailto:partners@celsius.network) requesting a `read only partner key.` Make sure that you send this email from your verified Celsius email address (the one you used to create your account)

# Installation 

Make a directory and start a virtual env for Python:

	$ cd workspace
	$ python3 -m venv env
	$ . env/activate/bin
	$ pip install celsius-python-sdk

If you prefer to install from source, you can do so by:
	
	$ git clone https://github.com/rguarascia/Celsius-App-API-Kit.git
	$ cd python/celsius-python-sdk/
	$ python3 setup.py install

You're ready to start fetching data!

# Prerequisite
	
Start by creating a JSON file for your API and Partner Key in the following format in order to access the functions in the next section.

Format:

	{
	    "X-Cel-Partner-Token": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
	    "X-Cel-Api-Key" : "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx"
	}
Both keys *should* have the layout as `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx` (layout subject to change)

# Fetching the Data!

To use the functions under the library you need to import it. You can do so easily by using this:
	
	import pyCelsius as CEL

Every function below returns a JSON.
## readCreds()
This function reads your credentials from the JSON file you created in the previous step, just provide the _/path/to/creds.json_ to the function and you're good to go!

	userCreds = CEL.readCreds("path/to/creds.json")

## getBalance()

   This function returns you balances per coin.
    
	CEL.getBalance(userCreds)

Return layout

    {
      balance: {
        eth: '0',
        btc: '0',
        dash: '0',
        bch: '0',
        ltc: '0',
        zec: '0',
        btg: '0',
        xrp: '0',
        xlm: '0',
        omg: '0',
        tusd: '0',
        gusd: '0',
        pax: '0',
        usdc: '0',
        dai: '0',
        mcdai: '0',
        cel: '0',
        zrx: '0',
        orbs: '0',
        'usdt erc20': '0',
        tgbp: '0',
        taud: '0',
        thkd: '0',
        tcad: '0',
        eos: '0',
        sga: '0',
        xaut: '0'
      }
    }

## Interest

This function returns how much interest you have earned over the course of your account per coin.

    CEL.getInterest(userCreds)
Return layout

    {
        interest: {
            CEL: {
                amount: 0,
                amount_usd: 0,
                amount_cel: 0
            },
            ETH: {
                amount: 0,
                amount_usd: 0,
                amount_cel: 0
            },
    ...

## Statistics

This function returns unique statistics about your account.

    CEL.getStats(userCreds)
Return Layout

    {
      deposit_count: '0',
      deposit_amount: {
        total_amount_usd: '0',
        BTC: { amount: '0', amount_usd: 0 },
        CEL: { amount: '0', amount_usd: 0 },
        ETH: { amount: '0', amount_usd: 0 },
        XLM: { amount: '0', amount_usd: 0 },
        XRP: { amount: '0', amount_usd: 0 }
      },
      withdrawal_count: '0',
      withdrawal_amount: {
        total_amount_usd: '-0',
        CEL: {
          amount: '-0',
          amount_usd: -0
        },
        ETH: { amount: '-0', amount_usd: -0 },
        LTC: { amount: '-0', amount_usd: -0 }
      },
      interest_count: '0',
      interest_amount: {
        total_amount_usd: '0',
        CEL: { amount: '0', amount_usd: 0 },
        ETH: { amount: '0', amount_usd: 0 },
        LTC: { amount: '0', amount_usd: 0 },
        XLM: { amount: '0', amount_usd: 0 },
        XRP: { amount: '0', amount_usd: 0 }
      }
    }

##  Pagination 

This function returns pagination of every transaction that has happened on your account.

    pagination  = {
	    'page': 1,
	    'perPage': 1
    }
    
    CEL.getTransactions(userCreds, pagination)
Return Layout

    {
      pagination: {
        total: 0,
        pages: 0,
        current: 1,
        per_page: 0,
        showing: '1 - 20'
      },
      record: [
        {
          amount: '0',
          amount_usd: 0,
          coin: 'CEL',
          state: 'confirmed',
          nature: 'interest',
          time: '2020-06-05T05:00:01.000Z',
          tx_id: null
        },
        ...
## Ending Notes
The API is pretty limited to what can be done, however this allows you to read pretty much all activities that have happened on your account. 

Check out the [official documentation here](https://developers.celsius.network/)
