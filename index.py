import subprocess

def pdf_to_html(pdf_path, html_output_path):
    command = f"wkhtmltopdf {pdf_path} {html_output_path}"
    subprocess.run(command, shell=True)

# Example usage
pdf_path = "/srv/pdf/files/JS3.pdf"
html_output_path = "/srv/pdf/files/kips.html"

pdf_to_html(pdf_path, html_output_path)



