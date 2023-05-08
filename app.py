from jinja2 import Environment, FileSystemLoader
import json

env = Environment(loader=FileSystemLoader('./template', encoding='utf8'))
tmpl = env.get_template('template.j2')

with open('parms.json', encoding='utf8') as f:
    params = json.load(f)

rendered_html = tmpl.render(params)
with open('result.html', 'w', encoding='utf8') as f:
    f.write(rendered_html)
