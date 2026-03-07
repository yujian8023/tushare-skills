import re
import os

import pandas as pd


class Node:
    id: int
    parent_id: int
    is_doc: bool
    title: str
    desc: str = ''
    name: str
    path: str
    content: str
    children: list['Node']
    categories: list[str]

def parse_df_recursive(df: pd.DataFrame, parent_id: int, parent_titles: list[str]) -> list['Node']:
    nodes = []
    for _, row in df[df['PARENT_ID'] == parent_id].iterrows():
        name = re.sub(r'[<>:"/\\|?*]', '', row.TITLE)
        name = name.replace('（', '(')
        name = name.replace('）', ')')
        node = Node()
        node.id = row['ID']
        node.parent_id = parent_id
        node.is_doc = row['IS_DOC']
        node.title = row['TITLE']
        node.name = name
        node.content = row['SRC_CONTENT']
        node.categories = parent_titles
        if isinstance(node.content, str):
            mm = re.search(r'描述[:： ]+(?P<desc>.+)\n', node.content)
            if mm:
                node.desc = mm.group('desc')
        nodes.append(node)
        if node.is_doc:
            continue
        node.children = parse_df_recursive(df, node.id, parent_titles + [node.name])
    return nodes


def create_dir_file_recursive(children: list[Node], path: str, docs: list[Node]):
    for child in children:
        if child.is_doc:
            file_path = os.path.join(path, child.name+'.md')
            child.path = file_path.lstrip('tushare/')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(child.content)
            docs.append({
                'id': child.id,
                'title': f'[{child.title}]({file_path})',
                'categories': ','.join(child.categories),
                'desc': child.desc,
            })
        else:
            dir_name = child.name
            current_path = os.path.join(path, dir_name)
            child.path = current_path.lstrip('tushare/')
            os.makedirs(current_path, exist_ok=True)
            create_dir_file_recursive(child.children, current_path, docs)


def main():
    # 读取csv文件，头信息为：ID, PARENT_ID, TITLE, SRC_CONTENT(markdown格式)
    df = pd.read_csv('data/api-doc.csv.csv')
    docids = set[int](df['PARENT_ID'].tolist())
    df['IS_DOC'] = ~df['ID'].isin(docids)
    print(df)
    node_root = parse_df_recursive(df, 2, [])

    # 生成文件
    docs = []
    create_dir_file_recursive(node_root, 'tushare/references', docs)

    # 生成markdown
    df_md = pd.DataFrame(docs)
    df_md.drop(columns=['id'], inplace=True)
    df_md.sort_values(by=['categories'], inplace=True)
    df_md.rename(columns={'title': '标题', 'categories': '分类', 'desc': '描述'}, inplace=True)
    df_md.to_markdown('data/docs.md', index=False)


if __name__ == "__main__":
    main()
