# 将测试集的hr图像长宽裁剪至4的倍数，方便评估psnr与ssim

from PIL import Image
import os

def main():
	path = 'outputs'
	for index in range(10):
		test_hr_path = os.path.join(path, 'hr_' + str(index+1) + '.jpg')
		img = Image.open(test_hr_path)
		print('original size:')
		print(img.size)
		length = img.size[0]
		width = img.size[1]
		img = img.crop((0, 0, length//4*4, width//4*4))
		print('current size:')
		print(img.size)
		img.save(test_hr_path)

if __name__ == '__main__':
    main()