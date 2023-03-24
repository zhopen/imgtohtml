import sys
import pytesseract
from PIL import Image

def convert(file_name):
    # 打开图片
    print("-----" + file_name)
    image = Image.open(file_name)
    # 进行文字识别
    text = pytesseract.image_to_string(image, lang='chi_sim')
    # 输出识别结果
    print(text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--file")
    args = p.parse_args()
    print(args.file)
    if args.file is None:
        print("missing file")
        pass
    else:
        print("--file: " + args.file)
        convert(args.file)


