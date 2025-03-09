
# Script2Sceen (Text-to-Image Generation) 

This project utilizes the **Playground AI aesthetic model** (DeepFloyd IF) to generate high-quality images based on textual prompts. The model is integrated with the **Gradio** library to provide an interactive user interface for easy text-to-image generation.

The project is designed to run efficiently, utilizing GPU resources when available, and provides users with a seamless and intuitive way to create custom images based on their input.

## Features
- **Text-to-Image Generation**: Generate high-quality images from text descriptions using the DeepFloyd IF model.
- **Optimized for GPU**: The model uses mixed precision for better performance on compatible GPUs.
- **Interactive Interface**: A simple and user-friendly interface powered by Gradio that allows users to input text and see the generated image.
- **SafeTensors Support**: The model weights are loaded in SafeTensors format for better safety and performance.

## Model Details
- **Model Name**: Playground AI aesthetic model (`playgroundai/playground-v2-1024px-aesthetic`).
- **Pre-trained Model**: This project uses the pre-trained model from the **Hugging Face** model hub, specifically fine-tuned for aesthetic image generation.
- **Optimized for GPU**: Mixed-precision and SafeTensors format are used to optimize model loading and performance on GPUs.

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

- Python 3.x
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
```
