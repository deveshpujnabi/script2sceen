
# Script2Sceen (Text-to-Image Generation) 

This project utilizes the **Playground AI aesthetic model** (DeepFloyd IF) to generate high-quality images based on textual prompts. The model is integrated with the **Gradio** library to provide an interactive user interface for easy text-to-image generation.

The project is designed to run efficiently, utilizing GPU resources when available, and provides users with a seamless and intuitive way to create custom images based on their input.

## Features
- Generate images from text prompts.
- Use of the `playground-v2-1024px-aesthetic` model from Playground AI.
- Gradio frontend for an interactive user interface.
- Cloud deployment options for faster image generation (with GPU support).

---

## System Requirements

### Minimum Requirements for Local Deployment:
- **CPU**: 16GB of RAM (Recommended)
- **GPU**: NVIDIA GPU with at least **6 GB VRAM** (Recommended for faster inference)
- **Operating System**: Linux, Windows, or macOS
- **Python Version**: 3.7 or higher

### Cloud Deployment:
- **Cloud Provider**: AWS, Google Cloud, or Azure (Recommended for GPU instances)
- **GPU**: NVIDIA A100, V100, or Tesla P100 with **16 GB+ VRAM** for optimal performance
- **CPU**: 16 Cores (for cloud machines)
- **RAM**: 16 GB (Minimum)

### Performance Notes:
- On **CPU**, image generation will be slower. Reducing image resolution can improve performance.
- **GPU** usage is highly recommended for faster image generation. You can deploy on **Google Colab**, **Hugging Face**, or **other cloud services** that offer GPUs.

---

## Model Details

The **playground-v2-1024px-aesthetic** model is a pre-trained text-to-image diffusion model that converts textual descriptions into images with high fidelity.

**Model Information**:
- Model ID: `playgroundai/playground-v2-1024px-aesthetic`
- Model Size: ~2 GB
- Resolution: 1024x1024 (Can be adjusted for faster performance)

---

## GPU & Cloud Setup

### Using GPU for Faster Inference:
To utilize a GPU, you can either:
1. **Run Locally on a GPU**:
   - Ensure you have a CUDA-enabled GPU (e.g., NVIDIA GTX 1080 Ti, RTX 3060, or higher).
   - Install PyTorch with CUDA support (if not already installed).
   - If you don’t have a GPU, follow the **CPU** instructions, but note that image generation will take significantly longer.

2. **Cloud Deployment**:
   - You can deploy the app to a cloud server with GPU support for better performance:
     - **Google Cloud**: Use a VM with **NVIDIA Tesla T4, A100, or V100**.
     - **AWS EC2**: Use GPU instances such as **p3.2xlarge** or **g4dn.xlarge**.
     - **Azure**: Use GPU-powered VMs such as **NC-series**.

   - Follow the respective cloud provider documentation to set up GPU-based instances and deploy the model for inference.

---


## Setup Instructions

Follow these steps to set up and run the project locally:

### 1. Clone the Repository
Start by cloning this repository to your local machine:

```bash
git clone https://github.com/deveshpujnabi/script2sceen.git
cd script2sceen
```

### 2. Create and Activate a Virtual Environment (Recommended)
It's highly recommended to create a virtual environment to avoid conflicts with other Python projects.

#### For Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python dependencies using the following command:

```bash
pip install -r requirements.txt
```

### 4. Run the Application
Once the dependencies are installed, you can run the application by executing the following:

```bash
python app.py
```

This will start the Gradio app and provide a local link (e.g., `http://127.0.0.1:7860/`) where you can enter text prompts to generate images.

### 5. Interact with the Application
- Once the app is running, navigate to the provided URL.
- Enter a textual description in the input box, and click on **Submit**.
- The model will generate an image based on your description and display it on the interface.

## Requirements

The project requires the following Python libraries:

- Python 3.7+
- **PyTorch**: For running the deep learning model.
- **Gradio**: For creating the web interface.
- **Diffusers**: For working with Hugging Face diffusion models.
- **SafeTensors**: For securely loading model weights.

The dependencies are listed in `requirements.txt`, but you can install them manually using the following commands:

```bash
pip install torch>=1.10.0
pip install gradio>=3.0
pip install diffusers>=0.11.0
pip install transformers>=4.0.0
pip install safetensors>=0.2.0
```

## Project Structure

Here is an overview of the project directory:

```
project-name/
├── assets/                    # Folder for image outputs, examples, etc.
├── models/                     # Folder for any pre-trained models or weights (if they’re small enough to be included).
├── requirements.txt            # File for specifying Python dependencies.
├── app.py                      # Main script to run the app.
├── README.md                   # This file.
├── .gitignore                  # Ignore unnecessary files (e.g., virtual environments, temporary files).
└── LICENSE                     # Open-source license (e.g., MIT License).
```
---
## Collaborators
- **Devesh Punjabi** (Project Lead)
- **Sugandhi Tikkha** [GitHub Profile](https://github.com/Sugandhi30)
- **Moazzama Tufail** [GitHub Profile](https://github.com/Moazzama-Tufail)
---
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Known Issues and Limitations
- **GPU Dependency**: The model can be slow on machines without GPU acceleration. Consider running the project on a machine with a CUDA-enabled GPU for better performance.
- **Model Size**: The model might require a significant amount of RAM. Ensure your machine has at least 16 GB of RAM for optimal performance.
- **Textual Limitations**: The model may occasionally produce unexpected results depending on the input text.

## Contributions

Feel free to contribute to this project by forking the repository and submitting pull requests. If you encounter any issues or have suggestions for improvement, please create an issue on GitHub.


Thank you for using this project!

---

**Happy Image Generating!**
