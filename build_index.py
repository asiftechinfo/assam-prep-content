import json, os, re
rx = re.compile(r'^(\d{4}-\d{2}-\d{2})[\s_-]*(.*)$')
names = [f for f in os.listdir('current_affairs') if f.lower().endswith('.pdf')]
ms = [(f, rx.match(f[:-4])) for f in names]
items = [{'file': f, 'date': m.group(1) if m else '', 'title': (m.group(2) if m and m.group(2) else f[:-4])} for f, m in ms]
items.sort(key=lambda x: (x['date'], x['title']), reverse=True)
json.dump(items, open('current_affairs/index.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
