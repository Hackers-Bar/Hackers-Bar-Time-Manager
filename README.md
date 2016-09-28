#Hackers Bar Time Manager

##Using
* Raspberry Pi 2 Model B (Raspbian installed)
* Sony PaSoRi RC-S38
* Python2.7

##Installation
```
sudo pip install libusb1 pyserial nfcpy
git clone https://github.com/Hackers-Bar/Hackers-Bar-Time-Manager.git
cd Hackers-Bar-Time-Manager/src/
```
Then connect PaSoRi to your Raspberry Pi and execute this.
```
sudo python connection_test.py
```
Touch a tag.

**Congrats**
Now you got your tag!

If you got any probrems, [Check here](http://nfcpy.readthedocs.io/en/latest/topics/get-started.html)
