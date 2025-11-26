import shutil
import os

sources = [
    ("/Users/danielburke/Downloads/Hibernia Ballykeeran 2019 10 19.jpg", "hibernia.jpg"),
    ("/Users/danielburke/Downloads/ESB1.jpg", "ESB1.jpg"),
    ("/Users/danielburke/Downloads/ESB2.jpg", "ESB2.jpg")
]
dest_dir = "/Users/danielburke/Documents/repositories/hugo/bargehibernia/pelican_site/content/images/vessels"

with open("copy_log.txt", "w") as f:
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            f.write(f"Created {dest_dir}\n")
        
        for src, dst_name in sources:
            if os.path.exists(src):
                dst = os.path.join(dest_dir, dst_name)
                try:
                    shutil.copy2(src, dst)
                    f.write(f"Copied {src} to {dst}\n")
                except Exception as e:
                    f.write(f"Error copying {src}: {e}\n")
            else:
                f.write(f"Source not found: {src}\n")
                # Try to list dir to see what is there
                d = os.path.dirname(src)
                if os.path.exists(d):
                    # f.write(f"Listing {d}:\n")
                    # f.write(str(os.listdir(d)) + "\n")
                    pass
    except Exception as e:
        f.write(f"Global error: {e}\n")
