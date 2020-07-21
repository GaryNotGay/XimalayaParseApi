import base64
import hashlib
import random
import json
import time
import requests

def getLen(length):
    i = ''
    h = int(length / 3600)
    if not h == 0:
        i += str(h)
        i += 'h'
    length %= 3600
    m = int(length / 60)
    if not m == 0:
        i += str(m)
        i += 'm'
    length %= 60
    if not length == 0:
        i += str(length)
        i += 's'
    return i

def getTime():
    url = 'https://www.ximalaya.com/revision/time'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Safari/537.36'}
    response = requests.get(url = url, headers = headers)
    result = response.content.decode('utf-8')
    return result

def getSign():
    nowtime = str(int(time.time() * 1000))
    servertime = getTime()
    sign = str(hashlib.md5("himalaya-{}".format(servertime).encode()).hexdigest()) + "({})".format(str(round(random.random() * 100))) + servertime + "({})".format(str(round(random.random() * 100))) + nowtime
    return sign

def cg_hun(seed):
    cgStr = ''
    t = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/\\:._-1234567890'
    for index in range(len(t)):
        r = ran(seed) * len(t)
        o = int(r)
        cgStr += t[o]
        tArr = t.split(t[o])
        t = ''.join(tArr)
        seed = (211 * int(seed) + 30031) % 65536
    return cgStr

def ran(seed):
     seed = (211 * int(seed) + 30031) % 65536
     return seed / 65536

def cg_fun(fileID, cgStr):
    fileIDArr = fileID.split('*')
    str = ''
    for index in range(len(fileIDArr)-1):
        str += cgStr[int(fileIDArr[index])]
    return str

def vt(t, e):
    r = []
    o = 0
    i = ''
    for index in range(256):
        r.append(index)
    for index in range(256):
        o = (o + r[index] + ord(t[index%len(t)])) % 256
        n = r[index]
        r[index] = r[o]
        r[o] = n
    o = 0
    a = 0
    for index in range(len(e)):
        a = (a + 1) % 256
        o = (o + r[a]) % 256
        n = r[a]
        r[a] = r[o]
        r[o] = n
        i += chr(ord(e[index]) ^ r[(r[a] + r[o]) % 256])
    return i

def wt_tmp1(t, e):
    n = []
    for index in range(len(t)):
        if ord('a') <= ord(t[index]) and ord('z') >= ord(t[index]):
            o = ord(t[index]) - 97
        else:
            o = ord(t[index]) - 48 + 26

        for temp in range(36):
            if e[temp] == o:
                o = temp
                break

        if 25 < o:
            n.append(chr(o - 26 + 48))
        else:
            n.append(chr(o + 97))
    return ''.join(n)

def wt_tmp2(t):
    if not t:
        return ''
    a = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1]
    r = 0
    i = ''
    o = len(t)

    while r < o:
        e = a[255 & ord(t[r])]
        r += 1
        while r < o and -1 == e:
            e = a[255 & ord(t[r])]
            r += 1
        else:
            if -1 == e:
                break

        n = a[255 & ord(t[r])]
        r += 1
        while r < o and -1 == n:
            n = a[255 & ord(t[r])]
            r += 1
        else:
            if -1 == n:
                break

        i += chr(((e << 2) & 255 ) | (48 & n) >> 4)

        if 61 == (255 & ord(t[r])):
            return i
        e = a[255 & ord(t[r])]
        r += 1
        while r < o and -1 == e:
            if 61 == (255 & ord(t[r])):
                return i
            e = a[255 & ord(t[r])]
            r += 1
        else:
            if -1 == e:
                break

        i += chr((((15 & n) << 4) & 255) | (60 & e) >> 2)

        if 61 == (255 & ord(t[r])):
            return i
        n = a[255 & ord(t[r])]
        r += 1
        while r < o and -1 == n:
            if 61 == (255 & ord(t[r])):
                return i
            n = a[255 & ord(t[r])]
            r += 1
        else:
            if -1 == n:
                break

        i += chr((((3 & e) << 6) & 255) | n)
    return i

