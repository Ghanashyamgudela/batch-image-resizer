import os
from PIL import Image

def batch_resize(
    input_dir="images_input",
    output_dir="images_output",
    max_size=(800, 800),
    output_format=None
):
   
    os.makedirs(output_dir, exist_ok=True)
    
    valid_ext = (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff")
    
    for file in os.listdir(input_dir):
        if not file.lower().endswith(valid_ext):
            continue
        
        in_path = os.path.join(input_dir, file)
        
        try:
            with Image.open(in_path) as img:
              
             img = img.resize(max_size, Image.LANCZOS)

                
               
            base = os.path.splitext(file)[0]
            ext = output_format.lower() if output_format else img.format.lower()
            out_path = os.path.join(output_dir, f"{base}.{ext}")
            
       
            img.save(out_path, output_format if output_format else img.format)
            print(f"✅ {file} → {out_path}")
    
        except Exception as e:
            print(f"❌ Error with {file}: {e}")

print("\n🎯 Batch processing complete!")


if __name__ == "__main__":
    batch_resize(
        input_dir="images_input",   
        output_dir="images_output", 
        max_size=(800, 800),         
        output_format="JPEG"         
    )
