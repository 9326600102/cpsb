import cv2
from license_plate_detector import LicensePlateDetector
import os

# 创建车牌检测器实例
detector = LicensePlateDetector()

# 测试图像路径（用户需要替换为自己的测试图像路径）
test_image_path = "test_car.jpg"

# 检查图像是否存在
if not os.path.exists(test_image_path):
    print(f"测试图像不存在: {test_image_path}")
    print("请将测试图像命名为'test_car.jpg'并放在当前目录下")
    exit(1)

# 读取测试图像
image = cv2.imread(test_image_path)

if image is None:
    print(f"无法读取测试图像: {test_image_path}")
    exit(1)

print("开始检测车牌...")

# 处理图像并识别车牌
result_image, license_plate, license_text = detector.process_image(image)

# 显示结果
print(f"识别结果: {license_text}")

# 保存结果图像
cv2.imwrite("result.jpg", result_image)
print("结果图像已保存为: result.jpg")

# 如果检测到车牌，保存车牌图像
if license_plate is not None:
    cv2.imwrite("license_plate.jpg", license_plate)
    print("车牌图像已保存为: license_plate.jpg")

print("测试完成!")