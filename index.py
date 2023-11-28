import fitz  # PyMuPDF

def pdf_to_html(pdf_path, output_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Initialize HTML content
    html_content = ""

    # Iterate through pages and extract text
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        html_content += page.get_text("html")

    # Write HTML content to the output file
    with open(output_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

# Example usage
pdf_path = "/Users/mac/apps/pdf/files/JS3.pdf"
output_path = "/Users/mac/apps/pdf/files/kips.html"
pdf_to_html(pdf_path, output_path)
