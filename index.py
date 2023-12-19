import subprocess

pdf_path = '/Users/mac/Desktop/k2.pdf'
html_path = '/Users/mac/apps/pdf/k4.html'

def convert_pdf_to_html(pdf_path, output_html_path):
    try:
        result = subprocess.run(
            ['pdf2htmlEX', pdf_path,  output_html_path],
            capture_output=True,
            text=True,
            check=True
        )
        print(f'Successfully converted {pdf_path} to {output_html_path}')
    except subprocess.CalledProcessError as e:
        print(f'Error converting {pdf_path} to HTML: {e}')
        print(f"Command failed with return code {e.returncode}")
        print(f"Output: {e.output}")

# Replace 'input.pdf' and 'output.html' with your PDF and desired HTML file paths
convert_pdf_to_html(pdf_path, html_path)
