file_path = r'test.txt'


file_to_open = codecs.open(file_path, 'r+', 'utf-8')
sentences = file_to_open.readlines()
