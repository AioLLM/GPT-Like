class Config:
    vocab_size = None        # будет передан при покупке
    d_model = None
    n_head = None
    num_layers = None
    d_ff = None
    dropout = 0.1
    max_seq_len = 2048
    batch_size = 8

    # Special tokens
    bos_token = "<bos>"
    eos_token = "<eos>"
    pad_token = "<pad>"
    unk_token = "<unk>"
    user_token = "<user>"
    bot_token = "<bot>"
    paragraph_start_token = "<p>"
    paragraph_end_token = "</p>"
    start_token = "<start>"
    end_token = "<end>"

    special_tokens = [
        bos_token, eos_token, pad_token, unk_token,
        user_token, bot_token,
        paragraph_start_token, paragraph_end_token,
        start_token, end_token
    ]