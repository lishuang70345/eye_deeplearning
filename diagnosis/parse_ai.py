def parse_ai(ai):

    replace_ai = {"JIAOMY": "角膜炎", "JMHZ": "角膜混浊", "JIAOMBB": "角膜病变", "JMLNH": "角膜老年环",
                  "JIEMY": "结膜炎", "YZNR": "翼状胬肉", "JLB": "睑裂斑", "JMCX": "结膜下出血", "JIEMBB": "结膜病变",
                  "BNZ": "白内障",
                  "PTMY": "葡萄膜炎",
                  "YBSSSH": "眼表手术术后状态", "KQGYSH": "抗青光眼术后",
                  "YJJB": "眼睑疾病", "DJ": "倒睫", "YBZW": "眼表肿物"
                  }
    for item in ai.copy():
        if item == "jiaomo":
            ai.remove(item)
        if item == "YBSSSH":
            ai.remove(item)
        if item == "KQGYSH":
            ai.remove(item)
        # print(ai)

    ai = [replace_ai[i] if i in replace_ai else i for i in ai]
    return ai


if __name__ == "__main__":
    ai = ["JIAOMY", "jiaomo", "jiaomo"]
    disease = parse_ai(ai)
    print(disease)