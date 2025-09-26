import os
import photo as ph

image_path = r"E:\my works\Code\Machine Vision\1\2.jpg"
output_path = r"E:\my works\Code\Machine Vision\1\output2.jpg"

if os.path.exists(image_path):
    print("✅ Image found ")
    x = ph.photoshop(image_path)
    x.RGB(r=2, g=1, b=0, save=True, path=output_path)
    print("✅ Output saved", output_path)
else:
    print("❌ Image NOT found", image_path)