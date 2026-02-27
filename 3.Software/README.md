# 项目说明

## 项目名称
嵌入式软件项目框架

## 项目简介
本项目是一个基于 ARM Cortex-M4 内核的嵌入式软件项目框架，包含完整的目录结构和基础文件。

## 目录结构
```
Software/
├── Makefile              # 构建脚本
├── README.md             # 项目说明、编译方法、版本
├── .gitignore            # 忽略编译产物、配置文件
│
├── src/                  # 自己写的业务代码
│   ├── main.c            # 入口
│   ├── app/              # 应用层逻辑
│   ├── drivers/          # 板级驱动（自己封装）
│   ├── modules/          # 功能模块
│   └── utils/            # 工具函数
│
├── bsp/                  # 板级支持包
│   ├── cmsis/            # CMSIS 库
│   ├── hal/              # HAL 库
│   ├── startup/          # 启动文件
│   └── board/            # 板级初始化
│
├── include/              # 统一头文件路径
│
├── config/               # 配置文件
│
├── lib/                  # 第三方库
│
├── bootloader/           # Bootloader 代码
│
├── scripts/              # 脚本
│
├── build/                # 编译产物
│
└── output/               # 最终 hex/bin/elf
```

## 编译方法

### 环境要求
- ARM 交叉编译器：arm-none-eabi-gcc
- Make 工具
- Python（用于烧录脚本）

### 编译步骤
1. 进入项目目录：`cd Software`
2. 执行编译：`make all`
3. 烧录固件：`make flash`

## 版本信息

### 版本历史
- v1.0.0 (2026-02-26)：初始版本，创建项目框架

### 依赖库
- FreeRTOS：实时操作系统
- lwGPS：GPS 解析库
- LittleFS：小型文件系统
