# -*- coding: utf-8 -*-
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 一、初始化配置
MODEL_PATH = r"D:\ASR_LLX_TTS\Demo\tts_model\paraphrase-TinyBERT-L6-v2"  # 替换为实际模型路径

# 二、示例数据集（实际使用时替换为自己的标注数据）
# 标签说明：0=负面，1=正面
texts = [
    "这个产品完全达不到预期效果",  # 0
    "服务态度差到让人无法接受",    # 0
    "操作界面非常人性化设计",      # 1
    "性价比超高值得推荐",          # 1
    "物流速度慢得离谱",           # 0
    "功能强大超出我的想象",        # 1
    "客服回应迟钝不专业",         # 0
    "使用体验简直完美无缺",       # 1
]
labels = [0, 0, 1, 1, 0, 1, 0, 1]

# 三、加载本地模型
model = SentenceTransformer(MODEL_PATH)

# 四、特征提取
# print("正在生成句子嵌入...")
embeddings = model.encode(texts, convert_to_numpy=True)

# 五、数据集拆分
X_train, X_test, y_train, y_test = train_test_split(
    embeddings, labels, test_size=0.25, random_state=42
)

# 六、训练分类器
# print("\n训练分类器...")
clf = LogisticRegression(class_weight='balanced')
clf.fit(X_train, y_train)

# 七、评估模型
y_pred = clf.predict(X_test)
# print("\n评估报告：")
# print(classification_report(y_test, y_pred, target_names=["负面", "正面"]))

# 八、推理使用
def predict_emotion(text):
    emb = model.encode([text])
    proba = clf.predict_proba(emb)[0]
    prediction = clf.predict(emb)[0]
    return {
        "text": text,
        "预测结果": "正面" if prediction == 1 else "负面",
        "负面概率": f"{proba[0]:.2%}",
        "正面概率": f"{proba[1]:.2%}"
    }

# 测试推理
# test_s = [
#     "这次购物经历还算满意",
#     "产品质量差强人意",
#     "这是我用过最烂的APP"
# ]

# print("\n推理演示：")
def test_samples(user_text):
    # for sample in user_text:
        result = predict_emotion(user_text)
        # print(f"输入：{result['text']}")
        print(f"结果：{result['预测结果']} (负:{result['负面概率']}, 正:{result['正面概率']})\n")
        #将情绪识别结果写入文件
        with open('user_bert.txt','w') as f:
                f.write(result['预测结果'])
# test_samples(test_s)