import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Connect to Google Sheets using a service account
def connect_sheet(sheet_id, creds_file="credentials.json"):
    # Define the access scopes needed
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Load credentials from JSON key file
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    
    # Authorize client with credentials
    client = gspread.authorize(creds)
    
    # Open the sheet using its ID and get the first worksheet
    sheet = client.open_by_key(sheet_id).sheet1
    return sheet

# Read all data from the sheet (as a list of dictionaries)
def read_sheet_data(sheet):
    # Example: Column A = Style, B = Color, C = Theme, D = Title
    data = sheet.get_all_records()
    return data

# Update the image URL into a specific cell (e.g., column E)
def update_image_url(sheet, row, url, col=5):
    # Update the cell in row X and column E with the image URL
    sheet.update_cell(row, col, url)
