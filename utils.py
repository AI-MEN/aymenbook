import markdown
import re


def find_parents (path_markdown):
    current=path_markdown.split('.md')[0]
    with open(path_markdown, 'r') as f:
        text = f.read()
        #html = markdown.markdown(text)
    rows = text.split("\n")
    parents=[]
    for row in rows:
        if "parent" in row:
            parents+= [(current, re.search(r'\[(.*?)\]',row).group()[1:-1])]
    return parents

def find_recursive_parents (path_markdown, list_paires):
    lst = find_parents(path_markdown)
    #print(path_markdown, lst, list_paires)
    if len(lst)==0:
        return list_paires
    #print("no")
    for parent in lst:
        list_paires.extend(lst)
        find_recursive_parents(parent[1]+".md", list_paires)
    return list_paires


