from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-5.4-mini",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);
