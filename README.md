# wordcloud功能介绍
**1.提取txt\word文本，jieba分词后生成词云图**
**2.登陆微信并抓取微信所有好友签名生成词云图**
![image](https://github.com/ivanwhaf/wordcloud/blob/master/Resources/wd.png)
# 使用教程
1.电脑安装python环境
2.pip安装jieba、itchat、wordcloud、numpy、PIL、matplotlib、re 库.
3.运行根目录下word.py程序


# 注意事项
* 可根据个人需要将文本导入根目录下text.txt文件并自定义生成词云
* 要生成微信好友签名词云时,记事本打开word.py文件最后将如下代码注释
'''
text=get_file_text()
'''

并将
'''
text=get_wechat_sigature_text()
'''
代码取消注释重新运行程序即可



