from collections import namedtuple
import torch
from common.trainer import to_cuda


@torch.no_grad()
def do_validation(net, val_loader, metrics, label_index_in_batch):
    net.eval()
    metrics.reset()
    for nbatch, batch in enumerate(val_loader):
        batch = to_cuda(batch)
        # TODO: this should not be like this
        tokenized_answer = batch[label_index_in_batch]
        # for mlp
        # datas = [batch[i] for i in range(len(batch)) if i != label_index_in_batch % len(batch)]
        # outputs = net(*datas)
        # for decoder
        outputs = net(*batch)
        outputs.update({'tokenized_answer': tokenized_answer})
        metrics.update(outputs)

