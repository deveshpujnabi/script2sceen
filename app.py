# Step 1: Install necessary dependencies
import torch
import gradio as gr
from diffusers import DiffusionPipeline

# Step 2: Correct Model ID for DeepFloyd IF (Playground AI aesthetic model)
model_id = "playgroundai/playground-v2-1024px-aesthetic"

# Load the model pipeline with optimized settings
pipe = DiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    variant="fp16" if torch.cuda.is_available() else None,  # Optimize for GPU if available
    use_safetensors=True  # Load weights in SafeTensors format
)

# Move the model to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe.to(device)

# Step 3: Define function for generating image using Playground AI aesthetic model
def generate_image_playground_ai(prompt):
    try:
        # Generate the image using the model
        image = pipe(prompt).images[0]
        return image
    except Exception as e:
        return f"Error: {str(e)}"

# Step 4: Gradio interface for interactive text-to-image generation
def generate_image_gradio(prompt):
    output_image = generate_image_playground_ai(prompt)
    if isinstance(output_image, str):
        return output_image  # Return the error message if any
    else:
        return output_image  # Return the generated image

# Launch Gradio interface
gr.Interface(fn=generate_image_gradio, inputs="text", outputs="image").launch()
