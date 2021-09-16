

def parse_json(data):
    name = data['username']
    age = int(data['age'])
    # phone = data['tel']

    history = {'糖尿病': False,
               '高血压': False,
               '头疼': False,
               '其他': None}
    symptom = []

    if '糖尿病' in data['medical-history']:
        history['糖尿病'] = True
    if '高血压' in data['medical-history']:
        history['高血压'] = True
    if '头疼' in data['medical-history']:
        history['头疼'] = True
    # else:
    #     history['其他'] = item


    # 1. 是否感觉看东西模糊（视力下降）？
    if '慢慢的越来越看不清（最近几天、几个月或几年逐渐下降）' in data['1']:
        symptom.append('视力下降（慢慢下降）')
    if '突然就看不见了' in data['1']:
        symptom.append('视力下降（突发性）')
    if '从小视力不好' in data['1']:
        symptom.append('视力下降（天生的）')

    # 2.是否出现下列症状？（可多选)
    if '觉得看书/报纸模糊、看电视或远一点的地方更清楚（远视）' in data['2']:
        symptom.append('远看更清楚')
    if '觉得看远处模糊、看近处更清楚（近视）' in data['2']:
        symptom.append('近看更清楚')
    if '眼前突然间像看到闪电一样亮一下' in data['2']:
        symptom.append('闪光感')
    if '眼前黑了一块' in data['2']:
        symptom.append('视野缺损')
    if '看东西都是变形的，如直线变弯了' in data['2']:
        symptom.append('看东西是变形的')
    if '眼前有会飘的黑影，像蚊子一样' in data['2']:
        symptom.append("眼前有漂浮物")
    if '灯光周围有一圈彩虹' in data['2']:
        symptom.append("虹视")

    # 3.是否出现下列症状？（可多选）
    if '感觉眼睛里面有沙子' in data['3']:
        symptom.append("感觉眼睛里有沙子一样")
    if '眼睛干涩' in data['3']:
        symptom.append("干涩感")
    if '眼睛痒' in data['3']:
        symptom.append("眼睛痒")
    if '怕光（总觉得刺眼）' in data['3']:
        symptom.append("畏光（总觉得刺眼）")
    if '眼分泌物（眼屎）比平常增多' in data['3']:
        symptom.append('眼屎多')
    if '眼泪很多（溢泪）' in data['3']:
        symptom.append("流泪、溢泪")

    # 4.是否出现下列症状？（可多选）
    if '眼球突出' in data['4']:
        symptom.append("眼球突出")
    if '眼睑肿胀' in data['4']:
        symptom.append("眼睑肿胀")
    if '眼皮下垂（上眼皮遮挡大半个眼睛）' in data['4']:
        symptom.append("上眼皮下垂")
    if '暗一点的地方就看不见了（夜盲）' in data['4']:
        symptom.append("夜盲")
    if '晚上比白天看的更清楚（昼盲）' in data['4']:
        symptom.append("昼盲")
    if '看东西的颜色变的跟平常不一样' in data['4']:
        symptom.append('色觉异常')
    if '会把一个东西看成两个（视物重影）' in data['4']:
        symptom.append("看东西重影")

    # 5.眼睛是否出现疼痛？
    if '眼皮痛' in data['5']:
        symptom.append("眼痛（眼皮）")
    if '眼球（眼珠子）痛' in data['5']:
        symptom.append("眼痛（眼珠）")

    # 6.是否发现眼睛红？
    if '血丝多' in data['6']:
        symptom.append("眼红（血丝多）")
    if '眼白的地方有一片红色的血' in data['6']:
        symptom.append("眼红（片状红）")

    # 7.眼睛上长东西？
    if '长在眼皮上' in data['7']:
        symptom.append("眼睛上长东西（眼皮）")
    if '长在眼球（眼珠子）上' in data['7']:
        symptom.append("眼睛上长东西（眼珠）")

    # 8.眼睛是否有受伤（碰撞、划伤、击伤、刺伤、看紫外线灯、异物或有害物质入眼等）？
    if '是' in data['8']:
        symptom.append("有眼外伤")



    case = {'姓名': name,
            '年龄': age,
            # '电话': phone,
            '病史': history,
            '症状': symptom}

    return case


if __name__ == "__main__":
    data = {'username': 'll',
            'age': '25',
            'tel': '18862196994',
            'medical-history': ['高血压', '糖尿病'],
            'other': '',
            'agree': True,
            '1': ['从小视力不好'],
            '2': ['眼前感觉有黑影飘动如蚊子、苍蝇、蜘蛛网等', '看东西都是变形的，如直线变弯了'],
            '3': [],
            '4': ['眼球突出', '眼睑肿胀'],
            '5': [],
            '6': [],
            '7': [],
            '8': ['是'],
            }

    case = parse_json(data)

    print(case)
