import streamlit as st
import groq

if "messages" not in st.session_state:
    st.session_state.messages = []

cliente = groq.Groq(api_key = "CHAVE_GROQ_AQUI")

prompt = st.chat_input()
if prompt:
    st.session_state.messages.append({"role" : "user", "content" : prompt})
    completion = cliente.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages = st.session_state.messages,
        temperature=1,
        max_completion_tokens=8192,
        top_p=1,
        reasoning_effort="medium",
        stream=True,
        stop=None
    )

    str = ""
    for chunk in completion:
        str += chunk.choices[0].delta.content or ""
    
    st.session_state.messages.append({"role" : "assistant", "content" : str})
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            st.markdown("# IA disse:")
        else:
            st.markdown("# Você disse:")

        st.markdown(message["content"])