from mmcv import Config

cfg = Config.fromfile("./configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py")

# print(cfg)
print(f'Config:\n{cfg.pretty_text}')
