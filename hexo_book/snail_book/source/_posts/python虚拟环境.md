---
title: python虚拟环境
toc: true
date: 2024-07-08 14:14:22
tags: Python
categories: 编程语言
---

> 平常使用 anaconda 对开发环境做管理, 公司某天发了一条通知, 说 anaconda 未经授权不许使用, 存在 xxx 风险, 限令在一天内进行卸载. 在平常的一些 python 的项目中, anaconda 还是很方便的, 不同的项目管理不同的开发环境, 不过得合乎公司的规定, 所以只能通过其他的方式【命令】创建和管理虚拟环境了. 都是一些基础知识, 时间长没用, 做个记录.

[anaconda](https://www.anaconda.com/download/)

# 使用 virtualenv 管理虚拟环境

由于项目需要, 需要同时具备 py2 和 py3, 所以在创建虚拟环境的时候需要指定 python 解释器

创建虚拟环境

 `virtualenv env27 --python=python2.7`

激活虚拟环境

* windows: `.\env27\Scripts\activate`

退出虚拟环境

* windows: `.\env27\Scripts\deactivate`
