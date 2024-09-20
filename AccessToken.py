from poseidon import poseidon

appkey = 'af5cf8bd-cc04-4e35-abdf-8229d07a36cd'
appsecret = '8817e5e7-35c4-4252-be24-9cf64668d7be'

url = 'https://apim-ppe1.envisioniot.com/apim-token-service/v2.0/token/get'
header = {}
data = {
    "appKey": appkey,
    "encryption": "60da64210c20d1f100d3ebc6e05d53f9ba76ed7a6c684a60ef0f2740d55b0b5c" ,
    "timestamp": 1726833700531
}

req = poseidon.urlopen(appkey, appsecret, url, data,header,'POST')
print(req)