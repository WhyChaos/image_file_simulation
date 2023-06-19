import os


class Judge:
    def __init__(self, keyword_path):
        keyword_path = os.path.abspath(keyword_path)
        self.keyword_path = keyword_path

    def main(self, word: str):
        with open(self.keyword_path, 'r') as dic_file:
            for line in dic_file:
                keyword = line.strip()
                if keyword in word:
                    return True
        return False
