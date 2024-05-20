"""ef.py のテスト"""

import unittest
from datetime import date
from os import remove

from dpc import EF, EFFile


class TestEF(unittest.TestCase):
    """EF(BaseLine) のテスト"""
    def setUp(self):
        self.cols = (
            '012345678',         # 施設コード
            '1234567890',        # データ識別番号
            '20210520',          # 退院年月日（入院） | 生年月日（外来）
            '20210420',          # 入院年月日（入院） | 外来受診年月日（外来）
            '97',                # データ区分
            '5',                 # 順序区分
            '0',                 # 行為明細番号
            '123456789012',      # 病院点数マスターコード
            '197001570',         # レセプト電算処理システム用コード
            '',                  # 解釈番号
            '特別食加算（生活療養）',  # 診療明細名称
            '0.0',                  # 使用量
            '0',                  # 基準単位
            '0.0',                # 明細点数・金額
            '1',                  # 円・点区分
            '0',                  # 出来高実績点数
            '0',                  # 行為明細区分情報
            '228',                # 行為点数
            '0',                  # 行為薬剤料
            '0',                  # 行為材料料
            '1',                  # 行為回数
            '12345678',           # 保険者番号
            '1317',               # レセプト種別コード
            '20210518',           # 実施年月日（入院） | 実施年月日・診療開始日（外来）
            '01',                 # レセプト科区分
            '010',                # 診療科区分
            '1234567890',         # 医師コード
            '4W',                 # 病棟コード
            '0',                  # 病棟区分
            '0',                  # 入外区分
            ''                    # 施設タイプ
        )
        self.ef = EF(self.cols)

    def test_post_init(self):
        """__post_init__() のテスト"""
        self.assertEqual(self.ef.ef_1, '012345678')
        self.assertEqual(self.ef.ef_3, date(2021, 5, 20))
        self.assertTrue(self.ef.ef_15)
        self.assertEqual(self.ef.ef_24, date(2021, 5, 18))

    def test_str(self):
        """__str__() のテスト"""
        expected_str = '\t'.join([
            '012345678',         # 施設コード
            '1234567890',        # データ識別番号
            '20210520',          # 退院年月日（入院） | 生年月日（外来）
            '20210420',          # 入院年月日（入院） | 外来受診年月日（外来）
            '97',                # データ区分
            '5',                 # 順序区分
            '0',                 # 行為明細番号
            '123456789012',      # 病院点数マスターコード
            '197001570',         # レセプト電算処理システム用コード
            '',                  # 解釈番号
            '特別食加算（生活療養）',  # 診療明細名称
            '0.0',                  # 使用量
            '0',                  # 基準単位
            '0.0',                  # 明細点数・金額
            '1',                  # 円・点区分
            '0',                  # 出来高実績点数
            '0',                  # '行為明細区分情報
            '228',                # 行為点数
            '0',                  # 行為薬剤料
            '0',                  # 行為材料料
            '1',                  # 行為回数
            '12345678',           # 保険者番号
            '1317',               # レセプト種別コード
            '20210518',           # 実施年月日（入院） | 実施年月日・診療開始日（外来）
            '01',                 # レセプト科区分
            '010',                # 診療科区分
            '1234567890',         # 医師コード
            '4W',                 # 病棟コード
            '0',                  # 病棟区分
            '0',                  # 入外区分
            ''                    # 施設タイプ
        ])
        self.assertEqual(str(self.ef), expected_str)


class TestEFFile(unittest.TestCase):
    """EFFile(DPCFile) のテスト"""
    def setUp(self):
        self.file_content = '\t'.join([
            '012345678',         # 施設コード
            '1234567890',        # データ識別番号
            '20210520',          # 退院年月日（入院） | 生年月日（外来）
            '20210420',          # 入院年月日（入院） | 外来受診年月日（外来）
            '97',                # データ区分
            '5',                 # 順序区分
            '0',                 # 行為明細番号
            '123456789012',      # 病院点数マスターコード
            '197001570',         # レセプト電算処理システム用コード
            '',                  # 解釈番号
            '特別食加算（生活療養）',  # 診療明細名称
            '0.0',                  # 使用量
            '0',                  # 基準単位
            '0.0',                  # 明細点数・金額
            '1',                  # 円・点区分
            '0',                  # 出来高実績点数
            '0',                  # '行為明細区分情報
            '228',                # 行為点数
            '0',                  # 行為薬剤料
            '0',                  # 行為材料料
            '1',                  # 行為回数
            '12345678',           # 保険者番号
            '1317',               # レセプト種別コード
            '20210518',           # 実施年月日（入院） | 実施年月日・診療開始日（外来）
            '01',                 # レセプト科区分
            '010',                # 診療科区分
            '1234567890',         # 医師コード
            '4W',                 # 病棟コード
            '0',                  # 病棟区分
            '0',                  # 入外区分
            ''                    # 施設タイプ
        ])

        self.file_path = 'test_ef.txt'
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(self.file_content)
        self.ef_file = EFFile(self.file_path, 'utf-8')

    def tearDown(self):
        remove(self.file_path)

    def test_read(self):
        """read() のテスト"""
        self.assertEqual(len(self.ef_file.lines), 1)
        ef_line = self.ef_file.lines[0]
        self.assertEqual(ef_line.ef_1, '012345678')
        self.assertEqual(ef_line.ef_3, date(2021, 5, 20))
        self.assertEqual(ef_line.ef_24, date(2021, 5, 18))