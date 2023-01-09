import os

from transformers import AutoModelForCausalLM, AutoTokenizer

from api.prompt import Prompt


class BLOOM:
    def __init__(self, remote_model_name: str = "bigscience/bloom-560m"):
        self.prompt = Prompt()
        self.tokenizer = AutoTokenizer.from_pretrained(remote_model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            remote_model_name, pad_token_id=self.tokenizer.eos_token_id
        )
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default=0))
        self.frequency_penalty = float(os.getenv("OPENAI_FREQUENCY_PENALTY", default=0))
        self.presence_penalty = float(os.getenv("OPENAI_PRESENCE_PENALTY", default=0.6))
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", default=240))

    def add_msg(self, text):
        self.prompt.add_msg(text)

    def get_response(self):
        prompt = self.prompt.generate_prompt()
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        # max_length adjust with users input
        max_length = len(input_ids[0])
        greedy_output = self.model.generate(
            input_ids,
            max_length=max_length,
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            max_tokens=self.max_tokens,
        )
        response = self.tokenizer.decode(greedy_output[0], skip_special_tokens=True)
        return response.strip()
