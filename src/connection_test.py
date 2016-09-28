# -*- coding: utf-8 -*-
import nfc

def connected(tag):
    print tag
    return True

def main():
    clf = nfc.ContactlessFrontend('usb:054c:06c3')
    conn = False
    while not conn:
        conn = clf.connect(rdwr={'on-connect': connected})

if __name__ == '__main__':
    print "Now touch your tag!"
    main()
