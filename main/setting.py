import subprocess

def save_ollama_models():
    try:
        # 调用 `ollama list` 命令
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            check=True
        )

        # 解析输出
        models = []
        lines = result.stdout.strip().split("\n")  # 按行分割
        if len(lines) > 1:  # 跳过表头行
            for line in lines[1:]:  # 从第二行开始遍历
                columns = line.split()  # 按空格分割列
                if columns:  # 忽略空行
                    model_name = columns[0]  # 第一列为模型名称（如 "llama3:latest"）
                    models.append(model_name)

        # 将模型名称保存到文件
        with open("ollama_models.txt", "w") as f:
            for model in models:
                f.write(f"{model}\n")

        print(f"已保存 {len(models)} 个模型名称到 ollama_models.txt")

    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {e.stderr}")
#设置界面
def main():

    #获取本地ollama模型列表,默认ollama有两个模型
    model_name_list = []
    with open('ollama_models.txt','r',encoding='utf-8') as f:
        for line in f:
            model_name_list.append(line.strip())

    print("----------------------------------")
    print("设置界面")
    print("按1选择LLM模型\n"+"按2选择TTS模型\n"+"按3更新本地模型")
    print(f"你现有的模型列表为:{model_name_list}")
    print("----------------------------------")

    user_input = input("输入选择:")
    if user_input == "1":
        model_name = model_select(model_name_list)
        print("已选择LLM模型为"+model_name)
        with open("model.txt","w") as f:
             f.write(model_name)


    elif user_input == "2":
        model_name = model_select(model_name_list)
        print("已选择TTS模型为"+model_name)
        with open("main/tts.txt","w") as f:
             f.write(model_name)

    elif user_input == "3":
        save_ollama_models()
        main()


def add_model():
     #在本地模型列表中添加新模型
    print("添加模型界面")
    add_model_name = input("输入模型名称:")
    return add_model_name

def model_select(model_name_list):
        
        print("----------------------------------")
        print("LLM模型选择界面,输入exit返回主界面")

        for i in range(len(model_name_list)):
            print(f"按{i}选择:{model_name_list[i]}")

        print("----------------------------------")

        select_model = input("选择对话模型:")
        
        print("----------------------------------")

        #根据用户输入选择模型
        if select_model == "exit":
            return "exit"
        else:
            return model_name_list[int(select_model)]
    
if __name__ == "__main__":
    main()