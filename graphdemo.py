import os
from dotenv import load_dotenv
from graphrag.graph import TinyGraph
from graphrag.embedding.zhipu import zhipuEmb
from graphrag.llm.zhipu import zhipuLLM
from graphrag.embedding.bce import BCEEmb
from graphrag.llm.qwen import Qwen2_5


load_dotenv()

use_zhipu_api = os.environ.get('USE_ZHIPU_API')
zhipu_api_key = os.environ.get('ZHIPU_API_KEY')
emb_name, llm_name = os.environ["EMB_NAME"], os.environ["LLM_NAME"]
emb_url, llm_url = os.environ["EMB_URL"], os.environ["LLM_URL"]
neo4j_url, neo4j_username, neo4j_password = os.environ["NEO4J_URL"], os.environ["NEO4J_USER"], os.environ["NEO4J_PASS"]

global emb, llm

if use_zhipu_api == 'YES':
    emb = zhipuEmb('embedding-3', zhipu_api_key)
    llm = zhipuLLM('glm-4-flash', zhipu_api_key)
else:
    emb = BCEEmb(emb_name, emb_url)
    llm = Qwen2_5(llm_name, llm_url)

graph = TinyGraph(
    url=neo4j_url,
    username=neo4j_username,
    password=neo4j_password,
    llm=llm,
    emb=emb,
)

# graph.add_document('/path/to/your/data/')
# query_for_example = "请介绍五行战车"
#
# no_graph_res = llm.predict(query_for_example)
# local_res = graph.local_query(query_for_example)
# global_res = graph.global_query(query_for_example)
#
# print(f"no_graph_res: {no_graph_res}")
# print(f"local_res: {local_res}")
# print(f"global_res: {global_res}")
