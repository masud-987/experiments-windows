import urllib3

def fetch_url(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response

if __name__ == "__main__":
    url = "http://httpbin.org/get"
    response = fetch_url(url)
    print(response.status)
    print(response.data)