import tensorflow as tf

import gradio as gr

import os


model_path = "/content/drive/MyDrive/Model/"
def load_model(name: str):
	try:
		model = tf.keras.models.load_model(model_path+name)
	except Exception as e:
		raise gr.Error(e)

	return model

def list_model():
	model_list = []
	for model in os.listdir(model_path):
		if model.endswith(".h5"):
			model_list.append(model)
	return model_list

def save_model(model, name: str):
	try:
		model.save(model_path+name)
	except Exception as e:
		raise gr.Error(e)