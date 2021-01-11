import os, PyPDF2, re, io, shutil

# parameter variables
root_dir = r"/Users/erik/Documents/development/git/tesla_invoice_rename/pdfs"
rename_to = r"/Users/erik/Documents/development/git/tesla_invoice_rename/renamed"


# function for renaming the pdfs based on text in the pdf
def rename_pdfs(root_dir, rename_folder):
 # traverse down through the root directory to sub-directories
 for root, _, files in os.walk(root_dir):
  for filename in files:
   basename, extension = os.path.splitext(filename)
   # if a file is a pdf
   if extension == ".pdf":
    # create a reference to the full filename path
    fullpath = root + "/" + basename + extension
    # open the individual pdf
    pdf_file_obj = open(fullpath, "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    page_obj = pdf_reader.getPage(0)

    pdf_text = page_obj.extractText()
    s = io.StringIO(pdf_text)

    pattern = r"PU\d+"
    pattern2 = r"^\d{2}/(\d{2})/(\d{4})"

    # Iterate each line
    for line in s:
    # Regex applied to each line 
        match = re.search(pattern, line)
        match2 = re.search(pattern2, line)
        if match:
            new_line = match.group()
        if match2:
            path = rename_to + "/" + match2.group(2) + "/" + match2.group(1) + "/"
    new_filename = new_line + ".pdf"
    print(path + new_filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    shutil.copy(fullpath, path + new_filename)

rename_pdfs(root_dir,rename_to)