import requests

def myRequest(url,method,request_data,headers):
    #1、判断是get还是post请求
    # 2、调用request相应的方法.url,请求数据
    # 3、获取返回值
    #判断数据是否为空，不为空则转换成字典类型的数据
    if request_data is not None:
        request_data = eval(request_data)
    if headers is not None:
        cookies = eval(headers)
    if method == "get":
        res = requests.get(url,request_data)
    elif method == "post":
        res = requests.post(method = method, url = url, data = request_data, headers = headers)

    else:
        res = None
    return res

# r = requests.get(base_url+"/cookies",cookies=cookie)