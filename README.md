[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ThamarD/clean-poollogs/blob/master/LICENSE)
[![docs](https://img.shields.io/badge/doc-online-blue.svg)](https://github.com/ThamarD/clean-poollogs/blob/master/wiki)

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

Method 1
First clone the Cleanpoollogs repository (I asume you already have installed the Lisk pool and requests):

`git clone https://github.com/ThamarD/clean-poollogs`

`cd clean-poollogs`

`cp cleanpoollogs.py ~/lisk-pool/cleanpoollogs.py`

`cd ~/lisk-pool/`


Method 2
`cd ~/lisk-pool/`

`wget https://raw.githubusercontent.com/ThamarD/clean-poollogs/master/cleanpoollogs.py`


Tip: It is a good practice to make a backup of your poollogs.json while you are trying something new!

Then start the python script:

`python3 cleanpoollogs.py`

or if you are using another config file for your "lisk-pool":

`python3 cleanpoollogs.py -c config2.json`

It produces 2 files 
- First file is called "removedvotespoollogs.json" with all the removed voters with their received, pending payout and the date when the "unvote" is registered  by the script.
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

These steps look like, the followin, and as you can see, I have renamed the "lisk-pool" directory into "payout-pool":

```
cp ~/payout-pool/poollogs.json ~/payout-pool/Payments/$(date +%Y%m%d_%H%M%S).PrePayment.poollogs.json
sleep 1
python3 ~/payout-pool/liskpool.py -y -c ~/payout-pool/config.json
sleep 1
python3 ~/payout-pool/cleanpoollogs.py
sleep 1
cp ~/payout-pool/poollogs.json ~/payout-pool/Payments/$(date +%Y%m%d_%H%M%S).PostPayment.poollogs.json
sleep 1
cp ~/payout-pool/payments.sh ~/payout-pool/Payments/$(date +%Y%m%d_%H%M%S).payments.sh
sleep 1
bash ~/payout-pool/payments.sh
```

If you want to use the above, remember to create the Payments directory! In that directory, overtime you will see the history of your payments in this way:
```
20180714_073501.PrePayment.poollogs.json
20180714_073507.PostPayment.poollogs.json
20180714_073511.payments.sh
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

