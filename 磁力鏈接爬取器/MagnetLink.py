import re
import requests

# 询问用户输入需要读取的网页链接和记事本名称
webpage_url = input("请输入需要读取的网页链接：")
output_filename = input("请输入记事本名称：")

# 获取网页源代码
response = requests.get(webpage_url)
webpage_source_code = response.text

# 使用正则表达式匹配magnet链接
pattern = r'magnet:\?xt=urn:btih:[a-zA-Z0-9]*'
magnet_links = re.findall(pattern, webpage_source_code)

# 将链接写入记事本
with open(output_filename, 'w') as file:
    for link in magnet_links:
        file.write(link + '\n')

print(f"Magnet链接已写入记事本：{output_filename}")
