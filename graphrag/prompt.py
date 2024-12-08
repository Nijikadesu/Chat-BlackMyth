GET_ENTITY = """
## 目标

你是国产3A游戏《黑神话悟空》的影神图（游戏出现人物的简短介绍）知识库小助手。
你需要确定与给出的文本有关的关键概念，这些概念是理解游戏角色背景设定的关键。对于每一个概念，提供一个简短的描述，该描述在给出文本的背景下解释了其相关性与重要性。

## 示例

文本:
"旧时，云风谷深处有一座山庙，庙中住着一位素衣的僧人。此人清修多年，面容清癯，常于夜深时分燃灯诵经。这一夜，忽有金光自庙外破门而入，化作一道火凤直冲僧人而去。僧人不慌不忙，手持木鱼一敲，那木鱼迸发清音，将火凤震落在地。定睛一看，原来是一只浑身燃烧着赤焰的小妖。那妖见被擒，倒也不慌，只冷笑道：“僧人，本妖乃是守火之灵，原本为这山中灵脉镇护，因炼丹而毁了灵根，失了神智。既然今日被擒，倒也无话可说。只可惜，你们这些修道者，修的不过是虚妄的善果，岂能知天地之情？”僧人未答，只取下了供桌上的净水洒向小妖，将其火焰熄灭。赤焰退散后，小妖竟化作一只普通的朱砂蛇。它从腹中吐出一枚殷红的丹珠，低声说道：“此珠可治百毒万病，只望僧人莫再毁山。”僧人接过丹珠，随即将蛇放归山林。此后，这山庙常以丹珠救人，但因其珍贵，一珠千金，穷苦百姓虽闻此事，也只能望庙兴叹。"

回答:
<concept>
    <name>云风谷</name>
    <description>故事发生的地方，山庙所在的地理位置，僧人与蛇妖发生冲突的背景。</description>
</concept>
<concept>
    <name>僧人</name>
    <description>故事人物，居住在云风谷的一座山庙中，身着素衣，清修多年，面容清癯，常于夜深时分燃灯诵经。</description>
</concept>
<concept>
    <name>木鱼</name>
    <description>僧人的法器之一，用来抵御妖怪的侵扰，帮助僧人化解火凤的攻击。</description>
</concept>
<concept>
    <name>蛇妖</name>
    <description>守火之灵，原本为山中灵脉镇护，因炼丹而毁了灵根，失了神智，化成火凤袭击僧人不成反被擒拿，被擒的蛇妖对僧人说：“你们这些修道者，修的不过是虚妄的善果，岂能知天地之情？”，蛇妖被僧人的净水点化，显出原形，是一只朱砂蛇，蛇腹中有一枚殷红的丹珠，可治百毒万病，蛇妖将其赠与僧人，希望他莫再毁山。僧人收下后，将蛇放归山林</description>
</concept>
<concept>
    <name>净水</name>
    <description>僧人的所有物，僧人用其熄灭了朱砂蛇的火焰，将其显出原型。</description>
</concept>
<concept>
    <name>丹珠</name>
    <description>蛇妖的腹中有一枚殷红的单株，可治百毒万病，蛇妖将其赠与僧人，希望他不要再毁坏山林。僧人收下丹珠后，将蛇放归山林。此后，山庙常以丹珠救人，但因其珍贵，一珠千金，穷苦百姓虽然知道此药，也只能望庙兴叹</description>
</concept>
<concept>
    <name>贫苦百姓</name>
    <description>贫苦百姓虽然希望求得丹珠治病，但因其昂贵，只能望庙兴叹</description>
</concept>

## 格式


将每个概念用 <concept> HTML 标签包裹，并在 <name> 标签中包含概念的名称，在 <description> 标签中包含其描述。

## 文本

{text}

## 你的回答
"""


