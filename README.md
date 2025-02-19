# 西南交大图书馆抢座系统

本项目 fork from [Ctrl-T/SWJTU-LibSeatGetter: 西南交大图书馆抢座系统](https://github.com/Ctrl-T/SWJTU-LibSeatGetter)

## 编写原因
每到期末考试季，图书馆都是一座难求，从早晨就开始夸张的0剩余座位状态。但实际上人员进进出出，总是有偶尔出现一两个空缺座位的时候，本系统即着眼于此，实现自动蹲守，发现空位立即抢座。
> 作者也知道这其实没有解决根本问题😓，不过是加剧了内卷。。但目前情况下，只好大家都来卷吧

## 实现原理
### 用户管理
用`tmp_users`，`waiting_users`，`running_users`，`success_users`，`fail_users`分别储存登录但未开始抢座的用户，正在等待抢座的用户，正在抢座的用户，成功的用户，失败的用户，一个用户从登录到抢座成功的过程就是在不同的类别间转换的过程。
### 抢座过程
用户登录后进入`tmp_users`，点击抢座后进入`waiting_users`，抢座线程不断查看`waiting_users`，一旦出现用户即将其塞进`running_users`，并开始遍历座位为其抢座，抢座成功进入`success_users`，反之进入`fail_users`。
### 状态保持
用户在进行座位预约时需保持登录或重新登录，考虑到操作cookie太过繁琐，所以干脆使用requests库的session功能对用户的登录状态进行记录，故`tmp_users`，`waiting_users`使用字典数据结构，键为用户id，值为session。

## 说明
- 在 `config.py` 中的 `ROTATION_TIME` 中定义抢座轮询间隔时间
- 排除了2楼考研自习室
- 未使用任何方式在后台对用户数据进行储存
- 特别感谢[@卖女孩的小火柴](https://www.shinenet.cn)在软件编写过程中提供的帮助
- 本软件仅供学习交流