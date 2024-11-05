CFSRCNN

Paddle 复现版本

## 数据集

分类之后训练集用于训练SR模块
https://aistudio.baidu.com/aistudio/datasetdetail/106261
## aistudio
脚本任务地址: https://aistudio.baidu.com/aistudio/clusterprojectdetail/2356381
## 训练模型
链接：https://pan.baidu.com/s/1jf0UKI_wf7yRhwdA4AU5Kw 
提取码：u9lr
## 训练步骤
### train sr
```bash
python train.py -opt config/train/train_RCAN.yml
```
### train ClassSR
```bash
python train_ClassSR.py -opt config/train/train_ClassSR_RCAN.yml
```
多卡仅需
```bash
python -m paddle.distributed.launch train.py --launcher fleet -opt config_file_path
python -m paddle.distributed.launch train_ClassSR.py --launcher fleet -opt config_file_path
```
## 测试步骤
```bash
python test.py -opt config/test/test_RCAN.yml
```
```bash
python test_ClassSR.py -opt config/test/test_ClassSR_RCAN.yml
```
