
import os
import unittest
from main import read_file, preprocess, get_plagiarism_percentage


class TestPlagiarismDetection(unittest.TestCase):
    def test_read_file(self):
        # 创建一个临时测试文件，并写入一些文本
        temp_file = 'temp_test_file.txt'
        with open(temp_file, 'w', encoding='utf-8') as file:
            file.write('This is a test file.')
        # 测试文件读取功能
        self.assertEqual(read_file(temp_file), 'This is a test file.')
        # 清理临时文件
        os.remove(temp_file)

    # 测试文件不存在的情况
    def test_read_none_file(self):
        self.assertEqual(read_file('invalid_file.txt'), FileNotFoundError)

    # 测试预处理模块
    def test_preprocess(self):
        text = "Hello, world! This is a test."
        preprocessed_text = preprocess(text)
        self.assertEqual(preprocessed_text, "helloworldthisisatest")

    # 测试相同文本
    def test_get_plagiarism_percentage_same(self):
        original_text = "Hello, world!"
        copied_text = "Hello, world!"
        self.assertEqual(get_plagiarism_percentage(preprocess(original_text), preprocess(copied_text)), 1)

    # 测试文本只有一半相同
    def test_get_plagiarism_percentage_half_difference(self):
        original_text = "Hello, world!"
        copied_text = "Hello, universe!"
        self.assertAlmostEqual(get_plagiarism_percentage(preprocess(original_text), preprocess(copied_text)), 0.4615, places=4)

    # 测试文本完全不相同
    def test_get_plagiarism_percentage_difference(self):
        original_text = "Hello, world!"
        copied_text = "你好，世界！"
        self.assertAlmostEqual(get_plagiarism_percentage(original_text, copied_text), 0)

    # 测试文本相似性很高
    def test_get_plagiarism_percentage_high_similarity(self):
        original_text = "This is a test."
        copied_text = "That is a test."
        self.assertAlmostEqual(get_plagiarism_percentage(preprocess(original_text), preprocess(copied_text)), 0.8182, places=4)

    # 测试文本相似性很低
    def test_get_plagiarism_percentage_low_similarity(self):
        original_text = "This is a test."
        copied_text = "This is a completely different test."
        self.assertAlmostEqual(get_plagiarism_percentage(preprocess(original_text), preprocess(copied_text)), 0.3667, places=4)

    # 测试其中一个文本为空
    def test_get_plagiarism_percentage_empty_text(self):
        original_text = ""
        copied_text = "This is a test."
        self.assertEqual(get_plagiarism_percentage(preprocess(original_text), preprocess(copied_text)), 0)


if __name__ == "__main__":
    unittest.main()