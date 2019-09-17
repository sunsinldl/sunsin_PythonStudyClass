xiaoming_dict = {"name": "小明",
                 "age": 18,
                 "gender": True}
# 1.统计键值对数量
print(len(xiaoming_dict))

# 2.合并字典
temp_tuple = {"height": 1.75}
xiaoming_dict.update(temp_tuple)

# 3.清空字典
xiaoming_dict.clear()
print(xiaoming_dict)