def wt(t, gt, bt):
    param1 = wt_tmp1("d" + gt + "9", bt)
    param2 = wt_tmp2(t)
    n = vt(param1, param2).split('-')
    return n

def getTrack(albumId):
    res = []
    url = 'https://www.ximalaya.com/revision/album?albumId=' + str(albumId)
    cookies = {'1&_token': 'Your Cookies',}
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Safari/537.36','xm-sign': '', }
    headers['xm-sign'] = getSign()
    response = requests.get(url = url, cookies = cookies, headers = headers)
    result = response.content.decode('utf-8')
    resultJson = json.loads(result)
    TrackName = resultJson['data']['mainInfo']['albumTitle']
    TrackNum = resultJson['data']['tracksInfo']['trackTotalCount']
    for index in range(TrackNum):
        res.append(resultJson['data']['tracksInfo']['tracks'][index]['trackId'])
    return TrackName, res

def getDownUrl(Mp3ID):
    timestamp = getTime()
    BasicInfoUrl = 'https://mpay.ximalaya.com/mobile/track/pay/' + str(Mp3ID) + '/' + str(timestamp) + '?device=pc&isBackend=true'
    cookies = {'1&_token': 'Your Cookies',}    
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Safari/537.36', 'xm-sign': '',}
    headers['xm-sign'] = getSign()
    response = requests.get(url = BasicInfoUrl, cookies = cookies, headers = headers)
    result = response.content.decode('utf-8')
    resultJson = json.loads(result)
    title = resultJson['title']
    downDomain = resultJson['domain']
    apiVersion = resultJson['apiVersion']
    buyKey = resultJson['buyKey']
    length = resultJson['duration']
    seed = resultJson['seed']
    fileID = resultJson['fileId']
    ep = resultJson['ep']
    cgStr = cg_hun(seed)
    n = cg_fun(fileID, cgStr)
    if n[0] == '/':
        address = n
    else:
        address = '/' + n
    gt = vt("xm", "Ä[ÜJ=Û3Áf÷N")
    #gt = "g3utf1k6yxdwi0"
    bt = [19, 1, 4, 7, 30, 14, 28, 8, 24, 17, 6, 35, 34, 16, 9, 10, 13, 22, 32, 29, 31, 21, 18, 3, 2, 23, 25, 27, 11, 20, 5, 15, 12, 0, 33, 26]
    params = wt(ep, gt, bt)
    sign = params[1]
    token = params[2]
    timestamp = params[3]
    downurl = downDomain + '/download/' + apiVersion + address +'?sign=' + sign + '&buy_key=' + buyKey + '&token=' + str(token) + '&timestamp=' + timestamp + '&duration=' + str(length)
    filename = title + '-' + getLen(length)
    return filename, downurl

param = 'albumId+39488639'
#param = 'trackId+232373974'
badJson = {'Params Error!': 'Standard Format is \'albumId+NUM / trackId+NUM\' (https://www.ximalaya.com/Catagory/albumId/trackId) '}
isAlbum = False
isTrack = False
albumId = 0
trackId = 0
paramArr = param.split('+')

if paramArr[0] == 'albumId':
    isAlbum = True
    albumId = paramArr[1]
elif paramArr[0] == 'trackId':
    isTrack = True
    trackId = paramArr[1]
else:
    print(badJson)

if isAlbum:
    out = {}
    res = {}
    Track = getTrack(albumId)
    TrackNum = len(Track[1])
    for index in range(TrackNum):
        ReturnResult = getDownUrl(Track[1][index])
        filename = str(index + 1) + '/' + str(TrackNum) + '-' + ReturnResult[0]
        downurl = ReturnResult[1]
        res[filename] = downurl
    out['name'] = Track[0]
    out['res'] = res
    print(out)

if isTrack:
    out = {}
    ReturnResult = getDownUrl(trackId)
    filename = ReturnResult[0]
    downurl = ReturnResult[1]
    out['name'] = filename
    out['url'] = downurl
    print(out)

print(badJson)
