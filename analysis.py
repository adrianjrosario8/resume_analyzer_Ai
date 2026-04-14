import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai

from pdf import extract_text

key = os.getenv('google_api_key')

genai.configure(api_key=key)
model=genai.GenerativeModel('models/gemini-2.5-flash-lite')

def analyze_resume(pdf_doc, job_desc):
    if pdf_doc is not None:
        pdf_text = extract_text(pdf_doc)
        st.write(f'Text extracted successfully')
        
    else:
        st.warning('Error!! Drop the file in pdf format!')
        
    ats_score = model.generate_content(f'''Compare the given pdf {pdf_text}
                                       and given job description {job_desc}
                                       and provide ATS score on scale of 0 to 100
                                       
                                       Generate the results in bullet points (maximum 5 points)''')
    
    probability = model.generate_content(f'''Compare the given pdf {pdf_text}
                                         and given job description {job_desc}
                                         and provide the probability to get short listed for the given job description
                                         on a scale of 0 to 100.
                                         
                                         Generate the results in bullet points (maximum 5 points)''')
    
    goodfit=model.generate_content(f'''Compare the given pdf {pdf_text} with the 
                               job description {job_desc} and provide a score on scale of 0 to 100 
                               indicating how good fit the candidate is for the job. 
                               Give them a tier Based on their ATS score and if low give me suggestions to improve the resume''')
    resume_summary=model.generate_content(f'''Summarize the given pdf {pdf_text}  with the 
                                      job description {job_desc} in 3-4 lines highlighting the key skills and 
                                      experience of the candidate.''')
    skill_match=model.generate_content(f'''Compare the given pdf {pdf_text} with the job description {job_desc} and provide a list of 
                                   skills that match between the resume and the job description. Also provide a list of skills 
                                   that are missing in the resume but are required for the job.''')


    return st.write(f'''ATS Score: {ats_score.text}\n\nProbability of getting shortlisted: {probability.text}\n\nGood Fit: 
                    {goodfit.text}\n\nResume Summary: {resume_summary.text}\n\nSkill Match: {skill_match.text}''')
    
    
    
    
    
    
    
    
    
    
    