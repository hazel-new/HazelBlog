# 需要的基础背景知识

1. GitHub基本了解
2. git基础知识
3. markdown/html/css等web开发基础知识
4. Jekyll基础知识

# 环境准备

1. Github网页端：
   * 申请好GitHub账号，基本用户配置
   * 基本repo配置
2. 本地环境：
   * 本地 git 环境
   * git clone 想要的github上repo 【https/ssh模式要想好】
   * 安装Ruby & gem 【新版本ruby自动安装gem】
   * 利用gem 安装Jekyll
   * 下载喜欢的Jekyll blog模板 
   * 模板所在文件夹下，cmd命令行运行jekyll server
   * 选择自己习惯的编辑器/浏览器，主要文件格式是markdown跟html
   * 改模板对应文件，生成自己喜欢的模式，利用Jekyll 本地预览
   * git push到GitHub，网页端浏览
    
# 问题解决小结

1. https模式clone安全一些，但会导致每次push都要输入用户名密码，ssh模式方便一些。
    * 根据GitHub官方文档，将远程 URL 从 HTTPS 切换到 SSH
    * 根据GitHub官方文档，设置ssh key
2. pycharm上显示中文正常，到浏览器上变成乱码？
    * 火狐浏览器，右侧设置下面，more->Text Encoding(字符编码)->改成uniode
3. 主页背景图不显示?
    * 修改_sass下面_layout.scss，改background参数
4. md文件里面图片不显示?
    * 网站blog要写成绝对路径，不过相对路径在pycharm里可以预览
    * "\!\[book\]\(\{{ site.url }}/路径/图片文件)" ，这种写法需要把_config.yml里面的url参数提前定义




