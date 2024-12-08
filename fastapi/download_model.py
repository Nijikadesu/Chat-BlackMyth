from modelscope import snapshot_download
import os


# FastAPI部署部分参考自 DataWhale 开源项目 -> self-llm: 开源大模型食用指南
# 项目链接：https://github.com/datawhalechina/self-llm/tree/master
if not os.path.exists('./model'):
    os.makedirs('./model')


# internlm-chat-7b
model_dir_1 = snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='./model', revision='master')
# bce-embedding-base_v1
model_dir_2 = snapshot_download('maidalun/bce-embedding-base_v1', cache_dir='./model', revision='master')
