Building GPT-2-like language model, trained on all novels of the writer Nagib Mahfouz. 
The project goes from A-Z: from collecting the data to building app based on the pretrained model and containerize it.

![nagibGPT in comparison](https://github.com/user-attachments/assets/6ae002a5-17d6-408f-a2e5-a887fc1300ba)

Beginning with the most important 
# 5- Main
web app build with **FastAPI** and **Streamlit** , and of course training , saving and loading models with **pytorch** 
```sh
cd "5- main"
docker compose up
```
or you can make use of back-end (or fron-end) individually, by changing directory to ** 5- main/backend ** and run
```sh 
docker build -t {your_image_name:tag} .

docker run -d  -p host_port:container_port {your_image_name:tag}
```
No docker? no problem. Create env , install requirements and run script. 
**Note** change URL in frontend/ST_GUI.py to localhost, in case not using docker. 

# 4- train
Based on Andrej Karpathy youtube course and [github repo](https://github.com/karpathy/nanoGPT). Just modified to be possible to run on kaggle P100.
I've tested two methods of trainin: train validation datasets , and all in method.
in all-in method i've used all the datased and made generated text as criteria (i'm the judge) 
and also changed some of the optimization (which made traning faster but worse results)

# 3- tokenizer
Two seperate tokenizers for the two different approaches taken in traning (tran valid , and all-in )

rest of the repo is self-explaining.


