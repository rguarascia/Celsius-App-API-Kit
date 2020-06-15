// Ryan Guarascia
// July, 14, 2020
// Starter kit for users trying to use the Celsius Network APP API key to read data out of the app.

const {
    Celsius,
    AUTH_METHODS,
    ENVIRONMENT
} = require('celsius-sdk')
const partnerKey = process.env.PARTNER_TOKEN
const fs = require('fs');

init();

/**
 * Runs the functions from the Celsius API
 */
function init() {
    readKeys();
    runCelsius('balance');
    // runCelsius("interest");
    // runCelsius('stats');
    // runCelsius('pagetation');
}

/**
 * Reads in the partner key and API key.
 */
function readKeys() {
    var content = fs.readFileSync("credentials.json");
    var json = JSON.parse(content);
    process.env.PARTNER_TOKEN = json['partnerKey'];
    process.env.APP_KEY = json['appKey'];
}


/**
 * Calls the API with the respected endpoint
 * @param {string} call The function you'd like to call
 */
function runCelsius(call) {
    Celsius({
        authMethod: AUTH_METHODS.API_KEY,
        partnerKey: process.env.PARTNER_TOKEN
    }).then((celsius) => {
        console.warn("successfully connected");
        switch (call) {
            case "balance":
                celsius.getBalanceSummary(process.env.APP_KEY).then((balanceSummary) => {
                    console.log(balanceSummary)
                })
                    .catch((error) => {
                        console.error(error)
                    })
                break;
            case 'interest':
                celsius.getInterestSummary(process.env.APP_KEY).then((interestSummary) => {
                    console.log(interestSummary)
                })
                    .catch((error) => {
                        console.log(error)
                    })
                break;
            case 'stats':
                celsius.getStatistics(process.env.APP_KEY).then((statistics) => {
                    console.log(statistics);
                }).catch((error) => {
                    console.log(error);
                })
                break;
            case 'pagetation':
                const pagination = {
                    page: 1,
                    perPage: 20
                }

                celsius.getTransactionSummary(pagination, process.env.APP_KEY).then((transactions) => {
                    console.log(transactions)
                })
                    .catch((error) => {
                        console.log(error)
                    })
                break;
            default:
                console.log("invalid selection");
                break;
        }
    })
}