import zipfile

zip_f = zipfile.ZipFile('sample.zip')
sum = 0

for i in range(1,1000,2):
    filename=f'sample/kitamura_{i:05}_kgu.txt'
    #print(filename)
    with zip_f. open(filename, 'r') as file:
       number = int(file.read().strip())
       sum+=number
print('sum',sum)