import os
import shutil
from pathlib import Path


def extract_month(invoice_name):
    # Extract month from the invoice name
    try:
        invoice_name_parts = invoice_name.split("_")
        month = invoice_name_parts[-1].split(".")[0]  # Get month part before .pdf extension
        return month, invoice_name
    except Exception as e:
        print(f"Error: {e}")
        return None, None


def month_folder():
    # Create folders for each month if they don't already exist
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    for month in months:
        if not os.path.exists(month):
            os.mkdir(month)
            print(f"Created folder: {month}")
        else:
            print(f"Folder already exists: {month}")


def move_files():
    # List all files in the 'invoices/invoices' folder
    invoices_list = os.listdir('invoices/invoices')

    # Loop through each file in the list
    for file in invoices_list:
        if file.endswith('.pdf'):  # Ensure we're only dealing with PDF files
            month, invoice_name = extract_month(file)

            if month:  # If month was successfully extracted
                # Create the target folder if it doesn't exist
                if not os.path.exists(month):
                    os.makedirs(month)
                    print(f"Created folder: {month}")

                # Move the file to the corresponding month folder
                source = os.path.join('invoices/invoices', file)
                destination = os.path.join(month, file)

                # Move the file
                shutil.move(source, destination)
                print(f"Moved {file} to {month}/")
            else:
                print(f"Skipping file {file} due to extraction error.")


def main():
    # List all files in the 'invoices/invoices' folder
    invoices_list = os.listdir('invoices/invoices')
    print("Invoice List: ", invoices_list)

    # Create month folders
    month_folder()

    # Move the files into the correct folders
    move_files()


if __name__ == '__main__':
    main()
