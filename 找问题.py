from model.utils import load_json
from config import vocab_path,buckets
vocab = load_json("test/vocab.json")
def label_transform(text,start_type = '<start>',end_type = '<end>',pad_type = '<pad>',max_len = 160):
    text = text.split()
    text = [start_type] + text + [end_type]
    # while len(text)<max_len:
    #     text =text + [pad_type]
    text = [i for i in map(lambda x:vocab[x],text)]
    return text
    # return torch.LongTensor(text)
val=load_json("test/val.json")
for i in val:
    caption=val[i]['caption']
    try:
        text = label_transform(caption)

        # print(text)
    except Exception as ex:
        # print(i)
        print(ex)
