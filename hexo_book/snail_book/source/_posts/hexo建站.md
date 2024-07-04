title: hexo建站
date: 2024-06-28 14:38:28
tags: hexo
toc: true
categories: [工具]
---

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

* [hexo 操作](#hexo-操作)
  + [创建项目](#创建项目)
  + [启动调试](#启动调试)
  + [创建文章](#创建文章)
    - [markdown必要操作](#markdown必要操作)
      - [设置目录](#设置目录)
      - [插入图片](#插入图片)
  + [设置主题pure](#设置主题pure)
  + [部署推送到github](#部署推送到github)

<!-- /code_chunk_output -->

# hexo 操作

## 创建项目

```shell
hexo init snail_book
cd snail_book
npm install
```

## 启动调试

```shell
hexo clean
hexo g
hexo s
```

## 创建文章

```shell
hexo new 'postName'
hexo n -p 01_pandas/2024-07-04-pandas03
```

### markdown必要操作

#### 设置目录

vscode 安装插件 `Markdown Preview Enhanced`

你可以通过 `cmd/ctrl-shift-p` 然后选择 `Markdown Preview Enhanced: Create Toc` 命令来创建 TOC.

可查阅如下地址:

> https://www.bookstack.cn/read/mpe/zh-cn-toc.md

需要注意: 需要打开预览后, 再进行 `ctrl-s` 保持 md 文件, 才会生成目录在 当前 md 文件中.

#### 插入图片

推荐一种方式, 在 images 下, 根据知识库的 tags 进行目录创建

## 设置主题pure

pure主题就是我当前用的主题, 还可以

## 部署推送到github

```shell
hexo g -d
```
