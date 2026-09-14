import json, sys
nb_path = r"c:\Users\Sukrit\PycharmProjects\Langgraph-Tutorial\LLM_based_review_workflow.ipynb"
nb = json.load(open(nb_path, 'r', encoding='utf-8'))
code_cells = [ ''.join(c.get('source',[])) for c in nb.get('cells',[]) if c.get('cell_type')=='code']
concat = '\n\n'.join(code_cells)
try:
    compile(concat, 'concat', 'exec')
    print('Concatenated code compiles OK')
except Exception as e:
    import traceback
    print('Error:', repr(e))
    tb = traceback.format_exc()
    print(tb)
    # dump first 200 lines
    for i,line in enumerate(concat.splitlines()[:200],1):
        print(f'{i:4}: {line}')
    sys.exit(1)
