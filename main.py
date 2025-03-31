from crewai import Agent,Task, Crew, LLM
from crewai_tools import SerperDevTool
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Content Research & Writer",layout = "wide")

st.title("Content research and writer, powered by CrewAI")
st.markdown("Generate blog posts about any topic using AI Agents.")

with st.sidebar:
  st.header("Content Settings")

  topic = st.text_area(
      "Enter your topic",
      height = 100,
      placeholder = "Enter The topic"
  )

  st.markdown("### LLM Settings")
  temperature = st.slider("Temperature",0.0,1.0,0.7)

  st.markdown("---")

  generate_button = st.button("Generate Content", type="primary",use_container_width=True)

  with st.expander("How to use"):
    st.markdown("""
    1. Enter your desired content topic
    2. Play with the temperature
    3. Click 'Generate Content' to start
    4. Wait for AI to generate your article
    5. Download the result as a markdown file
    """)


  def generate_content(topic):
    # entire piece of code has been written same as before just the kickoff is written in return statement
    return crew.kickoff(inputs = {"topic":topic})

  # Main content area

  if generate_button:
    with st.spinner('Generating content ... This may take a while .'):
      try:
        result = generate_content(topic)
        st.markdown(result)

        # add download button

        st.download_button(
            label = "Download Content",
            data = result.raw,
            file_name = f"{topic.lower().replace(' ','_')}_article.md",
            mime = "text/markdown"
        )
      except Exception as e:
        st.error(f"An error occurred: {str(e)}")

  # Footer
  st.markdown("---")
  st.markdown("Built with crewAI, Streamlit")
