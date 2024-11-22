# 青龙面板脚本

<h4>用于储存本人制作的脚本</h4>



为了减轻搭建的压力、本人制作了一个专门用于处理的服务器
有需要可以使用本人提供的服务器
<h3>[个人服务器](https://ks.0tttt.com/)</h3>



* 源码没有加密 也没必要加密
* 实际运行环境可以在任意环境
* 如果不嫌麻烦可以考虑使用 [serv00](https://www.serv00.com/) 免费服务器

<p>如有时间我会增加更多的脚本，如果有想做的脚本也可以联系我</p>


不要直接拉取我的仓库，否则你会很惨。

## 新补充的使用环境变量来适配
|脚本|平台|工具名字|
|--|--|--|
|kuaishou.py|KS_COOKIE|快手|
|kuaishou_jisu.py|KSJSB_COOKIE|快手极速版|

* 因为快手平台针对数据的加密调整几项内容
* 快手极速版已经调整完毕，每个操作都包含一个 sig3 或者 sig4的加密验证
* 此值主要用作判断提交的数据是否属于客户端发起的验证
* 一般情况下只要重复提交内容，此值可以不变
* 也就是意味着，此值每个操作都需要单独设置
* 也同样意味着，此值可以长期持有进行提交

|脚本|平台|工具名字|
|--|--|--|
|kuaishou.py|KS_COOKIE|快手|
|kuaishou_jisu.py|KSJSB_COOKIE|快手极速版|



## 相关抓取连接地址
* 得到sig3 或者 sig4 后替换脚本尾部相同的值

|操作|特征地址|
|--|--|
|宝箱|https://nebula.kuaishou.com/rest/wd/encourage/unionTask/treasureBox/report|
|饭补|https://encourage.kuaishou.com/rest/wd/encourage/unionTask/dish/report|
|步数换金币（失效了）|https://encourage.kuaishou.com/rest/wd/encourage/unionTask/walking/detail|
|签到|https://nebula.kuaishou.com/rest/wd/encourage/unionTask/signIn/report|

``` python
def main():
    _cookie = "你的cookie" 
    get_baoxiang(_cookie, "宝箱sig")
    get_fanbu(_cookie, "饭补sig")
    get_walk(_cookie, "走路换金币sig") #失效了
    get_qiandao(_cookie, "签到sig")
    get_money(_cookie)
    
if __name__ == '__main__':
    main()
```


<h6>个人制作 并不能保证完美运行
有需要调整请联系我 Tou_taozi 
</h6>

###### [电报 @I_love_xxt](https://t.me/I_love_xxt)





