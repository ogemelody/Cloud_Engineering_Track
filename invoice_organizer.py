import os
import zipfile
from rapidfuzz.process import extract
from pathlib import Path
#to  extract data from zip file
invoice = "invoices.zip"
extract_to = "invoices"
#os.mkdir("invoices")
"""
with zipfile.ZipFile(invoice, "r") as zip_ref:
    zip_ref.extractall(extract_to)
    """
invoices_path = Path("invoices/invoices")
print(os.listdir(invoices_path))



def extract_month(invoices_list):

    for invoice in invoices_list:
        try:
            invoice_actual_name = invoice.split(".")
            invoice_name = invoice_actual_name[0]
            month_name = invoice_name.split("_")
            month = month_name[-1]
            return (month, invoice_name)
        except:
            print("Error:None")

def month_folder():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    for month in months:
        if not os.path.exists(month):  # Check if folder already exists
            os.mkdir(month)
            print(f"Created folder: {month}")
        else:
            print(f"Folder already exists: {month}")


def move_file(file, month):
    if month:
        # Construct full path for source and destination
        source_path = os.path.join('/Users/melodyegwuchukwu/PycharmProjects/Cloud_Engineering_Track/invoices/invoices/', file)  # Source file path
        destination_path = os.path.join(month,file)  # Destination folder path
        print(destination_path)
        try:
            os.rename(source_path, destination_path)
            print(f"Moved {file} to {month}")
        except FileNotFoundError as e:
            print(f"Error moving {file}: {e}")
    else:
        print(f"Skipping {file} due to extraction error.")


def main():
    invoices_list = os.listdir('invoices/invoices')  # List all files in the 'invoices' folder
      # Create month folders#
    month = extract_month(invoices_list)[0]
    invoices_name = extract_month(invoices_list)[1]
    month_folder()
    move_file(invoices_name, month)


            #continue# If a month was successfully extracted
              # Move the invoice file to the corresponding month folder


if __name__ == '__main__':
    main()