from PIL import Image

def show_data(image_path, description):
    """
    Used to show final data that goes on Instagram
    
    Use this for testing instead of posting on Instagram
    """
    print(f"""
    Image path: {image_path}

    image description: {description}
    """)
    Image.open(image_path)