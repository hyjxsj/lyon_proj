#!/bin/bash
# Date: 2020-8-10
# Auth: Lukas
# Mail: yangyang.huang@cloudfortdata.com
# Func: This is a template for script
# Ver.: 1.0

docker load < shadowsocks.tgz
mkdir -p /etc/shadowsocks-r
cat > /etc/shadowsocks-r/config.json << EOF
{
    "server":"0.0.0.0",
    "server_ipv6":"::",
    "server_port":9000,
    "local_address":"127.0.0.1",
    "local_port":1080,
    "password":"password0",
    "timeout":120,
    "method":"aes-256-cfb",
    "protocol":"origin",
    "protocol_param":"",
    "obfs":"plain",
    "obfs_param":"",
    "redirect":"",
    "dns_ipv6":false,
    "fast_open":true,
    "workers":1
}
EOF

#start shadowsocks service
docker run -d -p 9000:9000 -p 9000:9000/udp --name ssr --restart=always -v /etc/shadowsocks-r:/etc/shadowsocks-r teddysun/shadowsocks-r