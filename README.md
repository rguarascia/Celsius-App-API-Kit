# Celsius APP API Starter Kit

So you want to pull data programmatically from your Celsius account via API eh? No worries.
This is the starter kit to get you off your feet and creating in no time.

This example is done in Node.JS however it should work natively in Javascript. 

There are four basic functionalities that the API can do.

 - Get Balances
 - Get Total Interest Earned
 - Get Statistics
 - Get All Transactions (Deposits, Withdraws & Interest)

Let's break these down.

# Preheat

The **First** thing you need to do is generate an API key from the app. [View instructions here](https://developers.celsius.network/createAPIKey.html)
The **Second** thing you need to do is email [partners@celsius.network](mailto:partners@celsius.network) requesting a `read only partner key.` Make sure that you send this email from your verified Celsius email address (the one you used to create your account with.

# Ingredients 

Start up a project (or clone this repo) and fire up a terminal window.

If you are cloning this repo, open terminal to the root of the project and download the SDK via `npm install.` This will install the [Celsius SDK](https://www.npmjs.com/package/celsius-sdk).

If you are starting a fresh project, just fire up terminal, initialize a npm env by typing `npm init` and fill out the options to your liking. After the init is finished, download the Celsius SDK via `npm i celsius-sdk`

Set up your environment by setting up the initializers.

    const { Celsius,
	    AUTH_METHODS,
	    ENVIRONMENT } =  require('celsius-sdk') 
	
	Celsius({
	    authMethod: AUTH_METHODS.API_KEY,
	    partnerKey: process.env.PARTNER_TOKEN
	    // the docs says to use the staging environment however we want production so we can ignore it 
    }).then((celsius) => {  
	    // code goes here
    }

*Now lets get baking.*

# Lets Bake!

For this example, I have stored my credentials in a JSON file with the scheme

    {
    	"partnerKey": "partner key from email",
    	"appKey": "key from the app"
    }
Both keys *should* have the layout as `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx` (layout subject to change)

## Balances

   This promise function returns you balances per coin. 
    
	celsius.getBalanceSummary(process.env.APP_KEY).then((balanceSummary) => {
		 console.log(balanceSummary)
    })
    .catch((error) => {
	    console.error(error)
    })

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

This promise function returns how much interest you have earned over the course of your account per coin.

    celsius.getInterestSummary(process.env.APP_KEY).then((interestSummary) => {
	    console.log(interestSummary)
    })
    .catch((error) => {
	    console.log(error)
    })
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

This promise function returns unique statistics about your account.

    celsius.getStatistics(process.env.APP_KEY).then((statistics) => {
	    console.log(statistics);
    }).catch((error) => {
	    console.log(error);
    })
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

This promise function returns pagination of every transaction that has happened on your account.

    const  pagination  = {
	    page: 1,
	    perPage: 1
    }
    
    celsius.getTransactionSummary(pagination, process.env.APP_KEY).then((transactions) => {
	    console.log(transactions)
    })
    .catch((error) => {
	    console.log(error)
    })
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
