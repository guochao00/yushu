# 余数计算器应用

这是一个使用Kivy框架开发的Android应用，包含两个主要功能：
1. 除法计算器：计算两个整数的商和余数
2. 六十四卦名速见表：显示易经中的64卦及其编号和名称

## 文件结构

- `main.py` - 应用程序主代码
- `buildozer.spec` - Buildozer配置文件，用于构建APK
- `assets/` - 资源文件目录
  - `64卦名.jpeg` - 六十四卦名速见表图片

## 本地运行

要在本地Python环境中运行应用程序：

```bash
# 安装依赖
pip install kivy pillow

# 运行应用
python main.py
```

## 构建APK

要构建APK文件，您需要使用Buildozer工具：

### 在Linux上构建

1. 安装必要的依赖：

```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip build-essential git python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
sudo apt-get install -y libgstreamer1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good
sudo apt-get install -y openjdk-11-jdk autoconf automake libtool libffi-dev libssl-dev
sudo apt-get install -y cython patch make
```

2. 安装Buildozer：

```bash
pip3 install --user buildozer
```

3. 构建APK：

```bash
cd 余数计算器应用目录
buildozer android debug
```

构建完成后，APK文件将位于`bin/`目录中。

### 在Windows上构建

在Windows上，建议使用WSL(Windows Subsystem for Linux)或虚拟机运行Ubuntu，然后按照上述Linux构建步骤操作。

## 应用功能

### 除法计算器
- 输入被除数和除数
- 点击"计算"按钮获取商和余数
- 错误处理：除数为零或非整数输入

### 六十四卦名速见表
- 点击"查看六十四卦名速见表"按钮查看图表
- 点击"返回计算器"按钮返回计算功能

## 故障排除

如果构建过程中遇到问题：

1. 确保所有依赖都已正确安装
2. 尝试清理构建缓存：`rm -rf .buildozer`
3. 检查buildozer.spec文件中的配置是否正确
4. 查看详细日志：`buildozer -v android debug`
