import streamlit as st
import os
from openai import OpenAI


client = OpenAI(
    # This is the default and can be omitted
    api_key=st.secrets['api_key'],
)

context = [
      {
        "role": "system",
        "content": "너는 지금부터 오늘의 운세를 출력해주는 프로그램이다. 유저가 입력한 생년월일에 맞게 운세를 출력해줘\n\n#예시\n극적인 반전이 이루어질 것 같네. 순간적인 변화가 자네를 유리한 위치에 세워줄 것이네. 아무런 변화없이 안정감만 추구한다면 이는 곧 발전과 연결될 수 없다네. 자신감 있게 행동하는 모습을 보여야 하네. \n\n#제약조건\n- 반드시 말투는 '~하네'와 같은 노인 말투로 작성할 것\n- 최대한 내용은 3~4문장 정도로 짧게 출력할 것"
      }
    ]


st.header("♍️ 오늘의 운세")

name = st.text_input("이름을 입력하세요")
year = st.text_input("태어난 연도를 입력하세요")
month = st.text_input("태어난 달을 입력하세요")
day = st.text_input("태어난 날을 입력하세요")
button = st.button("운세보기")

if button:
  context.append({"role": "user", "content": year + "년 " + month + "월 " + day + "일"})
  response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = context,
    temperature = 0.7,
    max_tokens = 2000,
    top_p = 1,
    frequency_penalty = 0,
    response_format = {
      "type": "text"
    }
  )

  output = response.choices[0].message.content
  context.append({"role": "assistant", "content": output})

  st.write(name + "님의 운세를 알려주겠네. " + output)



