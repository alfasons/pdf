import subprocess

def html_to_pdf(html_path, output_path):
    command = f"wkhtmltopdf {html_path} {output_path}"
    subprocess.run(command, shell=True)

# Example usage
html_path = " /srv/pdf/files/kips.pdf"
pdf_output_path = "/srv/pdf/files/JS3.pdf"

html_to_pdf(html_path, pdf_output_path)
