import subprocess

def html_to_pdf(html_path, output_path):
    command = f"wkhtmltopdf {html_path} {output_path}"
    subprocess.run(command, shell=True)

# Example usage
html_path = "/Users/mac/apps/pdf/files/JS3.pdf"
pdf_output_path = "/Users/mac/apps/pdf/files/kips.pdf"

html_to_pdf(html_path, pdf_output_path)






# Example usage
pdf_path = "/Users/mac/apps/pdf/files/JS3.pdf"
output_path = "/Users/mac/apps/pdf/files/kips.html"
pdf_to_html(pdf_path, output_path)
