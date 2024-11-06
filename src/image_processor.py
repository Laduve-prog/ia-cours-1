from datetime import datetime

from PIL import Image, ImageOps
import os
from typing import Tuple


class ImageProcessor:
    def __init__(
        self,
        input_folder: str,
        output_folder: str,
        image_size: Tuple[int, int],
    ):
        """
        Initializes the ImageProcessor with input and output folders and target image size.

        :param input_folder: Path to the folder containing input images.
        :param output_folder: Path to the folder where processed images will be saved.
        :param image_size: Target size (width, height) for each image after processing.
        """
        self.input_folder = input_folder
        timestamp = datetime.now().strftime(("%Y%m%d%H%M%S"))
        self.output_folder = os.path.join(output_folder, timestamp)
        self.image_size = image_size
        os.makedirs(
            self.output_folder, exist_ok=True
        )  # Create the output folder if it doesn't exist

    def process_image(self, image_path: str, target_size: int) -> Image:
        """
        Opens an image, resizes it to fit the target size, and adds padding if necessary.

        :param image_path: Path to the input image.
        :return: The processed Image object, or None if an error occurs.
        """
        try:
            # Ouvre l'image
            image = Image.open(image_path)
            # Calcul du ratio pour le redimensionnement en conservant l'aspect
            width, height = image.size
            if width != height:
                # Redimensionne en conservant le ratio, puis applique le padding
                if width > height:
                    new_height = int(target_size * (height / width))
                    resized_image = image.resize(
                        (target_size, new_height),
                    )
                    # Ajoute du padding en bas si nécessaire
                    padded_image = ImageOps.expand(
                        resized_image,
                        border=(0, 0, 0, target_size - new_height),
                        fill=(114, 114, 144),
                    )
                else:
                    new_width = int(target_size * (width / height))
                    resized_image = image.resize(
                        (new_width, target_size),
                    )
                    # Ajoute du padding à droite si nécessaire
                    padded_image = ImageOps.expand(
                        resized_image,
                        border=(0, 0, target_size - new_width, 0),
                        fill=(114, 114, 144),
                    )
            else:
                # Redimensionne directement si déjà carré
                padded_image = image.resize((target_size, target_size))

            return padded_image
        except Exception as e:
            print(f"Error processing image {image_path}: {e}")
            return None

    def process_folder(self, target_size: int) -> None:
        """
        Processes all images in the input folder by resizing and adding padding, then saves them to the output folder.
        """
        for filename in os.listdir(self.input_folder):
            file_path = os.path.join(self.input_folder, filename)
            # Check if the file is an image with a supported extension
            if os.path.isfile(file_path) and filename.lower().endswith(
                (".png", ".jpg", ".jpeg")
            ):
                processed_image = self.process_image(file_path, target_size)
                if processed_image:
                    # Save the processed image in the output directory
                    output_path = os.path.join(self.output_folder, filename)
                    processed_image.save(output_path)
                    print(
                        f"Image {filename} processed and saved in {self.output_folder}"
                    )
                else:
                    print(
                        f"Skipping image {filename} due to processing error."
                    )
