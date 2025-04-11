from PIL import Image
import os

def resize_icon(input_path, output_dir):
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 定义Android需要的图标尺寸
    sizes = {
        'mdpi': 48,
        'hdpi': 72,
        'xhdpi': 96,
        'xxhdpi': 144,
        'xxxhdpi': 192
    }
    
    try:
        # 打开原始图片
        with Image.open(input_path) as img:
            # 确保图片是RGBA模式
            img = img.convert('RGBA')
            
            # 为每个尺寸创建图标
            for dpi, size in sizes.items():
                # 创建对应的mipmap目录
                mipmap_dir = os.path.join(output_dir, f'mipmap-{dpi}')
                os.makedirs(mipmap_dir, exist_ok=True)
                
                # 调整图片大小
                resized = img.resize((size, size), Image.Resampling.LANCZOS)
                
                # 保存调整后的图片
                output_path = os.path.join(mipmap_dir, 'favicon.png')
                resized.save(output_path, 'PNG')
                print(f'已生成 {dpi} 图标: {size}x{size}')
    
    except Exception as e:
        print(f'处理图片时出错: {e}')

if __name__ == '__main__':
    # 输入文件路径
    input_file = 'favicon.png'
    # 输出目录路径
    output_dir = 'android/app/src/main/res'
    
    resize_icon(input_file, output_dir)
    print('图标生成完成！') 