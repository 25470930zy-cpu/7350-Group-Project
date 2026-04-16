from pathlib import Path
import re
base = Path('.').resolve()
print('base', base)
for path in sorted(base.glob('**/*.html')):
    text = path.read_text(encoding='utf-8')
    m = re.search(r'(<nav class="site-nav" aria-label="Main navigation">)(.*?)(</nav>)', text, flags=re.S)
    print(path, 'FOUND' if m else 'NOTFOUND')
