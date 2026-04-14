import streamlit as st

from analysis import analyze_resume

st.set_page_config('Resume Analyzer', page_icon='🕵')

st.title(':red[RESUME ANALYZER USING AI]')

st.header(':blue[AI Powered Resume Analyzer with given JD using AI]')

st.subheader(f'''this page helps you to compare the compare the resume and the given job
             desc and provide ATS score, probability, skillmatch, SWOT analysis''')

st.sidebar.subheader('Drop your resume here')

pdf_doc = st.sidebar.file_uploader('Click here', type = ['pdf'])

st.sidebar.markdown('Designed by Jacob')

st.sidebar.markdown('GitHub: https://github.com/adrianjrosario8/resume_analyzer_Ai.git')

job_desc = st.text_area('Copy and paste the JD here', max_chars = 10000)

submit = st.button('Get Results')

if submit:
    with st.spinner('Loading...'):
        analyze_resume(pdf_doc, job_desc)