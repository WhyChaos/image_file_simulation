def is_chinese(char):
    if '\u4e00' <= char <= '\u9fff':
        return True
    else:
        return False


print(is_chinese('还'))
print(len('海hai '))
