# Automate My Job Hunt

I don't enjoy doing repetitive tasks over and over, especially when I can see ways in which they can be automated. I value my time very much and will gladly invest the upfront time in order to save more time in the long run. Also, its so fun to automate things!

## Curent Process

1. Grab lots of data on job postings using [Puppeteer](https://developer.chrome.com/docs/puppeteer/)
    - Get a crude crawler whipped together and refine it as I work along.
2. Interpret the data using some sort of sentiment analysis etc to find a succint way to represent the data.
    - Turn collected data into a vector form via embeddings and compute the inner product between it and my parameters vector for an ideal role.
    - Need to define what an ideal role is to me. (High priority)
3. For each 'ideal position' found:
    - Take my existing resume and the job posting and generate an ideal version of my resime that matches the posting better.
    - Create a list of tasks that need to be complete in preparation for the job. This can range from types of tools to brush up on, terminology to familiarize myself with, and ways to prepare for behavioral interview.
    - Automatically integrate the deadline for the posting into my calendar
    - integrate all of this data into an excel, csv, or Google sheets.
4. Have my future voice assistance integrate the calendar data with the hunting process. Essentially, we want to increase the surface area through which I can interface with this process.
