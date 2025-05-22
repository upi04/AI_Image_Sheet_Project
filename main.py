from sheet_handler import connect_sheet, read_sheet_data, update_image_url
from image_generator import generate_image
import urllib.parse

def create_prompt(style, color, theme, title):
    return f"{title} in {style} style with {color} background. {theme}"

def main():
    SHEET_ID = "16xFKyDof0yT_NRfLU6h4t2ZfeqpWOafYiaFlMqh4vJc"
    sheet = connect_sheet(SHEET_ID)

    data = read_sheet_data(sheet)

    for idx, row in enumerate(data, start=2):  
        style = row.get("Image Style", "")
        color = row.get("Background Color", "")
        theme = row.get("Theme Description", "")
        title = row.get("Content Title", "")

        prompt = create_prompt(style, color, theme, title)
        print(f"Generating image for row {idx} with prompt:\n{prompt}")

        filename = f"image_row_{idx}.png"
        filepath = generate_image(prompt, filename=filename)

       
        image_url = "file:///" + urllib.parse.quote(filepath.replace("\\", "/"))

        update_image_url(sheet, idx, image_url)
        print(f"Updated row {idx} with image URL: {image_url}")

if __name__ == "__main__":
    main()
