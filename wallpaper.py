def get_wallpapers():
    images = []
    # Get EVERY image from root
    for ext in ["*.jpg","*.jpeg","*.png","*.webp","*.JPG","*.JPEG","*.PNG"]:
        images += glob.glob(ext)
    # Also check subfolders
    for folder in ["static","static/wallpapers","wallpapers"]:
        if os.path.exists(folder):
            for ext in ["*.jpg","*.jpeg","*.png","*.webp","*.JPG","*.JPEG","*.PNG"]:
                images += glob.glob(f"{folder}/{ext}")
    # Remove duplicates and sort newest first
    images = sorted(set(images), reverse=True)
    return images
