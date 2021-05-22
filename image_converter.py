import sys
import os
import shutil
from PIL import Image

class CLI:
    def __init__(self, img_dir):
        self.cnvrsnDir = os.path.join(img_dir, 'Converted Images')
        self.img_dir = img_dir
        self.image_files = []
        self.image_extentions = ['png', 'jpeg', 'webp', 'jpg']
    
    def clear_cache(self):
        # Clear old converted files
        if os.path.exists(self.cnvrsnDir):
            shutil.rmtree(self.cnvrsnDir)
            os.mkdir(self.cnvrsnDir)
        else:
            os.mkdir(self.cnvrsnDir)

    def get_images(self):
        self.clear_cache()
        
        for root, dirs, files in os.walk(img_dir):
            for file in files:
                for ie in self.image_extentions:
                    if file.endswith(f'.{ie}'):
                        self.image_files.append(
                            {
                                'dir': os.path.join(root, file),
                                'ext': ie,
                                'cnvDir': os.path.join(
                                    root.replace(img_dir, self.cnvrsnDir),
                                    file
                                )
                            })

    def convert(self, ext):
        self.get_images()

        imageConverted = 0
        totalImages = len(self.image_files)
        
        for img in self.image_files:
            IMG = Image.open(img['dir']).convert('RGB')
            new_img = img['cnvDir'].replace(img['ext'], ext.lower())
            IMG.save(new_img, ext)
            imageConverted += 1
            print(f"Converted {imageConverted} / {totalImages} images to {new_img}")


if __name__ == "__main__":
    img_dir = sys.argv[1]
    ext = sys.argv[2]
    cli = CLI(img_dir)
    try:
        cli.convert(ext)
    except KeyError:
        print(ext, "is not supported!")
    except Exception as e:
        print("Error: ", e)
    
        
