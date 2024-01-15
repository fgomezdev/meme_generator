#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enums import TextPosition
from generator import Generator


if __name__ == '__main__':
    spacer = '\n\xa0' * 3  # falsos espacios, se declaran en la variable para evitar problemas con interrogate.
    params = [
        {
            'input_image_path': './src/blank_images/risa_leo.png',
            'alias': 'leo',
            'first_text': f'Ticket #9999:{spacer}.',
            'first_text_orientation': TextPosition.BOTTOM_LEFT,
            'second_text': 'Documentación técnica',
            'second_text_orientation': TextPosition.BOTTOM_LEFT,
        },
        {
            'input_image_path': './src/blank_images/sudor.jpg',
            'alias': 'sudor',
            'first_text': 'El sprint\ncierra mañana',
            'first_text_orientation': TextPosition.MIDDLETOP_RIGHT,
        },
        {
            'input_image_path': './src/blank_images/drake.jpg',
            'alias': 'drake',
            'first_text': '\nDocumentar\ncon\nGoogle Docs...',
            'first_text_orientation': TextPosition.MIDDLETOP_RIGHT,
            'second_text': 'Hay otra\nmanera...',
            'second_text_orientation': TextPosition.MIDDLEBOTTOM_RIGHT,
            'text_color': (0, 0, 0),
            'border_color': (55, 255, 205),
        },
        {
            'input_image_path': './src/blank_images/chinito.jpg',
            'alias': 'chinito',
            'first_text': 'Sphinx!',
            'first_text_orientation': TextPosition.BOTTOM_CENTER,
        },
        {
            'input_image_path': './src/blank_images/bla_bla.jpg',
            'alias': 'bla',
            'first_text': 'Igual tengo\nque documentar...',
            'first_text_orientation': TextPosition.BOTTOM_CENTER,
        },
        {
            'input_image_path': './src/blank_images/winnie_pooh.png',
            'alias': 'drake',
            'first_text': '\n...sí, hay que\ndocumentar...',
            'first_text_orientation': TextPosition.MIDDLETOP_RIGHT,
            'second_text': '\nPero gran parte\nse genera\nautomáticamente',
            'second_text_orientation': TextPosition.MIDDLEBOTTOM_RIGHT,
            'text_color': (0, 0, 0),
            'border_color': (55, 255, 205),
        },
        {
            'input_image_path': './src/blank_images/think_about_it.jpg',
            'alias': 'think',
            'first_text': 'No te olvides de\nlos DocStrings...',
            'first_text_orientation': TextPosition.TOP_RIGHT,
        },
        {
            'input_image_path': './src/blank_images/exito.webp',
            'alias': 'exito',
            'first_text': '¡Documentación lista!',
            'first_text_orientation': TextPosition.TOP_CENTER,
        },
        {
            'input_image_path': './src/blank_images/mr_incredible.jpg',
            'alias': 'gracias',
            'first_text': '¡Gracias!',
            'first_text_orientation': TextPosition.BOTTOM_CENTER,
        },        
    ]

    _generator = Generator()
    # _generator.FONT_SIZE = 25
    for i, param in enumerate(params):
        param['alias'] = f"{i}_{param['alias']}"
        _generator.generate_meme(**param)
