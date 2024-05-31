# ChatGLM3-6B的本地实现指南

## 模型出处
模型来自于**智谱AI和清华大学KEG实验室**联合发布的对话预训练模型 [https://modelscope.cn/models/ZhipuAI/chatglm3-6b/summary](https://modelscope.cn/models/ZhipuAI/chatglm3-6b/summary)

## 文件解释
* `ZhipuAI`文件夹下为源模型文件，下载自[https://modelscope.cn/models/ZhipuAI/chatglm3-6b/summary](https://modelscope.cn/models/ZhipuAI/chatglm3-6b/summary)
* `main.py`为具体的模型调用代码。
* `web_demo_gradio.py`也能完成模型的调用，而且能在网页进行可视化交互。
* `requirement.txt`列出了本地实现环境的所有包，请根据情况进行筛选。

## 本地电脑配置
* CPU: i9-13900H
* GPU: RTX 4060 8G
* 内存: 16G
