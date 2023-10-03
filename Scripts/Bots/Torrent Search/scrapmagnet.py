import urllib.parse
import urllib.request

trackers = [
    "udp://tracker.coppersurfer.tk:6969/announce",
    "udp://9.rarbg.to:2920/announce",
    "udp://tracker.opentrackr.org:1337",
    "udp://tracker.internetwarriors.net:1337/announce",
    "udp://tracker.leechers-paradise.org:6969/announce",
    "udp://tracker.coppersurfer.tk:6969/announce",
    "udp://tracker.pirateparty.gr:6969/announce",
    "udp://tracker.cyberia.is:6969/announce",
]


def scrapmag(torrenthash, torrentname):
    prefix = "magnet:?xt=urn:btih:"
    dn = "dn=" + urllib.parse.quote(torrentname, safe="")
    tr = ["tr=" + urllib.parse.quote(t, safe="") for t in trackers]
    tr = "&".join(tr)
    return prefix + torrenthash + "&" + dn + "&" + tr
