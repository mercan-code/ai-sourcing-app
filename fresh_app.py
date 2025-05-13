import streamlit as st
import openai

st.set_page_config(page_title="GPT Destekli Sourcing", layout="centered")

st.title("🤖 GPT Destekli Sourcing Değerlendirme Aracı")

openai.api_key = st.text_input("🔑 OpenAI API Anahtarınızı Girin", type="password")

job_desc = st.text_area("📌 Pozisyon Tanımı", height=200)
profile = st.text_area("👤 Aday Profil Bilgisi", height=200)

if st.button("🔍 Adayı Değerlendir"):
    if openai.api_key and job_desc and profile:
        with st.spinner("GPT analiz ediyor..."):
            try:
                prompt = f"""
You are an AI recruiter.

Job Description:
{job_desc}

Candidate Profile:
{profile}

Evaluate if this candidate is a good fit for the role above. Give a score from 1 to 10 and explain the reasoning. Highlight strengths and weaknesses.
"""
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.4,
                )
                st.markdown("### 🧠 GPT Değerlendirmesi")
                st.success(response.choices[0].message.content)

            except Exception as e:
                st.error(f"Hata oluştu: {str(e)}")
    else:
        st.warning("Lütfen tüm alanları doldurun ve API anahtarınızı girin.")
