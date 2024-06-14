
from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size=(216,216)):
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    for image_file in image_files:
        
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)

        with Image.open(input_path) as img:
            
            resized_img = img.resize(target_size)

            
            resized_img.save(output_path)

if __name__ == "__main__":
    input_folder = "Data"
    output_folder = "Data"
    resize_images(input_folder, output_folder)
