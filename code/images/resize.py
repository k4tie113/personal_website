from PIL import Image
import os

# Folder where images are stored
image_folder = ""
output_folder = "resized"  # Save resized images here

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)

# List of images to resize and rename
image_files = ["cavern.png", "dessert.jpg", "dungeon.png", "fashion.png", "lakesunset.png", "shattered.png"]

# Target size (adjust as needed)
new_size = (400, 300)  # Resize to 300x300 pixels

for filename in image_files:
    input_path = os.path.join(image_folder, filename)
    
    # Generate output filename (e.g., cavern2.png)
    name, ext = os.path.splitext(filename)
    output_filename = f"{name}2{ext}"  # Add "2" before extension
    output_path = os.path.join(output_folder, output_filename)

    try:
        # Open and resize the image
        img = Image.open(input_path)
        img = img.resize(new_size, Image.LANCZOS)  # Replace ANTIALIAS with LANCZOS
        img.save(output_path)

        print(f"✅ Resized: {filename} → {output_filename}")
    
    except FileNotFoundError:
        print(f"❌ Error: {filename} not found. Check file paths.")
    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")

print("✅ All images processed!")
