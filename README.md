# Get the current price of electricity from Nordpool and send an alert to Telegram

They are some crazy times we live in. It appears sometimes there is a surplus of electricity which causes the el. prices to be negative. For a consumer, this is a good thing, but for a el. producer, not so much. 

If you have some solar panels or wind tourbine and sell your electricity, you might not want to sell it when it is negative.

This script will give you a heads up when the price goes below zero, so you can start utlizing your electricity at home instead of selling it for negative profit. In other words, start turning on the dryer, dish washer, of course sauna :). 

## Prerequisites

I am assuming, you are on a linux based system and you need to have Python and the Nordpool Library.

To install Python, just google it.

To install the Nordpool library, run the following command.

```
pip install nordpool
```

## Automating the notifications
  
When the script notifies you correctly of the negative el. prices, the next step is to automate it. 

Run the following command to open your crontab.

```
crontab -e
```

Add the following into it.

```
30 8-18 * * * /usr/bin/python3 /ABSOLUTE PATH TO YOUR PYTHON FILE/example.py >> /ABSOLUTE PATH TO YOUR CRONLOG FILE 2>&1
```

Don't forget to replace the path to your python file and to the location where you want the log. 

This cron schedule will execute the specified command at the 30th minute of every hour between 8 AM and 6 PM. Adjust the time range (8-18 in this example) to match your desired daytime hours. The last run time will be 18:30.

## End Notes

This setup is just a hack to get notified. It is by no means perfect, but it will do the job.

If you found this guide useful, why not let it be known by [sending me a few sats](https://360swim.com/ln-donate-github) or via LN address⚡swmtr@360swim.com .
<br />
<img src="https://360swim.com/user/themes/swimquark/images/ln_git.png" width="400" />

Finally, if you are into swimming, checkout some [swimming tips](https://360swim.com/tips).
