import json

# 你的文件路径
file_path = "2023_11_3_大会戦南喰赤.json"

# 从文件中读取JSON数据
with open(file_path, "r", encoding="utf-8") as file:
    json_str = file.read()

# # 假设json_str是你的原始JSON数据，可以自己粘贴
# json_str =
# {"log":[[[0,0,0],[30000,30000,30000,30000],[47],[],[29,21,46,14,28,11,47,18,21,44,32,35,46],[32,34,21,36,22,41],[11,44,47,18,60,60],[35,24,33,26,34,31,31,43,34,26,29,26,17],[17,28,23,17,13,15],[29,43,28,34,60,"r60"],[15,29,18,14,41,12,22,43,19,23,26,27,47],[24,21,18,14,28,25],[47,43,12,41,14,19],[42,39,47,12,32,13,28,38,11,36,18,22,42],[16,39,16,13,35,42],[22,28,32,47,16,13],["和了",[0,0,4900,-3900],[2,3,2,"30符3飜3900点","一気通貫(2飜)","平和(1飜)"]]],[[1,0,0],[30000,29000,34900,26100],[19],[],[46,32,35,46,43,44,41,26,18,17,13,22,39],[22,45,43,28,12,"p464646",45,22,24,47,23,14,23],[39,43,41,43,44,45,60,32,35,60,26,28,24],[16,32,11,16,39,25,25,16,21,17,39,27,35],[15,23,38,29,44,31,34,44,47,42,21,41,53,"c242325"],[11,32,39,25,60,60,38,39,60,60,44,29,41,35],[19,15,16,24,34,24,31,38,51,36,32,42,24],[12,52,34,36,45,13,25,46,19,29,37,28,29,19],[19,42,31,12,60,60,15,60,60,60,36,60,60,60],[45,11,36,26,28,42,47,18,35,17,33,18,39],[12,21,26,14,31,46,29,17,11,14,13,37,37],[39,60,42,47,45,60,28,29,31,33,36,60,35],["和了",[1000,0,-1000,0],[0,2,0,"30符1飜1000点","役牌 發(1飜)"]]],[[2,0,0],[31000,29000,33900,26100],[44],[],[12,41,44,34,43,37,47,19,13,38,16,47,18],[28,39,31,"p474747",31,19,31],[43,44,34,16,28,41,18],[35,11,33,25,42,32,19,27,16,28,47,33,25],[43,21,14,27,35,17,26],[60,11,19,42,21,47,14],[53,41,38,24,18,26,46,26,44,37,14,42,21],[22,22,22,46,43,21,42],[44,42,21,18,60,60,24],[23,43,22,41,39,33,45,25,45,36,29,44,15],[17,29,13,47,13,19,17],[44,43,39,60,41,33,36],["和了",[1300,-1300,0,0],[0,1,0,"40符1飜1300点","役牌 中(1飜)"]]],[[3,0,0],[32300,27700,33900,26100],[46],[],[12,15,19,28,29,16,31,46,21,25,41,36,13],[27,33,47,42,38,35,24,13,28,22,22],[41,46,19,21,42,38,47,33,28,31,60],[32,23,36,43,45,36,37,42,25,11,12,14,24],[46,46,34,26,19,38,12,"c333234",32,15,41],[42,11,43,45,60,26,46,46,60,36,60],[16,29,44,21,27,25,26,34,14,43,16,32,18],[33,28,11,37,17,21,42,32,22,18,13],[43,44,60,21,37,60,60,14,60,60,60],[17,31,29,44,23,17,19,26,17,43,33,39,26],[47,45,27,16,21,44,31,52,42,15,24],[60,44,43,39,45,19,33,44,29,21,42],["和了",[0,1000,-1000,0],[1,2,1,"30符1飜1000点","断幺九(1飜)"]]],[[4,0,0],[32300,28700,32900,26100],[16],[],[47,19,36,26,21,43,27,38,45,18,44,31,21],[11,17,23,31,34,19,34,47,37,41,35,28,18,22,14,18,15],[43,44,11,47,45,60,60,60,34,60,60,"r23",60,60,60,60,60],[41,29,19,44,36,33,39,46,39,45,21,12,11],[29,23,45,24,14,47,39,42,23,45,"29p2929",27,38,17,"c222123",28,29],[12,33,36,60,60,23,44,60,19,46,47,60,41,11,38,17,28],[52,38,21,28,31,16,14,28,47,24,32,37,34],[43,12,19,35,31,24,14,27,13,13,35,15,37,42,38,44,"p282828"],[60,21,60,47,60,60,32,60,14,16,13,12,35,60,60,60,38],[12,11,25,46,25,16,44,51,25,26,36,43,37],[11,46,42,32,24,33,42,26,29,16,36,41,"c353637",15,33,27,23],[44,43,12,42,32,60,60,46,46,29,60,60,11,11,60,25,60],["和了",[-2000,0,0,3000],[3,0,3,"30符2飜2000点","断幺九(1飜)","赤ドラ(1飜)"]]],[[5,0,0],[29300,28700,32900,29100],[12],[],[43,45,28,12,39,27,35,22,41,28,15,47,42],[38,31,41,44,39,34,31,13,25],[43,41,60,31,47,42,60,45,22],[43,24,26,13,15,16,21,42,32,27,15,29,24],[19,14,44,32,25,31,18,23,11],[43,19,60,21,29,42,60,31,60],[37,17,24,29,19,41,38,33,26,43,33,16,44],[11,52,17,46,27,39,19,53,37],[43,19,44,41,11,46,60,17,29],[11,14,28,21,45,45,36,22,36,36,12,12,19],[27,23,32,37,25,23,22,17,"4545p45"],[19,11,60,14,37,60,60,25,17],["和了",[0,0,-1000,1000],[3,2,3,"30符1飜1000点","役牌 白(1飜)"]]],[[6,0,0],[29300,28700,31900,30100],[41],[],[15,27,46,37,18,46,38,41,13,22,29,21,19],[11,11,44,43,"4646p46",44,"c171819",16],[41,15,60,60,13,60,22,60],[19,16,46,42,31,26,42,18,47,41,36,45,34],[33,14,22,"42p4242",15,29,16,31,"c161415"],[31,41,45,47,46,60,22,19,18],[45,37,35,43,25,28,38,28,46,24,39,37,36],[31,36,47,52,44,32,26,14,12],[43,31,45,47,60,46,32,39,25],[35,38,17,21,24,16,22,27,23,34,26,43,19],[21,34,47,42,36,17,15,41],[43,38,60,60,34,19,17,60],["和了",[0,0,-1000,1000],[3,2,3,"30符1飜1000点","平和(1飜)"]]],[[7,0,0],[29300,28700,30900,31100],[21],[],[26,28,38,42,46,11,42,38,18,13,38,13,31],[45,"p424242",41,31,45,27,31,32,47],[31,46,60,60,18,11,60,60,60],[29,12,39,16,23,35,37,26,43,33,34,41,29],[12,29,14,15,18,35,21,13],[41,43,23,26,60,"r35",60,60],[12,22,24,18,43,27,34,19,14,44,25,19,32],[41,25,"c232224",43,14,26],[44,41,19,43,19,32],[46,46,14,36,35,27,38,44,28,42,53,39,11],[39,36,"4646p46",52,51,39,44,"53p3535",21],[44,42,11,14,60,38,60,28,60],["和了",[3600,-2600,0,0],[0,1,0,"40符2飜2600点","役牌:場風牌(1飜)","役牌:自風牌(1飜)"]]]],"rule":{"disp":"大会戦南喰赤","aka":1},"name":["心修","落宸","巨捞","吾导先路"],"title":["大会戦南喰赤: 14834","2023/9/27 22:02:58"]}

# 解析JSON字符串
data = json.loads(json_str)

# 对每个外部数组进行检查和修改
for entry in data["log"]:
    score_array = entry[1]
    # 检查是否是得分数组
    if len(score_array) == 4 and all(isinstance(x, (int, float)) for x in score_array):
        # 修改得分数组
        entry[1] = [num - 5000 for num in score_array]

# 将修改后的数据保存为新的JSON日志
new_json_str = json.dumps(data, indent=4, ensure_ascii=False)

# 保存到文件
with open("new_log.json", "w", encoding="utf-8") as file:
    file.write(new_json_str)