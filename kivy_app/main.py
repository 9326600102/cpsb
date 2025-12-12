from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import numpy as np
from license_plate_detector import LicensePlateDetector
import os

class LicensePlateApp(App):
    def build(self):
        # 创建主布局
        self.layout = BoxLayout(orientation='vertical')
        
        # 创建相机组件
        self.camera = Camera(play=True, resolution=(640, 480))
        self.layout.add_widget(self.camera)
        
        # 创建结果标签
        self.result_label = Label(text='点击拍照识别车牌', size_hint=(1, 0.1))
        self.layout.add_widget(self.result_label)
        
        # 创建拍照按钮
        self.capture_button = Button(text='拍照识别', size_hint=(1, 0.1))
        self.capture_button.bind(on_press=self.capture_image)
        self.layout.add_widget(self.capture_button)
        
        # 创建重置按钮
        self.reset_button = Button(text='重新开始', size_hint=(1, 0.1))
        self.reset_button.bind(on_press=self.reset_camera)
        self.reset_button.disabled = True
        self.layout.add_widget(self.reset_button)
        
        # 初始化车牌检测器
        self.detector = LicensePlateDetector()
        
        # 保存原始相机纹理
        self.original_camera = None
        
        return self.layout
    
    def capture_image(self, instance):
        # 从相机获取图像数据
        texture = self.camera.texture
        if texture is None:
            self.result_label.text = '无法获取相机图像'
            return
        
        # 保存原始相机以便重置
        self.original_camera = self.camera
        
        # 将纹理转换为OpenCV图像
        buf = np.frombuffer(texture.pixels, dtype=np.uint8)
        buf = buf.reshape(texture.height, texture.width, 4)
        # 转换为BGR格式并移除alpha通道
        img = cv2.cvtColor(buf, cv2.COLOR_RGBA2BGR)
        
        # 处理图像并识别车牌
        result_img, license_plate_img, license_text = self.detector.process_image(img)
        
        # 更新结果标签
        self.result_label.text = license_text
        
        # 将结果图像显示在相机位置
        self.show_result_image(result_img)
        
        # 启用重置按钮
        self.capture_button.disabled = True
        self.reset_button.disabled = False
    
    def show_result_image(self, img):
        # 移除相机组件
        self.layout.remove_widget(self.camera)
        
        # 将OpenCV图像转换为Kivy纹理
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_texture = Texture.create(size=(img_rgb.shape[1], img_rgb.shape[0]))
        img_texture.blit_buffer(img_rgb.flatten(), colorfmt='rgb', bufferfmt='ubyte')
        img_texture.flip_vertical()
        
        # 创建图像组件并显示
        self.result_image = Image(texture=img_texture)
        self.layout.add_widget(self.result_image, index=0)
    
    def reset_camera(self, instance):
        # 移除结果图像
        if hasattr(self, 'result_image'):
            self.layout.remove_widget(self.result_image)
        
        # 重新添加相机
        self.camera = Camera(play=True, resolution=(640, 480))
        self.layout.add_widget(self.camera, index=0)
        
        # 重置标签
        self.result_label.text = '点击拍照识别车牌'
        
        # 启用拍照按钮，禁用重置按钮
        self.capture_button.disabled = False
        self.reset_button.disabled = True

if __name__ == '__main__':
    LicensePlateApp().run()