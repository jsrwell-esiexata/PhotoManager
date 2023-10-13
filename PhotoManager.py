from typing import Any
import requests
from PIL import Image
import io
import base64


class PhotoManager:
    """
    Class that allows connecting to a URL and manipulating images in memory.

    Enables connecting to a URL, saving, encoding in base64, decoding from
    base64, converting to JPEG, and compressing images.
    """

    def __init__(self, name: str, image: Any = None):
        """Initialize the class instance with a name."""

        self.name = name
        self.image = image
        self.croped_image = None

    def get_image(self) -> Any:
        """Return the image."""

        return self.image

    def get_croped_image(self) -> Any:
        """Return the croped image."""

        return self.cropped_image

    def set_image_as_str(self, image_str: str) -> None:
        """Set an image like base64 in str for example."""

        self.image = image_str

    def connect_to_url(self, url: str) -> None:
        """
        Connect to a URL, retrieve the image, and store it in the instance.

        :param url: The URL of the image to connect to.
        """

        try:
            response = requests.get(url)
            response.raise_for_status()
            self.image = response.content

        except requests.exceptions.RequestException as e:
            print(f"Error connecting to URL: {e}")

    def save_image(self, file_path: str) -> None:
        """
        Save the image to a file at the specified path.

        :param file_path: The path where the image will be saved.
        """

        if self.image:
            try:
                if isinstance(self.image, bytes):
                    with open(f'{file_path}{self.name}.jpeg', 'wb') as f:
                        f.write(self.image)

                elif isinstance(self.image, Image.Image):
                    self.image.save(f'{file_path}{self.name}.jpeg')

                else:
                    print("Unsupported image type")

            except (IOError, ValueError) as e:
                print(f"Error saving the image: {e}")

    def save_croped_image(self, file_path: str) -> None:
        """
        Save the croped image to a file at the specified path.

        :param file_path: The path where the croped image will be saved.
        """

        if self.cropped_image:
            try:
                if isinstance(self.cropped_image, bytes):
                    with open(f'{file_path}{self.name}.jpeg', 'wb') as f:
                        f.write(self.cropped_image)

                elif isinstance(self.cropped_image, Image.Image):
                    self.cropped_image.save(f'{file_path}{self.name}.jpeg')

                else:
                    print("Unsupported image type")

            except (IOError, ValueError) as e:
                print(f"Error saving the croped image: {e}")

    def to_base64(self) -> None:
        """
        Convert the image to base64 and store it in the instance.
        """

        if self.image:
            try:
                if not isinstance(self.image, Image.Image):
                    # Convert bytes to PIL.Image.Image
                    self.image = Image.open(io.BytesIO(self.image))

                buffered = io.BytesIO()
                self.image.save(buffered, format="JPEG")
                self.image = base64.b64encode(buffered.getvalue()).decode()

            except (IOError, ValueError) as e:
                print(f"Error converting to base64: {e}")

    def from_base64(self) -> None:
        """
        Decode the image from base64 and store it in the instance.
        """

        try:
            image_data = base64.b64decode(self.image)
            self.image = Image.open(io.BytesIO(image_data))

        except (IOError, ValueError) as e:
            print(f"Error decoding from base64: {e}")

    def to_jpeg(self) -> None:
        """
        Convert the image to JPEG format and store it in the instance.
        """

        if self.image:
            try:
                if not isinstance(self.image, Image.Image):
                    # Convert bytes to PIL.Image.Image
                    self.image = Image.open(io.BytesIO(self.image))

                buffered = io.BytesIO()
                self.image.save(buffered, format="JPEG")
                self.image = buffered.getvalue()

            except (IOError, ValueError) as e:
                print(f"Error converting to JPEG: {e}")

    def compress_image(self, quality: int = 85) -> None:
        """
        Compress the image in JPEG format with the specified quality.

        :param quality: The quality of compression (0-100).
        """

        if self.image:
            try:
                if not isinstance(self.image, Image.Image):
                    # Convert bytes to PIL.Image.Image
                    self.image = Image.open(io.BytesIO(self.image))

                buffered = io.BytesIO()
                self.image.save(buffered, format="JPEG", quality=quality)
                self.image = buffered.getvalue()

            except (IOError, ValueError) as e:
                print(f"Error compressing the image: {e}")

    def relative_crop(self,
                      top: float,
                      right: float,
                      bottom: float,
                      left: float) -> None:
        """
        Crop the image based on relative percentage coordinates.

        :param top: Percentage of the top edge (0-100).
        :param right: Percentage of the right edge (0-100).
        :param bottom: Percentage of the bottom edge (0-100).
        :param left: Percentage of the left edge (0-100).
        """
        if self.image:
            try:
                if not isinstance(self.image, Image.Image):
                    # Convert bytes or base64 to PIL.Image.Image
                    if isinstance(self.image, str):
                        image_data = base64.b64decode(self.image)
                        self.cropped_image = Image.open(io.BytesIO(image_data))
                    else:
                        self.cropped_image = Image.open(io.BytesIO(self.image))

                # Get image dimensions
                width, height = self.cropped_image.size

                # Calculate pixel coordinates based on percentages
                left_pixel = int(left * width / 100)
                right_pixel = int(right * width / 100)
                top_pixel = int(top * height / 100)
                bottom_pixel = int(bottom * height / 100)

                # Crop the image
                self.cropped_image = self.cropped_image.crop(
                    (left_pixel, top_pixel, right_pixel, bottom_pixel))

                # Save the cropped image as JPEG
                buffered = io.BytesIO()
                self.cropped_image.save(buffered, format="JPEG")
                self.cropped_image = buffered.getvalue()

            except (IOError, ValueError) as e:
                print(f"Error cropping the image: {e}")


# =============================================================================
# ============================EXEMPLOS=DE=USO==================================
# =============================================================================
# Origem e destino da imagem
# =============================================================================
origin_image = "https://images.alphacoders.com/601/601059.jpg"
save_path = "/media/jsrwell/1234-5678/"  # Insira o diretório destino da imagem

# =============================================================================
# Instância e conexão obtendo a imagem
# =============================================================================
photo_manager = PhotoManager("giant-image")
photo_manager.connect_to_url(origin_image)

# =============================================================================
# Apenas para exemplo de conversão para base64 e retorno
# =============================================================================
photo_manager.to_base64()
photo_manager.from_base64()

# =============================================================================
# Compreesõ em 50%
# =============================================================================
photo_manager.compress_image(50)

# =============================================================================
# Salvando a imagem original
# =============================================================================
photo_manager.save_image(f"{save_path}original-")

# =============================================================================
# Localizando as 3 faces com base na imagem original e salvando elas
# =============================================================================
photo_manager.relative_crop(top=5, right=55, bottom=17, left=50)
photo_manager.save_croped_image(f"{save_path}face1-")
photo_manager.relative_crop(top=0, right=24, bottom=24, left=8)
photo_manager.save_croped_image(f"{save_path}face2-")
photo_manager.relative_crop(top=3, right=82, bottom=10, left=77)
photo_manager.save_croped_image(f"{save_path}face3-")
