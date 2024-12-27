import pdfplumber
import json

#used to extract adolescent events
def extract_table_from_pdf(pdf_path,start_page=0,stop_page=4):
    """
    Extracts a table from a PDF, handling multi-page scenarios.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        A list of dictionaries, where each dictionary represents a row in the table.
    """

    with pdfplumber.open(pdf_path) as pdf:
        table_data = []
        
        for page_num, page in enumerate(pdf.pages):
            if page_num in range(start_page,stop_page):
                print(page_num)
                table = page.extract_table()
                print(table)
                input()
                if table is None:
                    continue

                for line in table:
                    if line[0].isnumeric():
                        elem = {"roll":int(line[0])}
                        elem['event']=line[1]
                        elem['effects']=line[2]
                        table_data.append(elem)
        return table_data


# Example usage
pdf_file = "mutant_chronicles_rulebook.pdf"  # Replace with the actual path
table_data = extract_table_from_pdf(pdf_file,start_page=55,stop_page=59)

# # Save the data to a JSON file
with open("table_data.json", "w") as f:
    json.dump(table_data, f, indent=4)