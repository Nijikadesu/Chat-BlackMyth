## 基于 GraphRAG 打造黑神话：悟空聊天机器人

### 计划
- STEP 1： 完成黑神话悟空数据集的收集 （影神图，人物对话，关卡内容等）
- STEP 2： 根据数据集构建 GraphRAG（包含文本分段，向量化，持久化部署，相似度计算等功能）
- STEP 3： 接入本地语言模型（预计 Qwen2-7B），构造 prompt template，完成一次成功对话
- STEP 4： 基于 gradio 框架，完成前端对话页面构建
- STEP 5： 土地公对话语料收集，微调本地模型，增加模型个性化对话功能
- STEP 6： 加入 Agent 功能，允许通过谷歌搜索等 api 从外部获取游戏知识（比如攻略）

### 一些可供参考的资料

[1] [使用 LangChain 的 RAG](https://medium.com/data-science-in-your-pocket/graphrag-using-langchain-31b1ef8328b9)

[2] [天机：人情世故大模型](https://github.com/SocialAI-tianji/Tianji)

[3] [Tiny-Universe：大模型白盒子构建指南](https://github.com/datawhalechina/tiny-universe)

[4] [GraphRAG](https://github.com/microsoft/graphrag)

[5] [TinyGraphRAG](https://github.com/limafang/tiny-graphrag)

[6] [GraphRAG 简明介绍](https://medium.com/@cch.chichieh/knowledge-graph-rag-microsoft-graphrag-%E5%AF%A6%E4%BD%9C%E8%88%87%E8%A6%96%E8%A6%BA%E5%8C%96%E6%95%99%E5%AD%B8-ac07991855e6)