import os
import re
import json
import requests
from bs4 import BeautifulSoup
from file_operation import _create_file_if_not_exists, _create_folder_if_not_exists


def get_description(url):
    # 目标URL
    # url = 'https://www.gamersky.com/handbook/202408/1803371_24.shtml'

    # 使用 requests 获取网页内容
    response = requests.get(url)
    html = response.content

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html, 'html.parser')

    # 提取 GsWeTxt1 类中的文本
    character_name = soup.find('div', class_='GsWeTxt1').get_text()

    # 正则表达式，用于匹配“第X页：”的文本模式
    page_pattern = re.compile(r'^第\d+页：')

    # 提取 GsWeTxt1 后的所有 <p> 标签
    description = []
    for p in soup.find_all('p'):
        # 检查是否包含“第X页”模式的文本，并跳过
        if page_pattern.match(p.get_text()):
            continue
        # 检查是否包含“点击进入”的链接
        if p.find('a') and '点击进入' in p.get_text():
            break
        # 检查是否有 GsImageLabel 类
        if 'GsImageLabel' in p.get('class', []):
            break
        # 提取 <p> 标签的内容并添加换行符
        description.append(p.get_text()+ '\n\n')

    # 将提取的文本组合起来
    description_text = ''.join(description)  # 使用 ''.join 保持每行的换行符

    return description_text


def write2md(role, level, description):
    # 定义变量，创建目录与文件
    file_name = f"{role}.md"
    dir_name = f"../data/portraits/{level}"
    markdown_file = os.path.join(dir_name, file_name)
    _create_folder_if_not_exists(dir_name)
    _create_file_if_not_exists(markdown_file)

    # 生成 Markdown 内容（Markdown模板内容需要置前排列,否则写入文件会以代码块展示）
    markdown_content = f"""
## 类型

{level}

## 描述

{description}
    """

    # 将 Markdown 内容写入文件
    with open(markdown_file, "w", encoding="utf-8") as file:
        file.write(markdown_content)
    print(f"Markdown 文件已生成: {markdown_file}")


if __name__ == '__main__':
    # description = get_description('https://www.gamersky.com/handbook/202408/1803371_24.shtml')
    # role = '白衣秀士'
    # level = '人物'
    # write2md(role, level, description)

    _create_folder_if_not_exists('../data/portraits')
    roleinfo_config = r"../workspace/roleinfo.json"
    with open (roleinfo_config, 'r', encoding='utf-8') as file:
        roleinfo = file.read()
    roleinfo_dict = json.loads(roleinfo)

    for level, items in roleinfo_dict.items():
        print(f"类型: {level}")
        for item in items:
            role = item['role']
            url= item['url']
            description = get_description(url)
            write2md(role, level, description)
