# TreatnTrain_Decode

![image](https://github.com/beardstack/TreatnTrain_Decode/blob/master/signal-2022-09-07-094615_002.jpeg)

Objective:

To be able to use low cost transceivers e.g [YardStick One](https://greatscottgadgets.com/yardstickone/) or 
[EvilCrowRF](https://github.com/joelsernamoreno/EvilCrowRF-V2/) to control the dispensing of [Treat & Train™ Remote Reward Dog Trainer](https://store.petsafe.net/treat-train-remote-reward-dog-trainer) treats from a Linux machine or microcontroller

The devices are designed to have toggle switches to determine what "channel" they respond to denoted 1-4 on the remote and dispenser, I was able to capture those signals using a HackRF One :
* Raw Captures are in 01-04.raw
* nogui_tx[1-4].py replays the captured signals

However there is too much latency in the replay using the Hackrf and it would be easier and cheaper to use CC1101 modules.. 

The fcc id of the transmitter is [RF7SI398](https://fccid.io/RF7SI398) and the Freq is 433.92MHZ, the treat dispenser and the remote both have toggle switches for channels 1-4. There is no rolling codes but the modulation is currently unknown

TODO:

* [ ] Decode signals to HEX or BIN
* [ ] Create One script /w Params make it compat with RFCat? So it can interface with the Yardstick One
* [ ] Reduce latency
