# wordcloud功能介绍
* 提取txt\word文本，jieba分词后生成词云图
* 登陆微信并抓取微信所有好友签名生成词云图
<br>

![image](https://github.com/ivanwhaf/wordcloud/blob/master/Resources/wd.png)
# 使用教程
1.电脑安装python环境<br>
2.pip安装jieba、itchat、wordcloud、numpy、PIL、matplotlib、re 库<br>
3.运行根目录下word.py程序<br>


# 注意事项
* 可根据个人需要，将文本导入根目录下text.txt文件并自定义生成词云
* 可将3.jpg词云模型图片换成自定义图片
* 要生成微信好友签名词云时,记事本打开word.py文件，将底部如下代码注释
```
text=get_file_text()
```

并将上一行
```
text=get_wechat_sigature_text()
```
代码取消注释重新运行程序即可



