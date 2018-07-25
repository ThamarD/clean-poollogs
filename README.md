[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ThamarD/cleanpoollogs/LICENSE)
[![docs](https://img.shields.io/badge/doc-online-blue.svg)](https://github.com/ThamarD/cleanpoollogs/wiki)

# Cleanpoollogs
Cleanpoollogs is a cleanup script for the much used DPoS poollog.json (by Dakk) for delegate pay-out in lisk/shift/ARK/rise/oxy/lwf/kapu/onz etc 

This script removes the voters entry from the people who have unvoted you as a delegate.
And if somebody revote me, no problem! The script is ok with that. And if sombody unvote me, for the second or third time...? The pending and received will add up and the date when the unvote is detected is registerd in the log file.  

## Configuration / prerequisists
This script assumes 
- that you have installed the "Lisk pool distribution software" by Dakk.
- that this script will be started form that directory, it needs access to
    - config.json
    - poollogs.json

It uses the information from the config.json which was created during the Lisk pool setup and reads, cleans and saves the poollogs.json.

## Running it
First clone the Cleanpoollogs repository (I asume you already have installed the Lisk pool and requests):

`git clone https://github.com/ThamarD/poollogs-cleanup`

`cd poollogs-cleanup`


Then start it:

`python3 cleanpoollogs.py`

or if you are using another config file:

`python3 cleanpoollogs.py -c config2.json`

It produces 2 files 
- First file is called "removedvotespoollogs.json" with all the removed voters with their payout, received, pending payout and the date when the "unvote" is registered  by the script.
```
        "7710578903217350527X": {
            "pending": 0.658589451817388,
            "received": 1045.583572460881664,
            "unvotedate": [
                "2018-05-21 22:35",
                "2018-07-25 19:34"
            ]
        },
```
- Second file is the cleaned poollogs.json

So depending on when you run the script the "unvotedate" is more accurate or not (it is not based on blockchain info). 

## Using it
You can run this script after you have done your pay-out (daily, weekly, or other interval)
these are the steps I normaly do
1. create a backup copy of the initial "poollogs.json" in a directory (here "Payments"), just in case
2. do the payment run
3. clean-up the poollogs.json
4. create a backup copy of the new "poollogs.json" in a directory (here "Payments"), just in case
5. create a backup copy of the new "payments.sh" in a directory (here "Payments"), just in case
6. execute payment

```
cp ~/payout-pool/poollogs.json ~/payout-pool/Payments/$(date +%Y%m%d_%H%M%S).PrePayment.poollogs.json
sleep 2
python3 ~/payout-pool/liskpool.py -y -c ~/payout-pool/config.json
python3 ~/payout-pool/cleanpoollogs.py
sleep 2
cp ~/payout-pool/poollogs.json ~/payout-pool/Payments/$(date +%Y%m%d_%H%M%S).PostPayment.poollogs.json
cp ~/payout-pool/payments.sh ~/payout-pool/Payments/$(date +%Y%m%d_%H%M%S).payments.sh
bash ~/payout-pool/payments.sh
```

If you want to use the above, remember to create the Payments directory! In that direcoty overtime you will see the history of your payments in this way:
```
20180721_073501.PrePayment.poollogs.json
20180721_073507.PostPayment.poollogs.json
20180721_073511.payments.sh
```

## Donations
Besides voting for delegate Thamar, if you like this software and it helps you to get organized, I would greatly appreciate if you would consider to show some support by donating to one of the below mentioned addresses.

- OXY: 		902564290011692795X
- LWF: 		2526916071607963001LWF
- ONZ: 		ONZfxHuBy5e39nipSZuSgcKhYURE6QkWsK2j
- Shift: 	18040765904662116201S
- Lisk: 	8890122000260193860L
- BTC: 		1NrA8k8wNRwEZj2ooKQEf2fFnF6KqTE32T


## License

```
Copyright (c) 2018 ThamarD

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
```

