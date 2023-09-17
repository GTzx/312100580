
import string
import sys
import difflib

# 读取文件内容
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"文件不存在：{file_path}")
        return FileNotFoundError

def preprocess(text):
# 去除标点符号和空格，转换为小写字母
    text = text.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ', '')
    return text

# 使用difflib.Sequencematcher比较文本并计算重复率
def get_plagiarism_percentage(original_text, copied_text):
    # 创建Sequencematcher对象
    matcher = difflib.SequenceMatcher(None, original_text, copied_text)
    # 获取匹配块
    matching_blocks = matcher.get_matching_blocks()
    # 计算总匹配字符数
    total_matching_chars = sum(block.size for block in matching_blocks)
    # 计算重复率
    plagiarism_percentage = total_matching_chars / max(len(original_text),len(copied_text))

    return plagiarism_percentage

def main():
    if len(sys.argv) != 4:
        print("用法: python main.py 原文文件 抄袭版文件 答案文件")
        sys.exit(1)

    orig_path, copied_path, output_path = sys.argv[1:]

    # 读取原文文本和抄袭文本
    original_text = read_file(orig_path)
    copied_text = read_file(copied_path)

    # 预处理文本
    original_text = preprocess(original_text)
    copied_text = preprocess(copied_text)

    # 计算重复率
    plagiarism_percentage = get_plagiarism_percentage(original_text, copied_text)

    # 写入答案文件
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(f"{plagiarism_percentage:.2%}")

    # profiler.print_stats(sort='cumulative')

if __name__ == "__main__":
    main()
