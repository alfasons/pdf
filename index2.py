import subprocess

def convert_pdf_to_html(pdf_path, output_path):
    try:
        subprocess.run(['pdftohtml', '-noframes', '-enc', 'UTF-8', '-c', '-q', pdf_path, output_path])
        print(f'Successfully converted {pdf_path} to {output_path}')
    except Exception as e:
        print(f'Error converting {pdf_path} to HTML: {e}')

if __name__ == '__main__':
    pdf_file_path = '/Users/mac/Desktop/k2.pdf'
    html_output_path = '/Users/mac/apps/pdf/k4.html'

    convert_pdf_to_html(pdf_file_path, html_output_path)
 

 