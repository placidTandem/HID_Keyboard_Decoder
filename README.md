# HID_Keyboard_Decoder
This is used to decode HID Keyboard commands that have been intercepted in a packet analyzer

To use this tool requires you to extract the key data first from a packet analyzer tool.

This can be done by first capturing the traffic using WireShark on the USB interface. Then narrowing the results to usb.src == "1.9.2"&& !(usb.capdata == 00:00:00:00:00:00:00:00)&&(usb.transfer_type == 0x01) where the source is the correct one for the keyboard.

Take this data into the Kali command line and run the following commands:

```
tshark -r <file>.pcap -T fields -e usb.capdata > keystrokes.txt
cat keystrokes.txt |awk 'NF' >pipe; cat pipe >keystrokes.txt
```
  
The keyboard conversion information can be found at https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf and this script was based on the information provided by:
https://ctf-wiki.github.io/ctf-wiki/misc/traffic/protocols/USB/
https://osqa-ask.wireshark.org/questions/53919/how-can-i-precisely-specify-a-usb-device-to-capture-with-tshark
https://medium.com/@ali.bawazeeer/kaizen-ctf-2018-reverse-engineer-usb-keystrok-from-pcap-file-2412351679f4

In the future I will had a function to do the conversion from the pcap.
