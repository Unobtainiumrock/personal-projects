const puppeteer = require('puppeteer');
// const site_1 = 'https://www.linkedin.com/';
// const site_2 = 'https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in';
const site_3 = 'https://data.berkeley.edu/data-science-discovery-fall-2023-overview';

(async () => {
    // Launch a browser instance
    const browser = await puppeteer.launch({ headless: 'new' });

    // Create a new tab in the browser. 
    const page = await browser.newPage();

    // Navigate to a website.
    try {
        await page.goto(
            site_3,
            { waitUntil: 'networkidle2', timeout: 30000 }
            );
    } catch(e) {
        console.error("Navigation timed out. Proceeding without waiting for networkidle2...");
        await page.waitForSelector('body');
    }    
    
    try {
        const links = await page.evaluate(() => {
            return Array.from(document.querySelectorAll('div.field__item > div > div > a.image-wrapper ')).map((a) => a.href);
        })

        const googleFormsLinks = links.filter(link => link.includes('forms.gle'));

        googleFormsLinks.forEach((link) => {
            console.log(link);
        });

    } catch (e) {
        console.error('Error occurred: ', e);
    } finally {
        await browser.close();
    }

    // // Grab the page's content
    // const content = await page.evaluate(() => {
    //     return document.documentElement.outerHTML;
    // });

    // console.log(content);
    console.log('Success');
})();