ENTITY_DISAMBIGUATION = """
## Goal
Given multiple entities with the same name, determine if they can be merged into a single entity. If merging is possible, provide the transformation from entity id to entity id.

## Guidelines
1. **Entities:** A list of entities with the same name.
2. **Merge:** Determine if the entities can be merged into a single entity.
3. **Transformation:** If merging is possible, provide the transformation from entity id to entity id.

## Example
1. Entities:
   [
       {"name": "Entity A", "entity id": "entity-1"},
       {"name": "Entity A", "entity id": "entity-2"},
       {"name": "Entity A", "entity id": "entity-3"}
   ]
   
Your response should be:

<transformation>{"entity-2": "entity-1", "entity-3": "entity-1"}</transformation>


2. Entities:
   [
       {"name": "Entity B", "entity id": "entity-4"},
       {"name": "Entity C", "entity id": "entity-5"},
       {"name": "Entity B", "entity id": "entity-6"}
   ]

Your response should be:

<transformation>None</transformation>

## Output Format
Provide the following information:
- Transformation: A dictionary mapping entity ids to the final entity id after merging.

## Given Entities
{entities}

## Your response
"""


GET_TRIPLETS = """
## 目标:
从提供的文本中识别并提取给定概念之间的所有关系，并表示为三元组形式（主语, 谓语, 宾语）。
确定概念之间尽可能多的关系。三元组的实体必须来自给定的实体列表。三元组的关系应准确反映两个概念之间的相互作用或联系。

## 指南:
1. **主语:** 三元组中的第一个实体，它是一个主动参与动作或关系的概念。
2. **谓语:** 描述主语与宾语之间的关系或动作，它说明了主语与宾语之间的联系。
3. **宾语:** 三元组中的第二个实体，通常是受主语影响或与主语有关联的概念。

## 示例:
1. 文本:
    "孙悟空被尊称为齐天大圣。" 
   给定的实体列表: 
   [{{"name": "孙悟空", "entity id": "entity-1"}}, {{"name": "齐天大圣", "entity id": "entity-2"}}]
   输出:
   <triplet><subject>孙悟空</subject><subject_id>entity-1</subject_id><predicate>被尊称为</predicate><object>齐天大圣</object><object_id>entity-2</object_id></triplet>
2. 文本:
    "氢是一种无色、无味、无毒的气体，是宇宙中最轻、最丰富的元素。氧是一种支持燃烧的气体，广泛存在于地球的大气中。水是一种由氢和氧组成的化合物，其化学式为 H2O。"
    给定的实体列表:
    [{{"name": "氢", "entity id": "entity-3"}}, {{"name": "氧", "entity id": "entity-4"}}, {{"name": "水", "entity id": "entity-5"}}]
    输出:
    <triplet><subject>氢</subject><subject_id>entity-3</subject_id><predicate>是...的组成成分</predicate><object>水</object><object_id>entity-5</object_id></triplet>
    <triplet><subject>氧</subject><subject_id>entity-3</subject_id><predicate>是...的组成成分</predicate><object>水</object><object_id>entity-5</object_id></triplet>
3. 文本:
    "小明在周末读了一本书" 
    给定的实体列表:
    []
    输出:
    None

## 格式:
对于每一个提取出的三元组，请严格按照以下 HTML 格式提供输出:
**实体必须仅选自给定的实体列表"**
<triplet><subject>[实体名称]</subject><subject_id>[Entity ID]</subject_id><predicate>[动作或关系]</predicate><object>[Entity]</object><object_id>[实体名称]</object_id></triplet>

## 给定的实体:
{entity}

## 文本:
{text}

## 额外指示:
- 在提供响应之前，需对文章进行逐句解析和分析。
- 主语 和 宾语 必须从给定的实体列表中选择，且不可更改其内容。
- 如果未找到涉及给定实体的相关三元组，则不应提取任何三元组。
- 如果文本中的概念与给定实体相似，但名称不同，请将其重写为符合给定实体列表要求的形式。

## 你的回答:
"""

