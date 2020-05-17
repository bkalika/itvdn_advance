import hashlib
import base64
import urllib.request
import urllib.parse

operation_name = 'operationName'  # "partnerP2C"
login = 'login'
transaction_id = '1'
application_secret_key = 'applicationSecretKey'
sum_str = transaction_id + login + operation_name

abc = base64.b64encode(hashlib.sha512(sum_str.encode('utf-8')).digest())
print(sum_str, type(sum_str))
print("abc:", abc)
print(type(abc))
abc_str = str(base64.b64encode(hashlib.sha512(sum_str.encode('utf-8')).digest()))


print(type(abc_str))
abc_ask = abc_str + application_secret_key
print("abc_ask:", abc_ask)
abc2 = base64.b64encode(hashlib.sha512(abc_ask.encode('utf-8')).digest())
check = abc + abc2
# print("TLO:", abc)
print("ask2", abc2)
aaa = hashlib.sha512(as_bytestring(abc2).decode('utf-8')).digest()
check2 = str(check)
print("aaa:", aaa)
# print(check)
# print(check2)
abc2 = base64.b64encode(hashlib.sha512(check2.encode('utf-8')).digest())
# print(abc2)

check_str = str(abc) + application_secret_key
sha_signature = hashlib.sha512(check_str.encode()).hexdigest()
sha_signature2 = hashlib.sha512(sha_signature.encode()).hexdigest()

send_url = "https://api-test.lifecell.com.ua/gw/v1/"
login = 'volia'
password = 'ZG46M4I6O0tb8vQc'
alphaname = '<your alphaname>'
msisdn = '380731001805'
message_text = '<Message text>'
# request_template = """<?xml version="1.0" ?>
# <message>
#    <service id="single" source="{}" type="SMS"/>
#    <to>{}</to>
#    <body content-type="text/plain">{}</body>
# </message>""".format(alphaname, msisdn, message_text)
# request = urllib.request.Request(send_url, data=request_template)
# request.add_header("Content-Type", "text/xml")
# # auth_string = base64.b64encode(b'%s:%s' % (login, password))
# log = login+password
# auth_string = base64.b64encode(hashlib.sha512(log.encode('utf-8')).digest())
# request.add_header("Authorization", "Basic %s" % auth_string)
# u = urllib.request.urlopen(request)
# request_result = u.read()
# print(request_template)
# print(request_result)

# import urllib.parse
#
# url = "https://www.customdomain.com"
# d = dict(parameter1="value1", parameter2="value2")
#
# # req = urllib.request.Request(url, data=urllib.parse.urlencode(d))
# # f = urllib.request.urlopen(req)
# # resp = f.read()
#
# data = urllib.parse.urlencode(d).encode("utf-8")
# req = urllib.request.Request(send_url)
# with urllib.request.urlopen(req, data=data) as f:
#     resp = f.read()
#     print(resp)
