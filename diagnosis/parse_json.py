# {'username': '李爽',
#  'age': '25',
#  'tel': '18862196994',
#  'medical-history': ['高血压', '头疼', '糖尿病'],
#  'other': '',
#  'agree': True,
#  'result': ['无', '是', '否', '否', '是', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否', '否',
#             '血丝多', '否', '否', '否', '否', '否', '否', '否']
#  }

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

    result = data['result']

    # 1. 是否出现视力下降？
    if result[0] == '慢慢下降':
        symptom.append('视力下降（慢慢下降）')
    elif result[0] == '突然下降':
        symptom.append('视力下降（突发性）')
    elif result[0] == '自幼视力差':
        symptom.append('视力下降（天生的）')

    # 2. 看远处更清楚？
    if result[1] == '是':
        symptom.append('远看更清楚')

    # 3. 眼前是否出现闪光感？
    if result[2] == '是':
        symptom.append('闪光感')

    # 4. 视野是否缺失？
    if result[3] == '是':
        symptom.append('视野缺损')

    # 5. 看东西颜色是否不正常？
    if result[4] == '是':
        symptom.append('色觉异常')

    # 6. 看东西是否变形？
    if result[5] == '是':
        symptom.append('看东西是变形的')

    # 7. 眼睛是否出现疼痛？
    if result[6] == "眼皮痛":
        symptom.append("眼痛（眼皮）")
    elif result[6] == "眼球（眼珠子）痛":
        symptom.append("眼痛（眼珠）")

    # 8. 是否夜间看不见？
    if result[7] == '是':
        symptom.append("夜盲")

    # 9. 白天视力差，晚上视力比白天好（昼盲）？
    if result[8] == '是':
        symptom.append("晚上视力比白天好")


    # 10. 眼前是否有漂浮物？
    if result[9] == '是':
        symptom.append("眼前有漂浮物")

    # 11. 看东西是否有重影？
    if result[10] == '是':
        symptom.append("看东西重影")

    # 12. 是否畏光（总觉得刺眼）？
    if result[11] == '是':
        symptom.append("畏光（总觉得刺眼）")

    # 13. 是否有干涩感？
    if result[12] == '是':
        symptom.append("干涩感")

    # 14. 眼睛痒？
    if result[13] == '是':
        symptom.append("眼睛痒")

    # 15. 是否流泪、溢泪？
    if result[14] == '是':
        symptom.append("流泪、溢泪")

    # 16. 看东西易疲劳？
    if result[15] == '是':
        symptom.append("看东西易疲劳")

    # 17. 眼红？
    if result[16] == '血丝多':
        symptom.append("眼红（血丝多）")
    elif result[16] == '片状红':
        symptom.append("眼红（片状红）")

    # 18. 眼皮是否下垂？
    if result[17] == '是':
        symptom.append("上眼皮下垂")

    # 19. 感觉眼睛里有沙子一样（异物感）？
    if result[18] == '是':
        symptom.append("感觉眼睛里有沙子一样")

    # 20. 眼睛分泌物是否增多（例如眼屎）？
    if result[19] == '是':
        symptom.append('眼屎多')

    # 21. 睁眼困难？
    if result[20] == '是':
        symptom.append('睁眼困难')

    # 22. 一直眨眼睛？
    if result[21] == '是':
        symptom.append("一直眨眼睛")

    # 23. 眼睛上长东西？
    if result[22] == '眼皮':
        symptom.append("眼睛上长东西（眼皮）")
    elif result[22] == '眼球（眼珠子）':
        symptom.append("眼睛上长东西（眼珠）")

    # 24. 是否有眼外伤？
    if result[23] == '是':
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
            'result': ['无', '是', '是', '否', '是', '否', '眼球（眼珠子）痛', '是', '是', '否', '否', '否', '否', '否', '否', '否',
                        '血丝多', '否', '否', '否', '否', '否', '否', '否']
            }

    case = parse_json(data)

    print(case)
