from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit
import os

def py_to_pdf(input_file, output_file):
    # Create a new PDF with Reportlab
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    # Set font and size (using Courier, which is monospaced)
    font_name = 'Courier'
    font_size = 10
    c.setFont(font_name, font_size)

    # Calculate lines per page
    lines_per_page = int(height / (font_size * 1.2))  # 1.2 for line spacing

    with open(input_file, 'r') as file:
        lines = file.readlines()

    y = height - 40  # Start from top of page with a margin
    for line in lines:
        if y < 40:  # If we're at the bottom of the page
            c.showPage()  # Start a new page
            c.setFont(font_name, font_size)  # Reset font for new page
            y = height - 40  # Reset y to top of page

        # Preserve leading whitespace
        leading_space = len(line) - len(line.lstrip())
        indentation = ' ' * leading_space

        # Wrap long lines, preserving indentation
        wrapped_lines = simpleSplit(line.rstrip(), font_name, font_size, width - 80)
        for i, wrapped_line in enumerate(wrapped_lines):
            if i == 0:
                c.drawString(40, y, indentation + wrapped_line)
            else:
                c.drawString(40 + c.stringWidth(indentation, font_name, font_size), y, wrapped_line)
            y -= font_size * 1.2  # Move to next line

    c.save()

# Usage
input_file = r"C:\Users\kroy2\Documents\python\projects\json_processor\scripts\process_json3.py"
output_file = r"C:\Users\kroy2\Documents\python\projects\json_processor\scripts\process_json3.pdf"
py_to_pdf(input_file, output_file)

print(f"PDF created: {output_file}")