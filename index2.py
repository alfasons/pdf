import subprocess

pdf_path = '/srv/offers/console/runtime/templates/UP_15122023/1702637853_bmRZIUYP.pdf'
html_path = '/srv/offers/backend/web/pdf/contract_kips.html'

def convert_pdf_to_html(pdf_path, output_html_path):
    try:
        subprocess.run(['pdf2htmlEX', pdf_path, '--embed-image', '0', '--embed-css', '0', '--embed-font', '0', '--embed-javascript', '0', output_html_path], check=True)
        print(f'Successfully converted {pdf_path} to {output_html_path}')
    except subprocess.CalledProcessError as e:
        print(f'Error converting {pdf_path} to HTML: {e}')

# Replace 'input.pdf' and 'output.html' with your PDF and desired HTML file paths
convert_pdf_to_html(pdf_path, html_path)
