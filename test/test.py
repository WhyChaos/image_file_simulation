def find_all_keyword_positions(keyword, sentence):
    positions = []
    start_position = 0
    while True:
        position = sentence.find(keyword, start_position)
        if position == -1:
            break
        positions.append(position)
        start_position = position + 1
    return positions


keyword = "关键字"
sentence = "这是一个包含关键字的句子，关键字出现在这里，还有另外一个关键字。"
positions = find_all_keyword_positions(keyword, sentence)

if positions:
    print(f"关键字在句子中的位置是: {positions}")
else:
    print("关键字未在句子中找到。")
