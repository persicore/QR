# Generador de Códigos QR con Python

Este proyecto es un simple generador de códigos QR implementado en Python utilizando la biblioteca `qrcode`.

## Descripción

Este script de Python permite a los usuarios generar fácilmente códigos QR a partir de una URL proporcionada. Es útil para generar rápidamente códigos QR personalizados que enlacen a sitios web específicos.

## Características

- **Fácil de Usar**: Solo tienes que ejecutar el script y proporcionar la URL deseada para generar el código QR.
- **Personalización**: Puedes ajustar el tamaño del código QR, el tamaño de los cuadros y el color de fondo.
- **Versatilidad**: El código QR generado se guarda como una imagen `.png`, lo que facilita su uso en una variedad de aplicaciones y proyectos.

## Requisitos

- Python 3.x
- La biblioteca `qrcode` (se puede instalar con `pip install qrcode[pil]`)

## Uso

1. Ejecuta el script `generador_qr.py`.
2. Ingresa la URL que deseas codificar en el código QR cuando se te solicite.
3. La imagen del código QR se guardará en el directorio actual.

## Ejemplo

```bash
python generador_qr.py
