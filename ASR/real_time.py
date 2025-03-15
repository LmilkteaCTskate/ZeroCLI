import pyaudio
from vosk import Model, KaldiRecognizer
import json

# 加载模型
model = Model("asr_model/vosk-model-small-cn-0.22")
rec = KaldiRecognizer(model, 16000)

# 初始化麦克风输入
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

# 实时识别
print("开始录音，按 Ctrl+C 停止...")
def start_recognizer():
    while True:
        # 从麦克风输入数据
        data = stream.read(8192)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if result["text"]:
                    print("识别结果:", result["text"])
                    with open('user_audio_text.txt', 'w',encoding='utf-8') as f:
                        f.write(result["text"])
                    return result["text"]