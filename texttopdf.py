import StringIO
input_stream = StringIO.StringIO(text)
result = StringIO.StringIO()

pdfclass = pyText2Pdf(input_stream, result, "PDF title")
pdfclass.Convert()

response = HttpResponse(result.getvalue(), mimetype="application/pdf")
response['Content-Disposition'] = 'attachment; filename=pdf_report.pdf'

return response