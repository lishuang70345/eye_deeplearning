from django.shortcuts import render, HttpResponse
from detection.test_eye import detection
from segmentation.segmentation import seg
import json

# Create your views here.
def getim(request):
    if request.method == "POST":
        image = request.FILES['image']
        imgname = request.POST.get('imgname')
        print(image, imgname)

        with open('media/img/'+imgname, 'wb') as f:
            f.write(image.read())
            f.close()
        img = 'media/img/'+imgname

        try:
            img = seg(img)
            (img_result, disease) = detection(img, imgname)
        except:
            img, img_result, disease = img, '', []

        img = 'https://www.xmueye.com/media/img/'+imgname
        resp = {'img': img, 'img_result': img_result, 'disease': disease}
        print(resp)
        return HttpResponse(json.dumps(resp), content_type="application/json")