import json
import numpy as np
from string import digits


yzk = {'眼表专科': ['睑腺炎', '睑板腺囊肿', '病毒性睑皮炎', '过敏性睑皮炎', '眼睑肿物',
                '倒睫', '眼睑闭合不全', '上睑下垂', '泪道狭窄或阻塞', '泪囊炎',
                '干眼', '睑板腺功能障碍', '细菌性结膜炎', '病毒性结膜炎', '沙眼',
                '过敏性结膜炎', '结膜肿瘤', '翼状胬肉/睑裂斑', '结膜下出血',
                '结膜结石', '病毒性角膜炎', '真菌性角膜炎', '角膜炎症', '圆锥角膜',
                '角膜肿瘤', '巩膜炎', '角膜炎', '葡萄膜炎', '睑皮炎', '眼睑肿物', '睑板腺囊肿'],
       '视光专科': ['近视', '远视', '散光', '老视（老花眼）', '弱视', '视疲劳'],
       '眼底病专科': ['玻璃体浑浊（飞蚊症）', '玻璃体后脱离', '玻璃体积血', '视网膜脱离',
                 '黄斑裂孔', '青光眼', '视网膜动脉阻塞', '视网膜静脉阻塞', '糖尿病性视网膜病变', '糖尿病性视网膜病变（前期）',
                 '高血压视网膜病变', '高血压视网膜病变（前期）', '黄斑变性', '视神经炎', '缺血性视神经病变', '色盲/色弱', '夜盲症/视网膜色素变性'
                 '视网膜色素变性', '夜盲症'],
       '青光眼专科': ['急性闭角型青光眼', '青光眼'],
       '斜视与小儿眼科': ['斜视', '12岁以下'],
       '眼外伤专科': ['眼外伤'],
       '白内障专科': ['白内障'],
       '无': ['您的眼睛很健康，请继续保持']
       }

remove_digits = str.maketrans('', '', digits)


def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))


class Disease_Diagnose:
    def __init__(self):
        # with open("diagnosis/eye_disease_new.json", 'r') as fp:
        with open("/home/ubuntu/wx_test/diagnosis/eye_disease.json", 'r') as fp:
            self.disease_info = json.load(fp)

    def diagnose(self, case):
        age = case['年龄']
        symptom = case['症状']
        history = case['病史']

        if not symptom and not history['糖尿病'] and not history['高血压']:
            return []
        # 首先判断是否有眼外伤
        elif '有眼外伤' in symptom:
            # index = possible_list.index('眼外伤')
            # possible_rank[index] = 110
            return ['眼外伤']
        else:

            # 根据必有症状及否定症状先得到所有可能的眼表候选集合
            # 结合年龄
            possible_list = []
            for key in self.disease_info:
                info = self.disease_info[key]
                # print(key, info['must'])

                if set(info['must']) <= set(symptom) and set(info['not']) & set(symptom) == set():
                    # print(key, info['must'])
                    # possible_list.append(key)

                    # 根据年龄去除不合理的
                    if info['age']:
                        age_first = info['age'][0]
                        if age_first[0] == "<" and age <= get_num(age_first):
                            possible_list.append(key)
                        elif age_first[0] == ">" and age >= get_num(age_first):
                            possible_list.append(key)
                    else:
                        possible_list.append(key)

                # # 根据年龄来进行加权
                # if info['age']:
                #     age_first = info['age'][0]
                #     if age_first[0] == "<":
                #         rank -= np.tanh((age - get_num(age_first)) / 10) * 3
                #     else:
                #         rank += np.tanh((age - get_num(age_first)) / 10) * 3

            # 根据必有症状 + 或有症状 的总个数计算重叠症状
            # 急性病 优先度 +5
            # 年龄
            possible_rank = []
            for pos in possible_list:
                info = self.disease_info[pos]

                info_symptom = info['must'] + info['or']

                rank = len(set(symptom) & set(info_symptom))
                # 急性病 优先度 +5
                if info['acute']:
                    rank += 5

                possible_rank.append(rank)

            # 根据病史进行判断
            # 1. 糖尿病
            if history['糖尿病'] and '糖尿病性视网膜病变' in possible_list:
                index = possible_list.index('糖尿病性视网膜病变')
                possible_rank[index] = 100

            if not history['糖尿病'] and '糖尿病性视网膜病变' in possible_list:
                index = possible_list.index('糖尿病性视网膜病变')
                possible_rank[index] = -10

            if history['糖尿病'] and '糖尿病性视网膜病变' not in possible_list:
                possible_list.append('糖尿病性视网膜病变（前期）')
                possible_rank.append(10)

            # 2. 高血压
            if history['高血压'] and '高血压视网膜病变' in possible_list:
                index = possible_list.index('高血压视网膜病变')
                possible_rank[index] = 100

            if not history['高血压'] and '高血压视网膜病变' in possible_list:
                index = possible_list.index('高血压视网膜病变')
                possible_rank[index] = -10

            if history['高血压'] and '高血压视网膜病变' not in possible_list:
                possible_list.append('高血压视网膜病变（前期）')
                possible_rank.append(10)

            # 3. 头疼
            if history['头疼'] and '急性闭角型青光眼' in possible_list:
                index = possible_list.index('急性闭角型青光眼')
                possible_rank[index] = 100

            print(possible_list)

            # 进行排序
            possible_index = np.argsort(-np.array(possible_rank))

            result = []
            for index in possible_index:
                print(possible_list[index], possible_rank[index])
                # 去除是负分的
                if possible_rank[index] > 0:
                    result.append(possible_list[index].translate(remove_digits))
            # if len(result) == 0:
            #     result.append('')

            return result

    def get_yzk(self, result, age):
        yzk_name = "眼表专科"

        if age <= 12:
            yzk_name = "斜视与小儿眼科"
        else:
            for item in yzk:
                if result in yzk[item]:
                    yzk_name = item
                    break
        return yzk_name


if __name__ == "__main__":
    dg = Disease_Diagnose()
    # print(dg.disease_info)

    case = {'年龄': 50,
            # '症状': [],
            # '症状': ['视力下降（慢慢下降）', '看东西是变形的', '看东西重影', '有眼外伤', '眼睛痒'],
            # '症状': ['视力下降（突发性）', '看东西是变形的', '看东西重影', '有眼外伤', '远看更清楚', '眼珠痛'],
            '症状': ['眼睛上长东西（眼皮）', "干涩感"],
            '病史': {'糖尿病': False,
                   '高血压': False,
                   '头疼': False,
                   '其他': ''}}
    result = dg.diagnose(case)
    print(result)
    yzk = dg.get_yzk(result[0], case['年龄'])
    print(yzk)
