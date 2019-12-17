import calendar
import math
import re
import requests
import time


def get_data():
    eptime = round(time.time() * 1000)
    headers = {
            "Host": "192.168.0.1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Content-Type": "text/plain",
            "Cookie": "Authorization=Basic YWRtaW46YWRtaW4=",
            }
    headers["Referer"] = "http://192.168.0.1/main/wlStats.htm?_={}".format(eptime)
    req = requests.get("http://192.168.0.1/main/wlStats.htm", headers=headers, params={"_": "{}".format(eptime)})
    headers["Referer"] = "http://192.168.0.1/cgi?5&1"
    post_data1 = requests.post("http://192.168.0.1/cgi?5&1", headers=headers, data="[LAN_WLAN#0,0,0,0,0,0#0,0,0,0,0,0]0,2\r\nname\r\nSSID\r\n[SYS_MODE#0,0,0,0,0,0#0,0,0,0,0,0]1,1\r\nmode\r\n")
    headers["Referer"] = "http://192.168.0.1/cgi?6&1"
    post_data2 = requests.post("http://192.168.0.1/cgi?6&1", headers=headers, data="[LAN_WLAN_MSSIDENTRY#0,0,0,0,0,0#1,1,0,0,0,0]0,2\r\nName\r\nSSID\r\n[LAN_WLAN_GUESTNET#1,1,0,0,0,0#0,0,0,0,0,0]1,1\r\nName\r\n")
    pst_url = "http://192.168.0.1/cgi?7"
    headers["Referer"] = "http://192.168.0.1/cgi?7"
    post_data3 = requests.post("http://192.168.0.1/cgi?7", headers=headers, data="[ACT_WLAN_UPDATE_ASSOC#1,1,0,0,0,0#0,0,0,0,0,0]0,0\r\n")
    headers["Referer"] = "http://192.168.0.1/cgi?6"
    raw_data = requests.post("http://192.168.0.1/cgi?6", headers=headers, data="[LAN_WLAN_ASSOC_DEV#0,0,0,0,0,0#1,1,0,0,0,0]0,4\r\nAssociatedDeviceMACAddress\r\nX_TP_TotalPacketsSent\r\nX_TP_TotalPacketsReceived\r\nX_TP_HostName\r\n").text
    return raw_data


def list_data(raw_data):
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
    return mac_addr, pkts_nos


def convert_pkt(pkts_nos):
    pkts_nos = int(pkts_nos)
    byts = int(pkts_nos * 1480)
    if byts == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB")
    i = int(math.floor(math.log(byts, 1024)))
    p = math.pow(1024, i)
    s = round(byts / p, 2)
    return "%s %s" % (s, size_name[i])


