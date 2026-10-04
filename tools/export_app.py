"""Build the standalone teaching app. Python 3 standard library only."""
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
TITLE = 'Lung Mechanics Lab'
fragment = (ROOT / 'src/lung-mechanics.html').read_text(encoding='utf-8')
styles = (ROOT / 'tools/base.css').read_text(encoding='utf-8')
runtime = (ROOT / 'tools/tooltip-runtime.html').read_text(encoding='utf-8')
shell = (ROOT / 'tools/page-template.html').read_text(encoding='utf-8')
icon = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#18344b"/><path d="M16 5v8m0 0-5 5m5-5 5 5" fill="none" stroke="#ffffff" stroke-width="2"/><ellipse cx="9" cy="21" rx="5" ry="8" fill="#63b5ee"/><ellipse cx="23" cy="21" rx="5" ry="8" fill="#63b5ee"/></svg>'
page = shell.replace('{{TITLE}}', TITLE).replace('{{ICON}}', quote(icon, safe='')).replace('{{STYLES}}', styles).replace('{{APP}}', fragment).replace('{{RUNTIME}}', runtime)
destination = ROOT / 'dist/index.html'
destination.parent.mkdir(exist_ok=True)
destination.write_text(page, encoding='utf-8')
print(f'Built {destination.name} ({len(page.encode("utf-8")):,} bytes)')
