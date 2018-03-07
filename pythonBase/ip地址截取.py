ip = "192.168.1.123"
address = ip.split(".")[-1]     #ip最后一位
print(address)

list_ip = ip.split(".")
print(list_ip)
ip_new = ".".join(list_ip)              #将列表转换为ip，join的用法
print(ip_new)