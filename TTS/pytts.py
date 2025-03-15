import pyttsx3
def start(text):
    # 初始化 TTS 引擎
    engine = pyttsx3.init()
    # 设置语速（可选）
    engine.setProperty('rate', 250)  # 设置语速为 150（默认值通常为 200）
    rate = engine.getProperty('rate')  # 获取当前语速

    # 设置音量（可选）
    volume = engine.getProperty('volume')  # 获取当前音量
    engine.setProperty('volume', 1.0)  # 设置音量（范围：0.0 到 1.0）

    # 设置语音（可选）
    voices = engine.getProperty('voices')  # 获取可用设备
    engine.setProperty('voice', 0)  # 选择语音（0 为男性，1 为女性）

    audio_text = text
    engine.say(audio_text)
    #将语音保存
    # engine.save_to_file(audio_text, 'output.mp3')

    # 等待语音播放完成
    engine.runAndWait()
