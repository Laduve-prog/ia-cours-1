from src.image_processor import ImageProcessor


def main():
    # Constants for input and output directories and image size
    INPUT_FOLDER = "input_folder"
    OUTPUT_FOLDER = "datasets"
    IMAGE_SIZE = (256, 256)

    processor = ImageProcessor(INPUT_FOLDER, OUTPUT_FOLDER, IMAGE_SIZE)
    processor.process_folder(target_size=640)


if __name__ == "__main__":
    main()
