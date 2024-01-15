import os
from io import BytesIO
import requests
from PIL import Image, ImageDraw, ImageFont

from enums import TextPosition


class Generator:
    """prueba"""
    OUTPUT_DIR = './src/memes'
    TEXT_COLOR = (255, 255, 255)
    BORDER_COLOR = (0, 0, 0)
    BORDER_SIZE = 5
    # FONT = 'comic.ttf'
    FONT = 'impact.ttf'
    FONT_SIZE = None

    def _get_image(self, url_or_path: str) -> Image:

        source_image: str | BytesIO

        try:
            if url_or_path.startswith('http'):
                response = requests.get(url_or_path)
                response.raise_for_status()
                source_image = BytesIO(response.content)
            else:
                source_image = url_or_path

            image = Image.open(source_image)
            return image
        except requests.exceptions.RequestException:
            raise Exception('Error al consultar la url solicitada')
        except (IOError, OSError):
            raise Exception('Error al abrir la imagen')

    def _draw_text(
        self,
        image_draw_object: ImageDraw,
        text_position: tuple,
        text: str,
        font: ImageFont,
        text_color: tuple,
        border_color: tuple,
        border_size: int,
    ):

        if not text:
            return

        # Dibujamos el texto
        image_draw_object.text(text_position, text, font=font, fill=border_color)

        # Dibujamos el contorno del texto
        image_draw_object.text(
            (text_position[0] - border_size, text_position[1] - border_size),
            text,
            font=font,
            fill=text_color,
        )

    def _get_text_position(
        self,
        image_width: int,
        image_heigth: int,
        text: str,
        font: ImageFont,
        text_position: TextPosition = TextPosition.TOP_RIGHT,
    ) -> tuple:

        max_line_width = 0
        line_height = 0
        text_lines = f'{text}'.strip().split('\n')
        if len(text_lines) > 0:
            for line in text_lines:
                bbox = font.getmask(line).getbbox()
                if bbox:
                    line_height = bbox[3]
                    line_width = bbox[2]
                    if line_width > max_line_width:
                        max_line_width = line_width

        # Posicion Horizontal
        if text_position in (
            TextPosition.TOP_LEFT,
            TextPosition.MIDDLETOP_LEFT,
            TextPosition.MIDDLE_LEFT,
            TextPosition.MIDDLEBOTTOM_LEFT,
            TextPosition.BOTTOM_LEFT,
        ):
            text_x = 20
        elif text_position in (
            TextPosition.TOP_CENTER,
            TextPosition.MIDDLETOP_CENTER,
            TextPosition.MIDDLE_CENTER,
            TextPosition.MIDDLEBOTTOM_CENTER,
            TextPosition.BOTTOM_CENTER,
        ):
            text_x = (image_width - max_line_width) // 2
        elif text_position in (
            TextPosition.TOP_RIGHT,
            TextPosition.MIDDLETOP_RIGHT,
            TextPosition.MIDDLE_RIGHT,
            TextPosition.MIDDLEBOTTOM_RIGHT,
            TextPosition.BOTTOM_RIGHT,
        ):
            text_x = image_width - max_line_width - 20
        else:
            text_x = 20

        # Posicion Vertical
        if text_position in (
            TextPosition.TOP_LEFT,
            TextPosition.TOP_CENTER,
            TextPosition.TOP_RIGHT,
        ):
            text_y = 0
        elif text_position in (
            TextPosition.MIDDLETOP_LEFT,
            TextPosition.MIDDLETOP_CENTER,
            TextPosition.MIDDLETOP_RIGHT,
        ):
            text_y = image_heigth // 4 - line_height * len(text_lines)
        elif text_position in (
            TextPosition.MIDDLE_LEFT,
            TextPosition.MIDDLE_CENTER,
            TextPosition.MIDDLE_RIGHT,
        ):
            text_y = image_heigth // 2 - line_height * len(text_lines)
        elif text_position in (
            TextPosition.MIDDLEBOTTOM_LEFT,
            TextPosition.MIDDLEBOTTOM_CENTER,
            TextPosition.MIDDLEBOTTOM_RIGHT,
        ):
            text_y = image_heigth // 4 * 3 - line_height * len(text_lines)
        elif text_position in (
            TextPosition.BOTTOM_LEFT,
            TextPosition.BOTTOM_CENTER,
            TextPosition.BOTTOM_RIGHT,
        ):
            text_y = image_heigth - ((line_height + 15) * len(text_lines))
        else:
            text_y = 0

        return text_x, text_y

    def generate_meme(
        self,
        input_image_path: str,
        output_image_path: str = '',
        alias: str = '',
        first_text: str = '',
        first_text_orientation: TextPosition = TextPosition.TOP_RIGHT,
        second_text: str = '',
        second_text_orientation: TextPosition = TextPosition.BOTTOM_RIGHT,
        text_color: tuple = TEXT_COLOR,
        border_color: tuple = BORDER_COLOR,
        border_size: int = BORDER_SIZE,
    ):
                
        if not first_text and not second_text:
            raise Exception('Debes especificar al menos un texto')

        try:
            input_image = self._get_image(input_image_path)
        except Exception as ex:
            print(str(ex))
            return

        if not output_image_path:
            if alias:
                output_filename = alias
            else:
                output_filename = (second_text or first_text).replace('\n', '_').replace(' ', '_').lower()
            output_image_path = f'{self.OUTPUT_DIR}/{output_filename}.jpg'

        # Obtener el ancho y alto de la imagen
        width, height = input_image.size

        # Crear un objeto de dibujo
        draw = ImageDraw.Draw(input_image)

        # Utilizar una fuente predeterminada (puedes cambiar la fuente si lo deseas)
        font = ImageFont.load_default()

        # Configurar el tamaño de la fuente según los grupos de texto
        if first_text and second_text:
            font_size_coef = 14
        else:
            font_size_coef = 10

        font_size = self.FONT_SIZE or min(width, height) // font_size_coef

        try:
            font = ImageFont.truetype(self.FONT, font_size)
        except:  # noqa E722
            print('No se pudo cargar la fuente especificada, se usará la fuente por defecto')
            font = ImageFont.load_default(font_size)

        first_text_position = self._get_text_position(width, height, first_text, font, first_text_orientation)
        second_text_position = self._get_text_position(width, height, second_text, font, second_text_orientation)

        right_oriented = [
            TextPosition.TOP_RIGHT,
            TextPosition.BOTTOM_RIGHT,
            TextPosition.MIDDLE_RIGHT,
            TextPosition.MIDDLETOP_RIGHT,
            TextPosition.MIDDLEBOTTOM_RIGHT,
        ]

        # En caso de estar orientados a la derecha redefinimos la posicion
        # horizontal de ambos textos según el que este más a la izquierda
        if first_text_orientation in right_oriented and second_text_orientation in right_oriented:
            text_x = min(first_text_position[0], second_text_position[0])
            first_text_position = (text_x, first_text_position[1])
            second_text_position = (text_x, second_text_position[1])

        border_size = min(border_size, 10)
        self._draw_text(
            draw,
            first_text_position,
            first_text,
            font,
            text_color,
            border_color,
            border_size,
        )
        self._draw_text(
            draw,
            second_text_position,
            second_text,
            font,
            text_color,
            border_color,
            border_size,
        )

        # Si no existe el directorio, lo creamos
        directorio = os.path.dirname(output_image_path)
        if not os.path.exists(directorio):
            os.makedirs(directorio)

        input_image.save(output_image_path)
        print(f'Meme generado: {output_image_path}')
