# BLOOM-Linebot
Since GPT-3 API is charged, so I'm curious about if there's open source LLM that is also 'well-pretrained & finetune on question-answering'. 

- Use `BLOOM` to generate chats from AI model
- Create https webhook with `flask` + `ngrok`

### Screenshots
- To continue the text
![](https://i.imgur.com/8ZyInSG.png)
- The bot is socialize! XD
![](https://i.imgur.com/UcEwmiS.png)
- To write high-CTR titles XD...
![](https://i.imgur.com/o5jGQEO.png)
- To write some code
![](https://i.imgur.com/OGYtzzK.png)
- To write some story (Uhh..sorry for mixing `zh_CN` & `zh_TW`)
![](https://i.imgur.com/0La3zYX.png)


### What is BLOOM?
BLOOM is an open-access multilingual language model launched by Huggingface's BigScience Project that contains 176 billion parameters and was trained for 3.5 months on 384 A100–80GB GPUs. 
In this repository we use the lighter version of BLOOM: `bloom-1b1`

### Generate function parameters to play with

- `max_length`
- `num_beams`
- `no_repeat_ngram_size`
- `num_return_sequences`
- `early_stopping`
- `do_sample`
- `temperature`
- `top_k`
- `top_p`

### Use [Ngrok](https://ngrok.com/download) to get a public https url

1. Register on Ngrok to get `authtoken`
https://dashboard.ngrok.com/get-started/setup

2. Download Ngrok
```bash
~$ wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
```

3. Unzip & Install Ngrok
```bash
~$ tar xvzf ngrok-v3-stable-linux-amd64.tgz
```

4. Add your authtoken to the default `ngrok.yml` configuration file
```bash
~$ ./ngrok config add-authtoken <your-authtoken>
```

5. Start a HTTPS tunnel forwarding to your local port
```bash
~$ ./ngrok https 5000
```

### Reference
- [Using different decoding methods for language generation with Transformers](https://huggingface.co/blog/how-to-generate)
- [howarder3/GPT-Linebot-python-flask-on-vercel](https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel)

