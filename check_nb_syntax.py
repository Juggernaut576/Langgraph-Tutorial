import json, sys
nb_path = r"c:\Users\Sukrit\PycharmProjects\Langgraph-Tutorial\LLM_based_review_workflow.ipynb"
nb = json.load(open(nb_path, 'r', encoding='utf-8'))
for i,cell in enumerate(nb.get('cells',[])):
    if cell.get('cell_type')!='code':
        continue
    src = ''.join(cell.get('source',[]))
    try:
        compile(src, f'cell_{i}', 'exec')
    except Exception as e:
        print(i, cell.get('id'), repr(e))
        print('---SOURCE START---')
        print(src)
        print('---SOURCE END---')
        sys.exit(0)
print('No syntax errors detected in individual cells')
