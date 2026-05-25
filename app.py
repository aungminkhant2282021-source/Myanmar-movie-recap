import streamlit as st
import asyncio
import edge_tts
import os

st.set_page_config(page_title="Myanmar Movie Recap Voice Generator", page_icon="🎬")
st.title("🎬 Myanmar Movie Recap AI Voice")
st.write("ရုပ်ရှင် Recap အတွက် မြန်မာစာသားများကို အသံဖိုင်အဖြစ် အလွယ်တကူ ပြောင်းလဲပေးနိုင်သော Website")

text_input = st.text_area(
    "Recap စာသား (Script) ကို မြန်မာလို ရိုက်ထည့်ပါ -",
    placeholder="ဥပမာ - ဒီနေ့မှာတော့ လူဆိုးတွေကို တစ်ယောက်တည်း အပြတ်ရှင်းမယ့် ဇာတ်လမ်းလေးကို တင်ဆက်ပေးသွားမှာဖြစ်ပါတယ်။",
    height=250
)

voice_option = "my-MM-ZawZawNeural" 

if st.button("🔊 AI အသံဖိုင် ပြောင်းလဲမည်"):
    if text_input.strip() == "":
        st.warning("ကျေးဇူးပြု၍ စာသားတစ်ခုခု အရင်ရိုက်ထည့်ပေးပါ!")
    else:
        with st.spinner("AI အသံဖိုင်သို့ ပြောင်းလဲနေသည်... ခေတ္တစောင့်ဆိုင်းပါ..."):
            output_filename = "recap_voice.mp3"
            
            async def generate_voice():
                communicate = edge_tts.Communicate(text_input, voice_option)
                await communicate.save(output_filename)

            asyncio.run(generate_voice())
            
            if os.path.exists(output_filename):
                st.success("🎉 အသံဖိုင် ပြောင်းလဲမှု အောင်မြင်ပါသည်!")
                
                audio_file = open(output_filename, 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/mp3')
                
                st.download_button(
                    label="📥 Audio ဖိုင်ကို ရယူရန် နှိပ်ပါ",
                    data=audio_bytes,
                    file_name="myanmar_recap_voice.mp3",
                    mime="audio/mp3"
                )
