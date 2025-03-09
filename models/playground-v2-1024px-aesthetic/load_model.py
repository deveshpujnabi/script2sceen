from diffusers import DiffusionPipeline
import torch

# Correct Model ID for DeepFloyd IF
model_id = "playgroundai/playground-v2-1024px-aesthetic"

# Load Pipeline with Optimized Settings
pipe = DiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    variant="fp16" if torch.cuda.is_available() else None,  # Optimize for GPU
    use_safetensors=True  # Load weights in SafeTensors format
)

# Move to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe.to(device)

