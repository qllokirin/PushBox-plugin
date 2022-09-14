# PushBox-plugin

v3云崽插件

### **原游戏名：Helltaker**

---

# python环境

> 无版本限制 能安装OpenCV即可

* 1.安装

  * **win用户**

    我放个python3.7.3的链接

    > https://wwp.lanzoub.com/ioagG0a3xufc
  > 密码:atri
  
    这里借一张网图说明一下图中的√**一定要勾上**

    ![image](https://docimg2.docs.qq.com/image/bQeXgYp4QL88YoxSB-vgug.png?w=738&h=450)

* 2.**检查python**！！！！！！(**非常重要**)

  输入`python -V`和`pip -V`

  **如果是3.7**的话输出应该是`Python 3.7.3`和`xxxxx (python 3.7)`

* 3.升级pip

  ```
  python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple/
  ```
  
* 4.安装OpenCV

  ```
  pip3 install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
  pip3 install opencv-contrib-python -i https://pypi.tuna.tsinghua.edu.cn/simple
  ```

  检查OpenCV是否安装成功

  ```
  python
  import cv2
  ```

  无报错即时安装成功

# 安装插件

* 1.克隆代码

```
git clone https://gitee.com/magical_modoka/PushBox-plugin.git ./plugins/PushBox-plugin/
```

# 功能说明

发送**开始推箱子1**则可开始第一关

发送**上下左右**可移动

> 已知问题：
>
> 不能多开
>
> 开一个游戏会串群且可以一起玩
>
> 地图有待增加 目前只有原游戏第一关

# 免责声明

1. 功能仅限内部交流与小范围使用，勿将Yunzai-Bot及PushBox-plugin用于以盈利为目的的场景
3. 图片与其他素材均来自于网络，仅供交流学习使用，如有侵权请联系，会立即删除

# 如有问题

可以在自行百度or提出issue或查找相关issue

喜欢的话就点个star吧
