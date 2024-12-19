import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import pyupbit

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
upbit = pyupbit.Upbit(os.getenv("UPBIT_ACCESS_KEY"), os.getenv("UPBIT_SECRET_KEY"))

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello"}
    ]
)

print(completion.choices[0].message)
krw = upbit.get_balance("KRW")
print(krw)


# # 필요한 라이브러리 및 모듈을 가져옵니다
# import os  # 환경 변수(시스템 설정)를 다루기 위한 모듈
# from dotenv import load_dotenv  # .env 파일에서 환경 변수를 읽어오기 위한 모듈
# load_dotenv()  # .env 파일의 내용(환경 변수들)을 로드합니다

# from openai import OpenAI  # OpenAI의 API를 사용하기 위한 모듈
# import pyupbit  # Upbit(가상화폐 거래소)의 API를 사용하기 위한 모듈

# # OpenAI API에 연결하기 위한 클라이언트 생성
# # .env 파일에 저장된 'OPENAI_API_KEY' 값을 읽어옵니다
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # Upbit API에 연결하기 위한 객체 생성
# # .env 파일에 저장된 'UPBIT_ACCESS_KEY'와 'UPBIT_SECRET_KEY' 값을 읽어옵니다
# upbit = pyupbit.Upbit(os.getenv("UPBIT_ACCESS_KEY"), os.getenv("UPBIT_SECRET_KEY"))

# # OpenAI API에 메시지를 보내서 응답을 받는 코드
# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",  # 사용할 AI 모델 지정
#     messages=[  # AI에 보낼 메시지 구성
#         {"role": "system", "content": "You are a helpful assistant."},  # AI에게 역할을 정의
#         {"role": "user", "content": "Hello"}  # 사용자 메시지
#     ]
# )

# # OpenAI API의 응답 중 첫 번째 선택 결과를 출력
# print(completion.choices[0].message)

# # Upbit 계좌에서 현재 보유 중인 원화(KRW) 잔고를 가져오기
# krw = upbit.get_balance("KRW")

# # 원화 잔고를 출력
# print(krw)


# # 결과값
# PS C:\gptbitcoin> python .\autotrade_v1.py
# ChatCompletionMessage(content='Hello! How can I assist you today?', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None)
# 0.9181492