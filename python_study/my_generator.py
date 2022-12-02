def my_generators(test): # 제너레이터함수 생성
    for i in test:
        yield i	# for문으로 들어온 값들을 yield해준다.
            

number= list(range(1,10))

a  = my_generators(number) # 제너레이터 객체 생성
a.__next__()
next(a)
next(a)



def three_generator():
    a = [1, 2, 3]
    yield from a

a = three_generator()
print(a.__next__())


lst = [1,2,3,4,5]

list_result = [i *10 for i in lst]
generator_result =(i *10 for i in lst)

print(list_result)
print(generator_result)
print(next(generator_result))

