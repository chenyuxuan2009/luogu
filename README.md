本项目所有爬虫均没有违反 [https://www.luogu.com.cn/robots.txt](https://www.luogu.com.cn/robots.txt) 的内容。

# 使用说明

请不要擅自更改 main.py 的任何内容。

在 cookies.txt 中，分别输入你的 `_uid` 和 `__client_id`。具体可以使用搜索引擎搜索「如何获得 cookies」。

## 卷王监视器

**卷王监视器使用原理是爬取指定用户前后提交于通过差，并没有实时访问 /record，没有违反 robots.txt。**

进入 /monitor/monitorList.txt，输入你需要监视的用户的用户编号，第一行放你对被监视用户的昵称，第二行开始是被监视用户的用户编号集合，用**逗号** `,` 隔开。具体可见本仓库的 /monitor/monitorList.txt。

找到 monitor.py 运行。