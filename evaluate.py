# 评估模型在测试集中的psnr和ssim指标

import tensorflow as tf

def read_img(path):
    return tf.image.decode_image(tf.read_file(path))

def psnr(img1, img2):
    return tf.image.psnr(img1, img2, max_val=255)

def ssim(img1, img2):
    return tf.image.ssim(img1, img2, max_val=255, filter_size=11, filter_sigma=1.5, k1=0.01, k2=0.03)

def main():
    PSNR = []
    SSIM = []
    for index in range(10):
        #两张图像的尺寸要完全一致
        hr_path = 'outputs/hr_' + str(index+1) + '.jpg'
        sr_path = 'outputs/sr_' + str(index+1) + '.jpg'
        hr = read_img(hr_path)
        sr = read_img(sr_path)
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            p = sess.run(psnr(hr, sr))
            s = sess.run(ssim(hr, sr))
            print(p)
            print(s)
            PSNR.append(p)
            SSIM.append(s)
    print("PSNR:")
    print(PSNR)
    print("SSIM:")
    print(SSIM)
    with open('results.txt','a') as f:
        f.write('PSNR:\n')
        f.write(str(PSNR))
        f.write('\nSSIM:\n')
        f.write(str(SSIM))

if __name__ == '__main__':
    main()
