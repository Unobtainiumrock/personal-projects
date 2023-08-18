const puppeteer = require('puppeteer');

(async () => {
    // Launch a browser instance
    const browser = await puppeteer.launch({ headless: 'new' });

    // Create a new tab in the browser. 
    const page = await browser.newPage();

    // Navigate to a website.
    try {
        await page.goto(
            'https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in',
            { waitUntil: 'networkidle2', timeout: 30000 }
            );
    } catch(e) {
        console.error("Navigation timed out. Proceeding without waiting for networkidle2...");
        await page.waitForSelector('body');
    }    
    
    // Grab the page's content
    const content = await page.evaluate(() => {
        return document.documentElement.outerHTML;
    });

    console.log(content);

    console.log('Success');
})();