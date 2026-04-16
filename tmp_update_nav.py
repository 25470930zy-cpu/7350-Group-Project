from pathlib import Path
import os
import re
base = Path('d:/AIDM/sem2/7350/Group/static-site')
nav_items = [
    ('Core Concepts','core-concepts/aigc-definition.html',[
        ('Definition and Category of AIGC','core-concepts/aigc-definition.html'),
        ('Classifying Misinformation','core-concepts/classifying-misinformation.html'),
        ('The Double-Edged Sword','core-concepts/double-edged-sword.html'),
    ]),
    ('Literature','literature/mechanism.html',[
        ('Mechanism','literature/mechanism.html'),
        ('Psychology and Trust','literature/psychology-trust.html'),
        ('Dissemination and Algorithms','literature/dissemination-algorithms.html'),
        ('Ethics and Detection','literature/ethics-detection.html'),
    ]),
    ('Truth Lab','truth-lab/myths-debunked.html',[
        ('Myths Debunked','truth-lab/myths-debunked.html'),
        ('Case Study','truth-lab/case-study.html'),
    ]),
    ('Future Strategies','future-strategies/technical-solution.html',[
        ('Technical Solution','future-strategies/technical-solution.html'),
        ('Legal and Policy','future-strategies/legal-policy.html'),
        ('Social Countermeasures','future-strategies/social-countermeasures.html'),
    ]),
]

for path in sorted(base.glob('**/*.html')):
    text = path.read_text(encoding='utf-8')
    def rel_link(target):
        target_path = base / target
        rel = os.path.relpath(target_path, start=path.parent)
        return rel.replace('\\', '/')

    depth = len(path.parent.relative_to(base).parts)
    nav_html = ['      <nav class="site-nav" aria-label="Main navigation">\n']
    if depth > 0:
        nav_html.append(f'        <a href="{rel_link("index.html")}">Home</a>\n')
    for label, target, subs in nav_items:
        active = False
        current = path.resolve()
        if current == (base / target).resolve() or current.parent == (base / target).parent:
            active = True
        class_attr = ' class="active"' if active else ''
        nav_html.append('        <div class="nav-group">\n')
        nav_html.append(f'          <a href="{rel_link(target)}"{class_attr}>{label}</a>\n')
        nav_html.append('          <button type="button" class="nav-toggle" aria-expanded="false" aria-label="Toggle submenu"></button>\n')
        nav_html.append('          <div class="submenu">\n')
        for sub_label, sub_target in subs:
            nav_html.append(f'            <a href="{rel_link(sub_target)}">{sub_label}</a>\n')
        nav_html.append('          </div>\n')
        nav_html.append('        </div>\n')
    nav_html.append(f'        <a href="{rel_link("reference.html")}">Reference</a>\n')
    nav_html.append('      </nav>')
    nav_block = ''.join(nav_html)

    new_text = re.sub(r'<nav class="site-nav" aria-label="Main navigation">.*?</nav>', nav_block, text, flags=re.S)
    if new_text == text:
        print('NO CHANGE', path)
        continue
    script_path = rel_link('nav.js')
    if f'<script src="{script_path}"></script>' not in new_text:
        new_text = new_text.replace('</body>', f'  <script src="{script_path}"></script>\n</body>')
    path.write_text(new_text, encoding='utf-8')
    print('UPDATED', path)