GEN_COMMUNITY_REPORT = """
## 角色
你是一个人工智能助手，帮助人工分析师进行信息发现。
信息发现是识别和评估与某些实体（例如组织和个人）在网络中相关的信息的过程。

## 目标
编写一个关于社区的综合报告。
给定一组属于社区的实体以及它们的关系和可选的相关声明。该报告将用于向决策者提供有关社区和它们潜在影响的信息。
报告的内容包括社区关键实体的概述、它们的法律合规性、技术能力、声誉以及值得注意的声明。

## 报告结构

报告应包括以下部分：

- TITLE: 代表社区关键实体的名称 - 标题应该简短但具体，尽可能包含代表性命名实体。
- SUMMARY: 社区整体结构的执行摘要，描述其实体之间的关系，以及与其实体相关的重要信息。
- DETAILED FINDINGS: 社区的 5-10 个关键洞察列表。每个洞察应有一个简短的总结，并附有多段解释性文本，依据以下基础规则进行详细阐述，要全面。

返回格式化为 JSON 的字符串，格式如下：
{{
"title": <报告标题>,
"summary": <执行摘要>,
"findings": [
{{
"summary":<洞察 1 总结>,
"explanation": <洞察 1 解释>
}},
{{
"summary":<洞察 2 总结>,
"explanation": <洞察 2 解释>
}}
...
]
}}

## 基础规则
不要包含没有支持证据的信息。

## 示例输入
-----------
文本:
```
实体:
```csv
entity,description
VERDANT OASIS PLAZA,Verdant Oasis Plaza is the location of the Unity March
HARMONY ASSEMBLY,Harmony Assembly is an organization that is holding a march at Verdant Oasis Plaza
```
关系:
```csv
source,target,description
VERDANT OASIS PLAZA,UNITY MARCH,Verdant Oasis Plaza is the location of the Unity March
VERDANT OASIS PLAZA,HARMONY ASSEMBLY,Harmony Assembly is holding a march at Verdant Oasis Plaza
VERDANT OASIS PLAZA,UNITY MARCH,The Unity March is taking place at Verdant Oasis Plaza
VERDANT OASIS PLAZA,TRIBUNE SPOTLIGHT,Tribune Spotlight is reporting on the Unity march taking place at Verdant Oasis Plaza
VERDANT OASIS PLAZA,BAILEY ASADI,Bailey Asadi is speaking at Verdant Oasis Plaza about the march
HARMONY ASSEMBLY,UNITY MARCH,Harmony Assembly is organizing the Unity March
```
```
输出:
{{
"title": "Verdant Oasis Plaza and Unity March",
"summary": "The community revolves around the Verdant Oasis Plaza, which is the location of the Unity March. The plaza has relationships with the Harmony Assembly, Unity March, and Tribune Spotlight, all of which are associated with the march event.",
"findings": [
{{
"summary": "Verdant Oasis Plaza as the central location",
"explanation": "Verdant Oasis Plaza is the central entity in this community, serving as the location for the Unity March. This plaza is the common link between all other entities, suggesting its significance in the community. The plaza's association with the march could potentially lead to issues such as public disorder or conflict, depending on the nature of the march and the reactions it provokes."
}},
{{
"summary": "Harmony Assembly's role in the community",
"explanation": "Harmony Assembly is another key entity in this community, being the organizer of the march at Verdant Oasis Plaza. The nature of Harmony Assembly and its march could be a potential source of threat, depending on their objectives and the reactions they provoke. The relationship between Harmony Assembly and the plaza is crucial in understanding the dynamics of this community."
}},
{{
"summary": "Unity March as a significant event",
"explanation": "The Unity March is a significant event taking place at Verdant Oasis Plaza. This event is a key factor in the community's dynamics and could be a potential source of threat, depending on the nature of the march and the reactions it provokes. The relationship between the march and the plaza is crucial in understanding the dynamics of this community."
}},
{{
"summary": "Role of Tribune Spotlight",
"explanation": "Tribune Spotlight is reporting on the Unity March taking place in Verdant Oasis Plaza. This suggests that the event has attracted media attention, which could amplify its impact on the community. The role of Tribune Spotlight could be significant in shaping public perception of the event and the entities involved."
}}
]
}}

## 真实数据
使用以下文本生成你的回答。请确保你的回答中没有任何虚构内容。

文本:
```
{input_text}
```

报告应包括以下部分：

- TITLE: 代表社区关键实体的名称 - 标题应该简短但具体，尽可能包含代表性命名实体。
- SUMMARY: 社区整体结构的执行摘要，描述其实体之间的关系，以及与其实体相关的重要信息。
- DETAILED FINDINGS: 社区的 5-10 个关键洞察列表。每个洞察应有一个简短的总结，并附有多段解释性文本，依据以下基础规则进行详细阐述，要全面。

返回格式化为 JSON 的字符串，格式如下：
{{
"title": <report_title>,
"summary": <executive_summary>,
"rating": <impact_severity_rating>,
"rating_explanation": <rating_explanation>,
"findings": [
{{
"summary":<insight_1_summary>,
"explanation": <insight_1_explanation>
}},
{{
"summary":<insight_2_summary>,
"explanation": <insight_2_explanation>
}}
...
]
}}

## 基础规则
不要包含没有支持证据的信息。

输出:
"""

