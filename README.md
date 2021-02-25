# elk 오픈 스택 활용을 위한 파이썬 코드

## elk에 대해 간단한 설명을 작성한다.

1. elasticsearch는 데이터 저장 및 조회가 가능하다.
elasticsearch폴더 안에는 REST API를 활용을 위한
json 파일을 담아둔 json폴더가 있으며
python_src에는 python을 활용하여 elasticsearch에 
데이터를 직접 전달할 수 있는 소스들을 넣어두었다.

2. logstash는 데이터를 elasticsearch에 전송해주는 역할을 한다.
logstash폴더안에는 conf폴더와 python_src폴더가 있다.
conf파일은 logstash가 돌아갈 때 필요한 파일을 말하여 
필터링 및 데이터 전송에 대한 역할을 해주기에 중요하다.
python_src에는 logstash로 데이터를 전달할 수 있도록하는
코드를 작성해두었다.
