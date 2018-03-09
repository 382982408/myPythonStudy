# -*- coding: utf-8 -*-


设置debug可以不用每次在修改代码之后重新运行，其设置debug有两种方式：

1. app.run(debug = True)
2. 写入配置文件，再导入，（许多其他的参数都放置到配置文件中，比如数据库相关的SECRET_KEY和SQLALCHEMY，用类似的方法导入）。