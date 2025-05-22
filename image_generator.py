import torch
from diffusers import StableDiffusionPipeline
import os

# Load the pre-trained Stable Diffusion model from HuggingFace
model_id = "runwayml/stable-diffusion-v1-5"

# Load the image generation pipeline with the model
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)

# Use GPU if available, otherwise use CPU
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Function to generate and save image from a given prompt
def generate_image(prompt, output_dir="generated_images", filename="output.png"):
    # Create output folder if not exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate the image from the prompt using Stable Diffusion
    image = pipe(prompt, guidance_scale=7.5, num_inference_steps=50).images[0]

    # Save image to the output directory
    filepath = os.path.join(output_dir, filename)
    image.save(filepath)
    return filepath
