import os 
import torch 
device ='cuda' if  torch.cuda.is_available() else 'cpu'
from .model_blueprint import GPT , GPTConfig

import __main__
setattr(__main__, "GPTConfig", GPTConfig)


from colorama import Fore , Back
from tokenizers import Tokenizer

PATH = os.path.dirname(__file__)

tokenizer = Tokenizer.from_file(os.path.join(PATH,'tokenizer.json'))

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class Text_generation_model(metaclass=SingletonMeta):
    
    _single_instances ={}
    def __init__(self, writer):
        
        self.writer = writer
        print(f"{Back.GREEN}Creating new writer: {self.writer} {Fore.RESET}{Back.RESET}")    
        for model in os.listdir(os.path.join(PATH,'models')):
            if( model.endswith('pth') and model[:-4] == self.writer)\
            or (model.endswith('pt') and model[:-3] == self.writer):
                
                blueprint = torch.load(os.path.join(PATH,'models',model) , map_location=device ,weights_only=False )

                self.model = GPT(blueprint['model_args'])
                self.model = self.model.to(device)
                self.model.load_state_dict(blueprint['model'])
                break
        else:
            raise FileNotFoundError('There\'s no such model for the writer provided')
    
    def __call__(self , sample, max_tokens , temp = 1 , top_k = 50):
        encoding = tokenizer.encode(sample)
        model_input  = (torch.tensor(encoding.ids, dtype=torch.long, device=device)[None, ...])
        generated_sentence = self.model.generate(model_input, max_tokens,temp,top_k)
        res = []
        for i in generated_sentence:
            res.append(tokenizer.decode(i.tolist()))
        return res
    def __str__(self):
        return f"{self.__class__.__name__} with value {self.writer}"

class Nagib_Mahfouz(Text_generation_model):
    def __init__(self, ):
        super().__init__('nagib_mahfouz')
##### new writers can be appended here 

class Nagib_Mahfouz_All_In(Text_generation_model):
    def __init__(self, ):
        super().__init__('nagib_mahfouz_all_in')