'''Unity実行時にこのファイルの実行が行われるかのテスト'''
class Test:
    '''テスト'''
    def __init__(self, data):
        self.data = data

    def message(self):
        '''出力'''
        print(self.data)

instance = Test("Hello World")
instance.message()
