import streamlit as st
import boto3
import json

# ---------- Bedrock AgentCore client ----------
@st.cache_resource
def get_bedrock_client():
    return boto3.client("bedrock-agentcore", region_name="ap-south-1")


AGENT_RUNTIME_ARN = "arn"

client = get_bedrock_client()

# ---------- Streamlit UI ----------
st.set_page_config(page_title="AgentCore QA", page_icon="", layout="centered")

st.title("AgentCore Question Answering")
st.write("Type your question below and get a response from your Bedrock Agent.")

# Text box for question
question = st.text_area(
    "Enter your question:",
    value="Recommend a laptop under 70,000 INR",
    height=100,
)

# Button to submit
if st.button("Ask Agent"):

    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Talking to AgentCore..."):
            
            # Correct payload format
            payload = {
                "prompt": question
            }

            try:
                response = client.invoke_agent_runtime(
                    agentRuntimeArn=AGENT_RUNTIME_ARN,
                    runtimeSessionId="sessionid",
                    payload=json.dumps(payload).encode("utf-8"),
                    qualifier="DEFAULT",
                )

                response_body = response["response"].read()
                response_data = json.loads(response_body)

                # Extract text from nested structure
                answer = response_data["response"]["content"][0]["text"]

                st.subheader("Agent Response")
                st.markdown(answer)

            except Exception as e:
                st.error(f"Error calling AgentCore: {e}")
