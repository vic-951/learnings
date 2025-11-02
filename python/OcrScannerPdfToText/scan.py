import os
import sys
from pdf2image import convert_from_path
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import argparse
import time

def preprocess_image(image):
    if image.mode != 'L':
        image = image.convert('L')
    
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(2.5)

    image = image.filter(ImageFilter.MedianFilter())
    
    return image

def pdf_to_text_optimized(pdf_path, language='en', dpi=300, page_range=None):
    """
    Args:
        pdf_path (str): path to pdf file
        language (str): language for OCR (musst be installed with tesseract)
        dpi (int): Resolution for pdf
        page_range (tuple): sites to scan (start, end) or None for all
    
    Returns:
        str: extracted text
    """
    try:
        print(f"Convert PDF with {dpi} DPI...")
        print(f"Language: {language}")
        
        if page_range:
            pages = convert_from_path(pdf_path, dpi=dpi, fmt='jpeg', 
                                    first_page=page_range[0], last_page=page_range[1])
        else:
            pages = convert_from_path(pdf_path, dpi=dpi, fmt='jpeg')
        
        full_text = ""
        total_pages = len(pages)
        
        print(f"Processing {total_pages} pages...")
        
        start_time = time.time()
        
        for i, page in enumerate(pages):
            print(f"Processed page {i+1}/{total_pages}")
            processed_page = preprocess_image(page)

            custom_config = r'--oem 1 --psm 6 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:!?()[]{}\'-_/\\@#$%&*+<>=|~^`'

            text = pytesseract.image_to_string(
                processed_page, 
                lang=language,
                config=custom_config
            )
            
            full_text += text + "\n\n"
            
        end_time = time.time()
        print(f"Processing time: {end_time - start_time:.2f} seconds")
            
        return full_text
    
    except Exception as e:
        return f"Error while scanning: {str(e)}"

def save_text_to_file(text, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Text was saved in: {output_path}")
    except Exception as e:
        print(f"Error while saving file: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='PDF OCR Scanner')
    parser.add_argument('pdf_path', help='path to your pdf file')
    parser.add_argument('-l', '--language', default='deu', 
                       help='language for OCR (deu, eng, fra, spa, ita, por)')
    parser.add_argument('-o', '--output', help='output-file (optional)')
    parser.add_argument('-d', '--dpi', type=int, default=300, 
                       help='Resolution in DPI (Standard: 300)')
    parser.add_argument('--pages', nargs=2, type=int, metavar=('START', 'END'),
                       help='Pages (z.B. --pages 1 5)')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.pdf_path):
        print(f"Error: PDF-File '{args.pdf_path}' not found")
        sys.exit(1)
    
    # Führe optimierte OCR durch
    print("Start scanning...")
    print("="*60)
    
    if args.pages:
        print(f"Processed Pages {args.pages[0]}-{args.pages[1]}")
        text = pdf_to_text_optimized(args.pdf_path, args.language, args.dpi, args.pages)
    else:
        text = pdf_to_text_optimized(args.pdf_path, args.language, args.dpi)
    
    print("="*60)
    
    if args.output:
        save_text_to_file(text, args.output)
    else:
        print("\nYour Text:")
        print("-"*60)
        # If you want to show the text of PDF-File in your Terminal, uncomment this line
        #print(text)
        print("-"*60)

if __name__ == "__main__":
    main()
