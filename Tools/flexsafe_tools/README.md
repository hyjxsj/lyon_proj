# flexsafe_tools

flexsafe_tools使用请求接口方式完成对Flexsafe的一些常用的操作，减少一些重复性劳动，让你每天快乐多一些。。。

# 快速开始
使用普通用户`cfservice`连接SSH连接服务器`172.16.71.180`,键入`toolist`命令查看所有可用命令。键入对应命令，即可使用。


![toolist](http://git.cloudfort.ml:2333/root/flexsafe_tools/raw/master/toolist.png?inline=false "toolist")

## 工具清单

- autoLicense - - - - 自动上传license及配置文件
- autoConfig  - - - - 配置邮箱服务器、开启加锁、配置备份服务器（AWS、ACE、本地都已支持）
- addFlexsafeUser - - - - 批量新增用户、修改密码、模拟登陆
- generateDir - - - - 创建各种权限的共享、存档目录，并在其目录内上传测试文件
- deleteBuckets  - - - - 批量删除阿里云&亚马逊Buckets
- syncTime  - - - - 自动同步系统时间
- createAuthorization - - - - 批量生成用户Authorization
- emptyFlexsafe - - - - 接口方式还原FlexSafe(不建议使用)
- rollBack - - - - 操作数据库方式还原FlexSafe（不建议使用）
> 使用`deleteBuckets`前，请仔细确认！！！



### 开发环境

- Python3.5
- `pip install -r require.txt`
- 每个工具对应各目录下`run.py`文件