# 7186. 사전 만들기

word = []

N = int(input())
for i in range(N) :
    word.append(input())

# 정렬
sort_word = sorted(word, key = lambda x : (len(x), x))
# print(sort_word)

# 중복 제거
result_word = list(dict.fromkeys(sort_word))

# 출력
for i in result_word :
    print(i)


''' 참고사항

- sorted(정렬할 데이터, key 파라미터, reverse 파라미터)
    : key 옵션 (key 파라미터)
    어떤 것을 기준으로 정렬할 것인가? 에 대한 기준
    즉, key 값을 기준으로 비교를 하여 정렬을 하겠다는 것
    이것을 정해 줄 수 있는 파라미터

- lamda
    : key = lamda x : (len(x), x)
    len(x) 는 word의 각 단어마다의 길이. 먼저 단어길이로 정렬하므로 첫번째에 둠
    x 는 단어 자체를 의미. 길이 다음 알파벳 순으로 정렬하므로 두번째째
    
- 리스트 중복 제거방법 3가지 (set -> 정렬까지 되버림, for -> 귀찬/시간오래 , dictionary)
    : dict.fromkeys( iterable)
    인자로 들어온 iterable 데이터를 key 값으로 해서 딕셔너리 자료형을 만들어 주는 작업을 하는 메서드
'''

'''
문제:
세아는 영어를 너무 좋아한 나머지 자기만의 영어사전을 만들려고 합니다. 
머릿속에 떠오른 영어단어를 다음과 같은 기준에 따라 정리하려고 합니다.
우선, 길이가 짧은 단어부터 순서대로 나열합니다. 만약 단어의 길이가 같다면 사전순대로 정리합니다.
세아가 사전을 만드는 프로그램을 작성하세요.

테스트케이스:
3
apple               apple
banana              banana
coconut        >    coconut

6
monk                    
apply                   monk
angel                   angel
elephant                apply
apply                   elephant
encyclopedia        >   encyclopedia

입력값 설명:
첫째 줄에 영단어의 개수 N이 주어집니다. (1 ≤ N ≤ 1,000)
둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어집니다.
주어지는 문자열의 길이는 50을 넘지 않습니다.

출력값 설명:
기준에 따라 정렬하여 단어들을 출력합니다. 
단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력합니다.

'''