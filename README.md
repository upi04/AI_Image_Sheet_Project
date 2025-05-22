# AI_Image_Sheet_Project


# 🖼️ Automated Image Generation with Google Sheets & Stable Diffusion

This project automates the generation of images based on prompts stored in a Google Sheets document. It uses the **Stable Diffusion v1.5** model from Hugging Face and integrates with Google Sheets API to read and update data.

---

## 📌 Features

- ✅ Automatically reads image prompts from a Google Sheet  
- 🧠 Generates images using Stable Diffusion v1.5 (offline or with Hugging Face)  
- 💾 Saves images to a local folder  
- 🔁 Uploads the generated image URL back to Google Sheets  

---

## 📁 Project Structure

```bash
├── main.py                 # Main execution script
├── sheet_handler.py        # Handles reading and writing to Google Sheets
├── generate_image.py       # Loads the AI model and generates the image
├── credentials.json        # Google service account credentials
├── generated_images/       # Folder to store output images
├── .env                    # Environment variables (e.g., Hugging Face token)
└── README.md               # Project documentation
