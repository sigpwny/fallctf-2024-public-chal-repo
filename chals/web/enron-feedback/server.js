const express = require('express');
const bodyParser = require('body-parser');
const puppeteer = require('puppeteer');
const crypto = require('crypto');
const fs = require('fs');

const secret_endpoint = crypto.randomBytes(32).toString('hex');

const port = 1337;

const app = express();

const flags = fs.readFileSync('flag.txt', 'utf8').split('\n');

app.use(bodyParser.urlencoded({extended: false}));
app.set('view engine', 'ejs');

app.get('/', async function(req, res) {
    res.render('index', {endpoint: 'submit', message: `Please don't submit embezzlement requests. We won't give you money.`});
});

app.get('/rematch', async function(req, res) {
    res.render('index', {endpoint: 'submit-rematch', message: `There's an old saying in Tennessee—I know it's in Texas, probably in Tennessee—that says, 'Fool me once, shame on... shame on you. Fool me—you can't get fooled again.'`});
});

// endpoint for only admin to access your name idea (finding this is not meant to be the challenge)
app.get('/'+secret_endpoint, function(req, res) {
    const message = req.query.message ?? '';

    res.render('view', {message, note: `Reminder: please do not accept embezzlement requests from the public form. ${flags[1]}`});
});

// simulate the admin opening your feedback message
async function admin(message) {
    const browser = await puppeteer.launch({args: ['--no-sandbox']});
    const page = await browser.newPage();

    let didpopup = false;
    page.on('dialog', async dialog => {
        didpopup = true;
        await dialog.accept();
    });

    await page.setExtraHTTPHeaders({'is-bot': 'true'});

    await page.setDefaultNavigationTimeout(3000);

    await page.setBypassCSP(true);

    try {
        const a = await page.goto(`http://localhost:${port}/${secret_endpoint}?message=${encodeURIComponent(message)}`, {
            waitUntil: 'networkidle0'
        });
        await page.waitForDelay(2000);
    } catch(e) {
        // console.error(e);
    } finally {
        await page.close();
        await browser.close();
    }

    return didpopup;
}

// endpoint for you to submit your feedback message to the admin
app.get('/submit', async (req, res) => {
    // check if the request is from the bot (prevent infinite looping)
    if (req.headers['is-bot']) {
        return res.render('view', {message: 'hey!', note: ''});
    }
    
    // get parameters from the the form you submitted
    const message = req.query['message'] ?? '';

    // simulate the admin opening your name idea
    const didpopup = await admin(message);

    // send you back your own name idea so you can preview what the admin saw
    if (didpopup) {
        return res.render('view', {message, note: `The admin decided to accept your request because they were confused by your alert. ${flags[0]}`});
    } else {
        return res.render('view', {message, note: `Your feedback has been carefully reviewed by the admin's trash bin.`});
    }
});

// endpoint for you to submit your feedback message to the admin
app.get('/submit-rematch', async (req, res) => {
    // check if the request is from the bot (prevent infinite looping)
    if (req.headers['is-bot']) {
        return res.render('view', {message: 'hey!', note: ''});
    }
    
    // get parameters from the the form you submitted
    const message = req.query['message'] ?? '';

    // check if you're trying to pull a fast one
    if (/(script|img|svg)/i.test(message)) {
        return res.render('view', {message: 'Nice try, bucko!', note: `The Enron system has detected your attempt to embezzle money from the company.`});
    }

    // simulate the admin opening your name idea
    const didpopup = await admin(message);

    // send you back your own name idea so you can preview what the admin saw
    if (didpopup) {
        return res.render('view', {message, note: `The admin decided to accept your request because they were confused by your alert. ${flags[2]}`});
    } else {
        return res.render('view', {message, note: `Your feedback has been carefully reviewed by the admin's trash bin.`});
    }
});

app.listen(port, function() {
    console.log('Listening on port ' + port);
});
