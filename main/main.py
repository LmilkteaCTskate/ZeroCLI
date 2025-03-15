import sys
sys.path.append('D:\ASR_LLX_TTS\Demo')
from ollama import Client
import os

from TTS import pytts

client = Client(
    host='http://localhost:11434',
    headers={'x-some-header': 'some-value'}
)

def text_to_model(user_input):
        #情绪识别
        # from Bert import text_bert
        # text_bert.test_samples(user_input)

        response = client.chat(model=model_name, messages=[
            {
                'role': 'user',
                'content': user_input,
            },
        ],stream=True,)

        model_text = ''
        
        for chunk in response:
            #将模型回复保存到model_text中
            model_text += chunk['message']['content']
            #循环内流式输出(用户可见)
            print(chunk['message']['content'],end='',flush=True)
            with open('model_text.txt', 'w',encoding='utf-8') as f:
                f.write(model_text)
        print("\n")
        print("ctrl+c退出")
        #语音合成
        # pytts.start(model_text)
#文本输入
def test_talk():
    while True:
        user_input = input("输入问题:")
        text_to_model(user_input)
#语音输入
def asr_talk():
    while True:
        from ASR import real_time
        user_input = real_time.start_recognizer()

        text_to_model(user_input)
        print("继续录音")

with open('model.txt','r',encoding='utf-8') as f:
    model_name = f.read()
print("你对话的模型为"+model_name)
select_input = input("1为文本对话\n2为语音转文本对话\n3为设置界面\n请输入:")
if select_input == '1':
    test_talk()
elif select_input == '2':
    asr_talk()
elif select_input == '3':
    from main.setting import main
    main()