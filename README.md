```
from bs4 import BeautifulSoup
def remove(soup):
    for tag in soup():
        tag.attrs = None
    return soup
doc = '<p class="whatever">junk</p><div style="background: yellow;" id="foo" class="blah">blah</div>'
print(doc)
soup = BeautifulSoup(doc,'html.parser')
remove(soup)
print(soup)
```
# 好记性不如 Markdown

### 压缩文件乱码解压
- Ubuntu 上使用 unar ，自动识别编码
- Arch 使用 unzip-natspec 替代 unzip包，用法同 unzip 一样，unzip xxx.zip

###  为什么 Arch 的更新命令叫做 -Syu

从来很熟悉，但一直都没太搞明白的就是 Arch 包管理 Pacman 更新系统的指令叫做 Pacman -Syu，直到前几天翻译了下 Pacman 的文档，才搞明白.
"-S" 为什么用一个明显不方便的大写字母，之前一直不解, 其实S可以理解为 S模式，等同于 Pacman 其他几个，卸载模式 -R ，查询模式 -Q，单独一个大写的字母
其实没什么用处，需要配合后面参数来共同使用，这点在 Linux 工具链中其实蛮少见的，y 按照文档解释说，是refresh ，从远程刷新包数据，当然，大家都知道的，两个yy代表强制刷新，u就很好理解了，刷新后更新。

### Sogou 输入法在 xmodmap 键映射后失效问题[暂未解决]

经实测，当使用 xmodmap .Xmodmap 重新映射后，会在基于fcitx 框架的sogou输入法多次切换后失效，鉴于失效时间相隔还算长，目前暂时的 hack 方法是在后台开启一个crontab，每隔半小时重新映射一次，虽然不优雅，也只能如此了。

### 云服务器修改欢迎语
```
sudo vim /etc/pam.d/sshd 华为云服务器 动态提示信息 
sudo vim /etc/motd 静态提示信息
PS1 修改 zsh /bash 前缀 echo $PS1 出来按着模板填
```

### gnome 修改一周第一天
```
$sudo vim /usr/share/i18n/locales/chosen_locale
```

```
LC_TIME
[...]
week    7;19971130;5
first_weekday   2
first_workday   2
```

**记得刷新gen然后注销生效**

```
sudo locale-gen
```



### proxychain4 命令行强制走 sock5 代理
```
sudo vim /etc/proxychains.conf
/etc/proxychains.conf 里反注释掉 quiet_mode，然后每次运行只会有两行输出
```
### leanote 不能保存笔记
因为通过 yaourt 安装的默认没有 755 权限，重新chmod 一下就好了 
```
sudo chmod -R 755 /opt/leanote
```
**注意加上 -R 递归**'
### sogou fcitx 全家桶
```
pacman -S fcitx-im fcitx-configtool fcitx-sogoupinyin # yaourt 也可以  pacman 二进制更快
```

### vim 没有 sudo时候强制保存
>此命令是把当前文件（即%）作为stdin传给sudo tee命令来执行。说起来挺绕口，其实就是：用sudo强制保存。
>有时候在自己机器上折腾的时候需要更改一些系统的conf文件，编辑了半天结果发现vim不是以su打开的，无奈只能不保存退出，重新编辑。有这个命令之后能节省不少>误操作带来的事件损耗。
```
:w !sudo tee %
```
**写入zshrc**

### vscode 快捷键配置
```
// 将设置放入此文件中以覆盖默认设置
{
    "python.pythonPath": "/home/huang/.pyenv/shims/python",
    "files.autoSave": "afterDelay",
    "python.formatting.provider": "autopep8",
    "python.linting.flake8Enabled": false,
    "python.linting.pylintEnabled": true,
    "python.linting.pylintArgs": [
        "--disable=C0111"
    ],
    "editor.minimap.enabled": false,
    "workbench.colorTheme": "Atom One Dark",
    "window.zoomLevel": 0,
    "workbench.iconTheme": "vscode-icons"
}
```
### 自动重试  有时间重新把 leanote 库笔记全部挪到 Github
```
import random
from retrying import retry
@retry
def do_something_unreliable():
    if random.randint(0, 10) > 1:
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"
print do_something_unreliable()
```

### soup 语法糖
```
像调用 find_all() 一样调用tag 
find_all() 几乎是Beautiful Soup中最常用的搜索方法,所以我们定义了它的简写方法. BeautifulSoup 对象和 tag 对象可以被当作一个方法来使用,这个方法的执行结果与调用这个对象的 find_all() 方法相同,下面两行代码是等价的:
soup.find_all("a")
soup("a")
这两行代码也是等价的:
soup.title.find_all(text=True)
soup.title(text=True)
```

#### fake-agent 常用 api
```
from fake_useragent import UserAgent
ua = UserAgent()
#ie浏览器的user agent
print(ua.ie)
from fake_useragent import UserAgent
ua = UserAgent()
print(ua.random)
# ex
import requests
from fake_useragent import UserAgent
ua = UserAgent()
headers = {'User-Agent': ua.random}
url = '待爬网页的url'
resp = requests.get(url, headers=headers)
```

### 正则汉字
```
[\u4e00-\u9fa5] 表示汉字
```

#### samba 挂载
```
sudo vim /etc/samba/smb.conf
[homes] 
comment = Home Directories 
browseable = no 
writable = yes 
valid users = huang
path = /
sudo smbpasswd -a username 添加用户
sudo smbpasswd username //修改密码
# 重启 suso systemctl restart nmbd.service
smbd.service 和 nmbd.service
```
**服务名叫 nmbd 和 smbd 不叫 samba.service**

### 垃圾桶 pwd
```
$HOME/.local/share/Trash/files
```
### gunicorn / uwsgi 开启
```
nohup gunicorn blogproject.wsgi:application -b 127.0.0.1:8000 --reload &
```

### pyenv 依赖 zshenv 
```
# 依赖
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils

# 写入
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshenv
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshenv
echo 'eval "$(pyenv init -)"' >> ~/.zshenv
exec $SHELL
```

#### ffmpeg 命令
```
ffmpeg -ss 00:00:00 -t 00:00:30 -i test.mp4 -vcodec copy -acodec copy output.mp4
可以不写 ss 或者 t
-ss 指定从什么时间开始 
-t 指定需要截取多长时间 
-i 指定输入文件 
绝对时间用-to，相对时间用-t:
```
### bash 大小写不敏感
```
echo "set completion-ignore-case on">>~/.inputrc 
```

### 清洗标签
```
from bs4 import BeautifulSoup
def remove(soup):
    for tag in soup():
        tag.attrs = None
    return soup
doc = '<p class="whatever">junk</p><div style="background: yellow;" id="foo" class="blah">blah</div>'
print(doc)
soup = BeautifulSoup(doc,'html.parser')
remove(soup)
print(soup)
```




