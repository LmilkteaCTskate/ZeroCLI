import pyaudio
import wave
import keyboard  # 用于监听键盘事件
import os
import time

# 音频配置
FORMAT = pyaudio.paInt16  # 16位音频格式
CHANNELS = 1              # 单声道
RATE = 44100              # 采样率
CHUNK = 1024              # 每个缓冲区的帧数
RECORDING = False         # 是否正在录音
frames = []               # 用于存储录音数据

# 初始化 PyAudio
audio = pyaudio.PyAudio()

# 录音回调函数
def callback(in_data, frame_count, time_info, status):
    if RECORDING:
        frames.append(in_data)
    return (in_data, pyaudio.paContinue)

# 打开音频流
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    stream_callback=callback)

print("按住空格键开始录音，松开空格键停止录音并保存文件。按 Esc 键退出程序。")


# 监听键盘事件
while True:
    if keyboard.is_pressed('space'):  # 按下空格键
        if not RECORDING:
            print(f"录音中")
            RECORDING = True
            frames = []  # 清空之前的录音数据
    else:  # 松开空格键
        if RECORDING:
            print("录音停止，保存文件中...")
            RECORDING = False

            # 保存录音到文件
            filename = f"output.wav"
            with wave.open(filename, 'wb') as wf:
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(audio.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))
            print(f"文件已保存为 {filename}")

    if keyboard.is_pressed('esc'):  # 按下 Esc 键退出程序
        print("程序退出。")
        break

    time.sleep(0.1)  # 避免 CPU 占用过高

# 关闭音频流
stream.stop_stream()
stream.close()
audio.terminate()