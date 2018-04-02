from jinja2 import Environment, FileSystemLoader

import pdfkit

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("myreport.html")

template_vars = {"title" : "Sales Funnel Report cco Ntional",
                 "vol_list": "Nikuj is bad boy"}
html_out = template.render(template_vars)

pdfkit.from_string(html_out,'d:\\rpt3.pdf')


#HTML(string=html_out).write_pdf("report.pdf")

