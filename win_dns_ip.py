import platform
import socket
import subprocess

output = subprocess.check_output(["ipconfig", "-displaydns"])
ipconfig_all_list = output.split("")
dns_ips = []
for i in range(0, len(ipconfig_all_list)):
    if "DNS Servers" in ipconfig_all_list[i]:
        first_ip = ipconfig_all_list[i].split(":")[1].strip()
        #if not is_valid_ipv4_address(first_ip):
            continue
        dns_ips.append(first_ip)
        k = i+1
        while k < len(ipconfig_all_list) and ":" not in ipconfig_all_list[k]:
            ip = ipconfig_all_list[k].strip()
            if is_valid_ipv4_address(ip):
                dns_ips.append(ip)
            k += 1
        break
print(dns_ips)

