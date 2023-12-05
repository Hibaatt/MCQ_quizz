#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import openai  
openai.api_key = "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"

def generate_question(topic):
    prompt = f"Generate a multiple-choice question about {topic}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def main():
    st.title("MCQ Quiz App")
    
    # Get user input for quiz topic
    topic = st.text_input("Enter your preferred quiz topic:")
    
    # Generate a question based on the user's topic
    question = generate_question(topic)
    
    st.write(f"Question: {question}")

if __name__ == "__main__":
    main()
