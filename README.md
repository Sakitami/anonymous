# anonymous

> 我曾默默无语地，毫无指望地爱过您。
> 
> ——Александр Сергеевич Пушкин

![](./image/welcome.png)

匿名信，表露心意。那些难以启齿的话，就在这里传达吧。

---

## 功能
- [x] 拥有用户注册与登录系统。
- [x] 使用哈希加密保存用户的密码。
- [x] 使用Markdown语法格式化信件。
- [x] 使用html和css美化信件显示。
- [x] 可以发送信件给以注册过的用户。
- [x] 可以查看已收到的和已发送的信件。
- [x] 可以自行双向删除已发送或已收到的信件。
- [x] 可以查看全部已注册用户的用户列表。
- [ ] 可以定期双向删除已发送的信件。
- [ ] 可以指定信件的送达时间。
- [x] 阅读过的信件将被标记为“已读”，且发件人可以被看到。
- [x] 每个账户可拥有最多三个匿名名片，匿名名片可用在发送信件时，作为指定发件人名称。
- [ ] 可以修改信件样式。
- [ ] *nix系统支持。

---

## 截图

- 状态截图

![状态截图](https://i.loli.net/2021/11/18/vjZUeRQqbBpck3H.png)

- 用户列表(全部用户)

![image.png](https://i.loli.net/2021/11/18/uP93KjZzcUBrbn5.png)

- 我的信件

![image.png](https://i.loli.net/2021/11/18/DviwjlV7TehScR1.png)

- 发送信件

![image.png](https://i.loli.net/2021/11/18/biOvXw8EyBZlpDe.png)

---

## 安装
### 使用源代码
在安装前，确保您的计算机内已经装有Git、Python(>=3.9)环境，且拥有haahlib、pyqt5、pandas、sqlalchemy、markdown库。

- 首先，打开终端，并定位到您所需的目录。
```bash
cd /home/anonymous/anonymous
```
- 使用Git克隆该仓库。
```bash
git clone https://github.com/Sakitami/anonymous.git
```
- 进入目录后，使用编辑器打开mysql.py文件。
```bash
vim mysql.py
```
- 在指定位置修改您的数据库地址、端口号、用户名以及密码。

- 使用Python运行anonymous.py。

---

### 使用安装程序
- 在Releases页面下载安装程序(exe)文件。
- 打开安装程序，在UA界面中，选择“是”。
- 若您使用的是预览版(Demo/Alpha/Beta)，安装时会提示您输入密码。预览版的密码为：
```bash
yesiknowtherisk
```
- 根据安装程序提示，选择安装位置并完成安装。
- 若您安装在C盘Program Files文件夹下，需要将匿名信程序设为“使用管理员权限打开”，否则将遇到无法写入临时文件的错误。
