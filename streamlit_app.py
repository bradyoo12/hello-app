# https://www.youtube.com/watch?v=HKoOBiAaHGg

import streamlit as st
import vertexai
from vertexai.language_models import TextGenerationModel
# st.write('Hello world!')

vertexai.init(project="mycloudml-337117", location="us-central1")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 256,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison@001")
response = model.predict(
    """is streamlit a framework?""",
    **parameters
)
st.write(f"{response.text}")
