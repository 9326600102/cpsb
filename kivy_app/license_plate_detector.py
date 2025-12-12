import cv2
import numpy as np
import re
import os

# 尝试导入pytesseract，如果失败则使用替代方案
try:
    import pytesseract
    # 在安卓上，Tesseract的路径可能需要调整
    # 可以通过buildozer.spec文件配置TESSDATA_PREFIX环境变量
    pytesseract_available = True
except ImportError:
    pytesseract_available = False

class LicensePlateDetector:
    def __init__(self):
        self.pytesseract_available = pytesseract_available
    
    def preprocess_image(self, image):
        """预处理图像以提高车牌识别率"""
        # 转换为灰度图
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # 应用高斯模糊去除噪声
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # 使用自适应阈值进行二值化
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        
        # 应用形态学操作（膨胀和腐蚀）来增强字符
        kernel = np.ones((3, 3), np.uint8)
        morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        
        return morph
    
    def detect_license_plate(self, image):
        """检测图像中的车牌区域"""
        # 预处理图像
        processed = self.preprocess_image(image)
        
        # 查找轮廓
        contours, _ = cv2.findContours(processed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # 筛选可能的车牌轮廓
        license_plate_contour = None
        for contour in contours:
            # 计算轮廓的周长
            perimeter = cv2.arcLength(contour, True)
            
            # 近似轮廓为多边形
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            
            # 检查是否为四边形
            if len(approx) == 4:
                # 计算轮廓的面积和宽高比
                area = cv2.contourArea(contour)
                x, y, w, h = cv2.boundingRect(approx)
                aspect_ratio = w / float(h)
                
                # 车牌的宽高比通常在2:1到5:1之间
                if 2.0 < aspect_ratio < 5.0 and area > 1000:
                    license_plate_contour = approx
                    break
        
        if license_plate_contour is None:
            return None
        
        # 获取车牌区域的坐标
        x, y, w, h = cv2.boundingRect(license_plate_contour)
        license_plate = image[y:y+h, x:x+w]
        
        return license_plate, (x, y, w, h)
    
    def recognize_license_plate(self, license_plate_image):
        """识别车牌上的文字"""
        if not self.pytesseract_available:
            return "OCR不可用，请安装pytesseract"
        
        try:
            # 预处理车牌图像
            processed_plate = self.preprocess_image(license_plate_image)
            
            # 使用Tesseract OCR识别文字
            # 配置Tesseract只识别字母和数字
            config = '--psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            text = pytesseract.image_to_string(processed_plate, config=config)
            
            # 清理识别结果，只保留字母和数字
            cleaned_text = re.sub(r'[^A-Z0-9]', '', text)
            
            return cleaned_text
        except Exception as e:
            return f"OCR识别错误: {str(e)}"
    
    def process_image(self, image):
        """处理图像并识别车牌"""
        if image is None:
            return None, None, "无法读取图像"
        
        # 检测车牌
        result = self.detect_license_plate(image)
        
        if result is None:
            return image, None, "未检测到车牌"
        
        license_plate, (x, y, w, h) = result
        
        # 识别车牌文字
        license_text = self.recognize_license_plate(license_plate)
        
        if len(license_text) < 5 and "OCR不可用" not in license_text:
            return image, None, "车牌识别失败"
        
        # 在原始图像上绘制边框
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(image, license_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        return image, license_plate, license_text