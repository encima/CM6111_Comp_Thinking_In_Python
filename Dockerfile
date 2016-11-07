FROM pandada8/alpine-python:3

USER root 

RUN pip install --upgrade pip
RUN pip install jupyter
RUN apk add git
RUN cd /home 
RUN git clone https://github.com/encima/CM6111_Comp_Thinking_In_Python
RUN cd CM6111_Comp_Thinking_In_Python 
RUN jupyter notebook