GLOBAL_MAP_POINTS = """
您是一位有用的助手，回答有关表格中数据的问题。


---目标---

生成一个响应，包含一系列关键信息，回答用户的问题，并总结数据表中所有相关的信息。

你应该使用以下提供的数据表作为生成响应的主要依据。

如果你不知道答案，或者数据表中没有足够的信息来回答问题，只需说明无法回答。请不要编造信息。

每个关键信息点应包括以下内容:
- 描述：对该点的详细描述。
- 重要性分数：一个介于 0 到 100 之间的整数分数，表示该信息点在回答用户问题中的重要性。如果无法回答问题，则分数为 0。

响应应采用以下 HTML 格式：

<point><description>"对第一点的描述..."</description><score>重要性分数</score></point>
<point><description>"对第二点的描述..."</description><score>重要性分数</score></point>


响应应保留原有意义，并且保留情态动词（例如“应该”，“也许”或“将会”）的用法。
不要包含没有支持证据的信息。

---数据表格---

{context_data}

---用户查询---

{query}

---目标---

生成一个响应，包含一系列关键信息，回答用户的问题，并总结数据表中所有相关的信息。

你应该使用以下提供的数据表作为生成响应的主要依据。

如果你不知道答案，或者数据表中没有足够的信息来回答问题，只需说明无法回答。请不要编造信息。

每个关键信息点应包括以下内容:
- 描述：对该点的详细描述。
- 重要性分数：一个介于 0 到 100 之间的整数分数，表示该信息点在回答用户问题中的重要性。如果无法回答问题，则分数为 0。

响应应采用以下 HTML 格式：

<point><description>"对第一点的描述..."</description><score>重要性分数</score></point>
<point><description>"对第二点的描述..."</description><score>重要性分数</score></point>


"""

LOCAL_QUERY = """
你是一名《黑神话：悟空》影神图对话助手，根据上下文回答用户关于影神图的问题，你将使用小神称呼自己。

## 用户查询
{query}

## 上下文
{context}

## 任务
基于给定的上下文，请提供对用户查询的响应。

## 注意
使用检索到的上下文来回答问题。如果您不知道答案，就直接说不知道。
1.根据我的提问,总结检索到的上下文中与提问最接近的部分,将相关部分浓缩为一段话返回;
2.根据语料结合我的问题,给出建议和解释。

## 示例输入:
-----------
请介绍二郎显圣真君
输出:
小神为您查询了《影神图》，以下信息将帮助你更好地了解显圣二郎真君：
...
-----------
请介绍反恐精英
小神为您翻遍了《影身图》，偏偏找不到任何关于反恐精英的记载，小圣息怒啊!

## 你的回答
"""

GLOBAL_QUERY = """
## 用户查询
{query}

## 上下文
{context}

## 任务
基于给定的上下文，请提供你对用户查询的响应。

## 注意
如果给定的上下文没有足够的信息支撑对用户查询的响应，请如实回答无法响应。

## 示例输入:
-----------
请介绍二郎显圣真君
输出:
小神为您查询了《影神图》，以下信息将帮助你更好地了解显圣二郎真君：
...
-----------
请介绍反恐精英
小神为您翻遍了《影身图》，偏偏找不到任何关于反恐精英的记载，小圣息怒啊!

## 你的回答
"""
