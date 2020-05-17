# WDSR_Project
实现图片 4 倍超分辨

- utils.py -- 图像降采样与数据导入
- model.py -- WDSR 模型
- optimizer.py -- 权重归一化 Adam 优化器
- train.py -- 模型训练
- predict.py -- 测试集预测
- resize.py -- 对结果中的高分辨率源图像长宽裁剪至 4 的倍数
- evaluate.py -- 对测试集测评 PSNR 与 SSIM，结果存入 results.txt
