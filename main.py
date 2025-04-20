from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window

# 设置窗口大小
Window.size = (400, 600)

# 除法计算函数
def division_with_remainder(dividend, divisor):
    """
    执行除法运算并返回商和余数。

    Args:
        dividend: 被除数。
        divisor: 除数。

    Returns:
        一个包含商和余数的元组 (quotient, remainder)。
        如果除数为零，则返回 None。
    """
    try:
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder
    except ZeroDivisionError:
        return None

# 计算器屏幕
class CalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super(CalculatorScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 标题
        self.layout.add_widget(Label(text='除法计算器', font_size=24, size_hint=(1, 0.2)))
        
        # 被除数输入
        dividend_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.15))
        dividend_layout.add_widget(Label(text='被除数:', size_hint=(0.3, 1)))
        self.dividend_input = TextInput(multiline=False, input_type='number', size_hint=(0.7, 1))
        dividend_layout.add_widget(self.dividend_input)
        self.layout.add_widget(dividend_layout)
        
        # 除数输入
        divisor_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.15))
        divisor_layout.add_widget(Label(text='除数:', size_hint=(0.3, 1)))
        self.divisor_input = TextInput(multiline=False, input_type='number', size_hint=(0.7, 1))
        divisor_layout.add_widget(self.divisor_input)
        self.layout.add_widget(divisor_layout)
        
        # 计算按钮
        self.calculate_button = Button(text='计算', size_hint=(1, 0.15))
        self.calculate_button.bind(on_press=self.calculate)
        self.layout.add_widget(self.calculate_button)
        
        # 结果显示
        self.result_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.3))
        self.quotient_label = Label(text='商: ', size_hint=(1, 0.5))
        self.remainder_label = Label(text='余数: ', size_hint=(1, 0.5))
        self.result_layout.add_widget(self.quotient_label)
        self.result_layout.add_widget(self.remainder_label)
        self.layout.add_widget(self.result_layout)
        
        # 错误信息
        self.error_label = Label(text='', color=(1, 0, 0, 1), size_hint=(1, 0.15))
        self.layout.add_widget(self.error_label)
        
        # 导航到图片页面的按钮
        self.image_button = Button(text='查看六十四卦名速见表', size_hint=(1, 0.15))
        self.image_button.bind(on_press=self.go_to_image)
        self.layout.add_widget(self.image_button)
        
        self.add_widget(self.layout)
    
    def calculate(self, instance):
        # 清除之前的错误信息
        self.error_label.text = ''
        
        try:
            dividend = int(self.dividend_input.text)
            divisor = int(self.divisor_input.text)
            
            result = division_with_remainder(dividend, divisor)
            
            if result is None:
                self.error_label.text = '除数不能为零'
                self.quotient_label.text = '商: '
                self.remainder_label.text = '余数: '
            else:
                quotient, remainder = result
                self.quotient_label.text = f'商: {quotient}'
                self.remainder_label.text = f'余数: {remainder}'
        
        except ValueError:
            self.error_label.text = '无效的输入. 请输入整数.'
            self.quotient_label.text = '商: '
            self.remainder_label.text = '余数: '
    
    def go_to_image(self, instance):
        self.manager.current = 'image'

# 图片显示屏幕
class ImageScreen(Screen):
    def __init__(self, **kwargs):
        super(ImageScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 标题
        self.layout.add_widget(Label(text='六十四卦名速见表', font_size=24, size_hint=(1, 0.1)))
        
        # 图片显示
        self.image = Image(source='assets/64卦名.jpeg', size_hint=(1, 0.8), allow_stretch=True)
        self.layout.add_widget(self.image)
        
        # 返回按钮
        self.back_button = Button(text='返回计算器', size_hint=(1, 0.1))
        self.back_button.bind(on_press=self.go_back)
        self.layout.add_widget(self.back_button)
        
        self.add_widget(self.layout)
    
    def go_back(self, instance):
        self.manager.current = 'calculator'

# 主应用
class RemainderApp(App):
    def build(self):
        # 创建屏幕管理器
        self.screen_manager = ScreenManager()
        
        # 添加计算器屏幕
        calculator_screen = CalculatorScreen(name='calculator')
        self.screen_manager.add_widget(calculator_screen)
        
        # 添加图片屏幕
        image_screen = ImageScreen(name='image')
        self.screen_manager.add_widget(image_screen)
        
        return self.screen_manager

if __name__ == '__main__':
    RemainderApp().run()
