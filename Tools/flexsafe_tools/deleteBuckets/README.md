# 功能
- 快速删除亚马逊&阿里云的bucket

# 注意!
- 删除阿里云上的bucket时，会清空所有bucket，请谨慎操作！
- 亚马逊上有非测试bucket，为防止删除生产数据，仅提供根据bucket名称进行批量删除，需将bucket名称
放在`aws_buckets.txt`文件
- 利用`Xpath`可快速获取网页上待删除bucket名称（浏览器安装XpathHelp类似插件）
- Xpath：`//a[contains(text(),"cloudfort-backup")]`
![avatar](https://i.ibb.co/rbZZfgc/get-Bucke-Name-By-Xpath.png)

# 使用
- Python 3环境执行 `pip install -r requirements.txt`安装依赖库


- 执行`python deleteBuckets.py`


