import requests
import math


def get_data(url):
    headers = { "Referer": "http://192.168.0.1/mainFrame.htm",
                "Cookie":  "Authorization=Basic YWRtaW46YWRtaW4="}
    data = "[LAN_WLAN_ASSOC_DEV#0,0,0,0,0,0#1,1,0,0,0,0]0,4\r\nAssociatedDeviceMACAddress\r\nX_TP_TotalPacketsSent\r\nX_TP_TotalPacketsReceived\r\nX_TP_HostName\r\n"
    raw_data = requests.post(url, headers=headers, data=data).text
    return raw_data


def list_data(url):
    re_addr_str = "(([0-9A-Fa-f]{2}[-:]){5}[0-9A-Fa-f]{2})|(([0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4})"
    re_pkts_str = "([0-9]{3,15})"
    mac_addr = []
    pkts_nos = []
    for addr in re.finditer(re_addr_str, raw_data):
        mac = addr.group(0)
        mac_addr.append(mac)
    for pkts in re.finditer(re_pkts_str, raw_data):
        pkt = pkts.group(0)
        pkts_nos.append(pkt)
    return mac_addr,pkts_nos


def pkt_to_byte(pkt_nos):
    byts = int(pkt_nos / 1480)
    return byts


def convert_size(byts):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(byts, 1024)))
   p = math.pow(1024, i)
   s = round(byts / p, 2)
   return "%s %s" % (s, size_name[i])



