from com.zcy.api.gateway.sdk import client
from com.zcy.api.gateway.sdk.http import request
from com.zcy.api.gateway.sdk.common import constant

#zcy open server info
host = "121.196.217.18"
port = 9002
url = "/test/category.back.tree"

#init http client
cli = client.DefaultClient(app_key="354232", app_secret="F4Cbc4nnKMJg")

#append param to url
url += "?"
url += "root=0&depth=3"
req_post = request.Request(host=host, port=port, url=url, method="GET", time_out=30000)

#set extra header param
headers = {}
headers[constant.HTTP_HEADER_ACCEPT] = "application/json"
req_post.set_headers(headers)

req_post.set_content_type(constant.CONTENT_TYPE_FORM)

#get response and show
print cli.execute(req_post)
