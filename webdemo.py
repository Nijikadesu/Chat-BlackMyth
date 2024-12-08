import os
import gradio as gr
from dotenv import load_dotenv
from graphrag.graph import TinyGraph
from graphrag.embedding.zhipu import zhipuEmb
from graphrag.llm.zhipu import zhipuLLM
from graphrag.embedding.bce import BCEEmb
from graphrag.llm.qwen import Qwen2_5


load_dotenv()

use_zhipu_api = os.getenv('USE_ZHIPU_API')
zhipu_api_key = os.getenv("ZHIPU_API_KEY")
emb_name, llm_name = os.environ["EMB_NAME"], os.environ["LLM_NAME"]
emb_url, llm_url = os.environ["EMB_URL"], os.environ["LLM_URL"]
neo4j_url, neo4j_username, neo4j_password = os.environ["NEO4J_URL"], os.environ["NEO4J_USER"], os.environ["NEO4J_PASS"]


def init_graph(data_path):
    global emb, llm, graph

    if use_zhipu_api == 'YES':
        emb = zhipuEmb('embedding-3', zhipu_api_key)
        llm = zhipuLLM('glm-4-flash', zhipu_api_key)
    else:
        emb = BCEEmb(emb_name, emb_url)
        llm = Qwen2_5(llm_name, llm_url)

    emb = BCEEmb(emb_name, emb_url)
    llm = Qwen2_5(llm_name, llm_url)
    graph = TinyGraph(
        url=neo4j_url,
        username=neo4j_username,
        password=neo4j_password,
        llm=llm,
        emb=emb,
    )

    graph.add_document(data_path)
    return f"doc '{data_path}' has been loaded."


def chatbot1_response(user_input):
    output = graph.local_query(user_input)
    return {"role": "assistant", "content": f"{output}"}


def chatbot2_response(user_input):
    output = llm.predict(user_input)
    return {"role": "assistant", "content": f"{output}"}


def combined_response(history1, history2, user_input):
    response1 = chatbot1_response(user_input)
    history1.append({"role": "user", "content": user_input})
    history1.append(response1)

    response2 = chatbot2_response(user_input)
    history2.append({"role": "user", "content": user_input})
    history2.append(response2)

    return history1, history2, ""


TITLE="""
# 基于 GraphRAG 的《黑神话：悟空》影神图小助手 \n
### 基座模型: BCE-Embedding + Qwen2.5-7b-Instruct \n
### 说明：点击下方按钮初始化 GraphRAG | 聊天框输入问题后发送，将同时开启两段对话，分别对应借助/不借助GraphRAG进行答案生成。
### 
"""


with gr.Blocks() as demo:
    gr.Markdown(TITLE)

    with gr.Row(equal_height=True):
        with gr.Column(scale=3, min_width=200):
            data_path = gr.Textbox(label="数据路径", placeholder="输入数据路径后，点击右侧按钮初始化 GraphRAG")
        with gr.Column(scale=1, min_width=100):
            update_button = gr.Button("初始化 GraphRAG")
        with gr.Column(scale=3, min_width=200):
            init_message = gr.Textbox(
                label="初始化提示",
                placeholder="打印 GraphRAG 初始化状态",
                interactive=False,
                lines=1,
            )

    with gr.Row():
        with gr.Column():
            gr.Markdown("### ChatBot 1 | 使用 GraphRAG")
            chatbot1 = gr.Chatbot(
                label="Chat",
                type="messages",
                avatar_images=(None, "https://em-content.zobj.net/source/twitter/376/hugging-face_1f917.png"),
                height=466
            )
        with gr.Column():
            gr.Markdown("### ChatBot 2 | 不使用 GraphRAG")
            chatbot2 = gr.Chatbot(
                label="Chat",
                type="messages",
                avatar_images=(None, "https://em-content.zobj.net/source/twitter/376/hugging-face_1f917.png"),
                height=466
            )


    user_input = gr.Textbox(show_label=False, placeholder="输入你想了解的影神图角色...", lines=1)
    send_button = gr.Button("发送")

    update_button.click(
        init_graph,
        inputs=[data_path],
        outputs=[init_message],
    )

    send_button.click(
        combined_response,
        inputs=[chatbot1, chatbot2, user_input],
        outputs=[chatbot1, chatbot2, user_input]
    )


if __name__ == "__main__":
    demo.launch()
