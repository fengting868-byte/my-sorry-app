import streamlit as st
from openai import OpenAI

# 页面配置
st.set_page_config(page_title="致女朋友的道歉信", page_icon="💖", layout="centered")

st.title("💖 又不小心惹闵蝶生气了")
st.write("对不起，我错了。以下是我用AI为你定制的专属道歉：")

# 侧边栏
with st.sidebar:
    st.header("⚙️ 设置")
    # 直接从系统保险箱里拿 Key，不需要用户输入
    api_key = st.secrets["DEEPSEEK_API_KEY"]
    reason = st.text_area("付瑞方为什么惹你生气了？（填一句就行，比如：打游戏没回消息）")

# 主界面
if st.button("生成道歉信并请求原谅"):
    if not reason:
        st.warning("请先在左边输入 API Key 和 生气原因！")
    else:
        with st.spinner("正在诚恳反思中..."):
            try:
                client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
                
                # 给 AI 设定一个极度深情的身份
                system_prompt = "你是一个极其深情、擅长写情书的男朋友。请用极其真诚、温柔、带点小幽默和撒娇的语气，写一封大约300字的道歉信。一定要深刻反省，并保证绝不再犯。"
                
                response = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"我惹女朋友生气的原因是：{reason}"}
                    ],
                    stream=True
                )
                
                st.success("反思完毕，请大人过目：")
                
                # 打字机效果展示
                full_response = st.write_stream(response)
                
                # 魔法时刻：满屏下气球！(Streamlit的特效)
                st.balloons()
                st.snow()
                
            except Exception as e:
                st.error(f"出错了：{e}")
