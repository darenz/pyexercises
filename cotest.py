import asyncio

async def hello(n):
    print("hello %d"%n)
    await asyncio.sleep(1)
    print("hello %d again"%n)

tasks = [hello(n) for n in range(5)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
#loop.close()

async def wget(url):
    connect = asyncio.open_connection(url,80)
    reader,writer = await connect
    header = "GET / HTTP/1.1\r\nHost: %s\r\n\r\n"%url
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break;
        print("{}'s header > {}".format(url,line.decode('utf-8').rstrip()))
    writer.close()
    return 


urls = ["www.baidu.com","www.sina.cn","www.qq.com"]
tasks2 = [wget(url) for url in urls]
print(type(tasks2[0]))
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks2))
loop.close()
