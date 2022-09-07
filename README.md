# TreatnTrain_Decode

![image](https://github.com/beardstack/TreatnTrain_Decode/blob/master/signal-2022-09-07-094615_002.jpeg)

Objective:

To be able to use a [YardStick One](https://greatscottgadgets.com/yardstickone/) to control the dispensing of [Treat & Train™ Remote Reward Dog Trainer](https://store.petsafe.net/treat-train-remote-reward-dog-trainer) treats from a Linux machine

I was able to capture those signals using a HackRF One :
* Raw Captures are in 01-04.raw
* nogui_tx[1-4].py replays the captured signals

However there is too much latency in for the replay using the Hackrf and it would be easier and cheaper to use a yardstick one. 

The fcc id of the transmitter is [RF7SI398](https://fccid.io/RF7SI398) and the Freq is 433.92MHZ

TODO:

* [ ] Decode signals to HEX or BIN
* [ ] Create One script /w Params make it compat with RFCat? So it can interface with the Yardstick One
* [ ] Reduce latency
