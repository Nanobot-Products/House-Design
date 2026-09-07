with open('index.html', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if '<body>' in line:
            print('body:', i+1)
        if 'id="workspace"' in line:
            print('workspace:', i+1)
        if 'three.min.js' in line:
            print('scripts:', i+1)
            break
