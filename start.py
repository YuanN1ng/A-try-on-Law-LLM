from transformers import pipeline
import torch
from pprint import pprint

# 创建pipeline
pipe = pipeline("text-generation",
                model="MaziyarPanahi/calme-3.1-llamaloi-3b",
                device=0,  # 使用 GPU
                torch_dtype=torch.float16,
                max_length= 1000)  # 设置为 FP16

# 用于存储对话历史的变量
conversation_history = []
n=1
# 循环进行交互式对话
while True:
    # 获取用户输入

    user_input = input("You: ")

    if user_input.lower() == "exit":  # 退出对话
        break

    # 将用户输入添加到对话历史中
    conversation_history.append({"role": "user", "content": user_input})


    input_for_model = conversation_history

    # 使用pipeline生成模型回复
    result = pipe(input_for_model)


    # 直接提取生成的文本
    assistant_reply = result[0]['generated_text'][n]['content']

    # 打印模型的纯文本回复
    print(f"Assistant: {assistant_reply}")


    conversation_history.append({"role": "assistant", "content": assistant_reply})
    n+=2