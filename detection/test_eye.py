from mmdet.apis import init_detector, inference_detector
import mmcv
import os
import numpy as np

config_file = 'detection/my_config.py'
ckp = 'detection/eye_exps/f_latest.pth'

model = init_detector(config_file, ckp, device='cpu')


def detection(img, imgname):
    # print(img)
    # img_mmcv = mmcv.imread(img)
    # img = mmcv.imrotate(img, -90, auto_bound=True)# 旋转图片

    result = inference_detector(model, img)
    # print(result)
    # print(type(result))
    disease = model.show_result(img, result, score_thr=0.3, bbox_color=(0, 0, 255), text_color=(0, 255, 0),
                      mask_color=None, thickness=2, font_size=13,
                      out_file=f'media/img_result/'+os.path.basename(imgname))
    img_result = 'https://www.xmueye.com/media/img_result/'+os.path.basename(imgname)
    return img_result, disease

if __name__ == "__main__":

    detection('detection/ODoa86c5HjwUBeIVIVIl9KOPzoHPJw1629251686.png')