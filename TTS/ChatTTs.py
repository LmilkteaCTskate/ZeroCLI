import ChatTTS

chat = ChatTTS.Chat()
chat.load_models()  # 加载模型（首次运行会自动下载）
texts = ["你好，欢迎使用 ChatTTS！", "Hello, this is a test."]

wavs = chat.infer(texts, use_decoder=True)
chat.save_wavs(wavs, ["output_1.wav", "output_2.wav"])