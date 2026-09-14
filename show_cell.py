import json
nb_path = r"c:\Users\Sukrit\PycharmProjects\Langgraph-Tutorial\LLM_based_review_workflow.ipynb"
nb = json.load(open(nb_path,'r',encoding='utf-8'))
cell_id='5867d046c7e81579'
for c in nb['cells']:
    if c.get('id')==cell_id:
        print(''.join(c.get('source',[])))
        break
else:
    print('cell not found')
