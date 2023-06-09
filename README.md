# imgtohtml
# 推荐最好的OCR python库
有许多优秀的OCR Python库可供选择，以下是其中一些：

Tesseract-OCR：Tesseract-OCR 是 Google 开发的一个开源 OCR 引擎，可以通过 Python 绑定来使用。Tesseract-OCR 可以识别多种语言，包括英语、中文等。安装后，可以使用 pytesseract 库调用 Tesseract-OCR。

OCRopus：OCRopus 是一个OCR 引擎和文本识别框架，它可以通过Python访问，支持多种OCR任务，例如文本线定位、文本分割、文本识别等。

Kraken：Kraken 是一个OCR 引擎，支持多种OCR任务，包括文本行定位、文本分割和文本识别等。Kraken 同样可以通过Python访问。

EasyOCR：EasyOCR 是一个基于深度学习的OCR库，它可以识别多种语言，并且具有较高的识别准确率。

OpenCV：OpenCV 是一个计算机视觉库，可以用于图像处理和识别。它可以通过 Python 访问，并提供了一些 OCR 功能，如字符识别等。

这些库各有特点，选择适合自己需求的库即可。
 


# 介绍下Tesseract-OCR怎么用
Tesseract-OCR 是一个开源 OCR 引擎，可以通过 Python 绑定来使用。在使用 Tesseract-OCR 之前，需要先安装 Tesseract-OCR 和 pytesseract 库。

安装 Tesseract-OCR：

对于 Windows 系统，可以从 Tesseract-OCR 官方网站 https://github.com/UB-Mannheim/tesseract/wiki 下载安装程序，并将安装路径添加到环境变量 PATH 中。
对于 Linux 系统，可以通过包管理器安装 Tesseract-OCR。
安装 pytesseract 库：
使用 pip 命令安装：

Copy code
pip install pytesseract
安装完成后，就可以使用 pytesseract 库来调用 Tesseract-OCR 进行文字识别了。

以下是一个使用 pytesseract 库进行图片文字识别的例子：

```
import pytesseract
from PIL import Image

# 打开图片
image = Image.open('test.png')

#
3进行文字识别
text = pytesseract.image_to_string(image, lang='eng')

# 输出识别结果
print(text)
```
在上面的例子中，image_to_string() 函数将打开的图片对象和识别语言作为参数，返回识别的文本结果。可以将识别结果输出到控制台或保存到文件中。

需要注意的是，Tesseract-OCR 对图片质量、字体等有一定的要求，如果图片质量过差或字体过于复杂，识别准确率可能会降低。



