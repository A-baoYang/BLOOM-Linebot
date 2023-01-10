from transformers import AutoModelForCausalLM, AutoTokenizer


class BLOOM:
    def __init__(self, remote_model_name: str = "bigscience/bloom-1b1"):
        self.tokenizer = AutoTokenizer.from_pretrained(remote_model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            remote_model_name, pad_token_id=self.tokenizer.eos_token_id
        )

    def get_response(self, text):
        input_ids = self.tokenizer.encode(text, return_tensors="pt")
        greedy_output = self.model.generate(
            input_ids,
            max_length=1024,
            # num_beams=5,
            # no_repeat_ngram_size=2,
            # num_return_sequences=3,
            # early_stopping=True,
            do_sample=True,
            temperature=0.7,
            top_k=0,
            # top_p=0.92
        )
        response = self.tokenizer.decode(greedy_output[0], skip_special_tokens=True)
        return response.strip()
