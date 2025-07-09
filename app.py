import gradio as gr
import tensorflow as tf
import pickle
from keras.utils import pad_sequences
model = tf.keras.models.load_model('lstm_fake_news_model.h5')
with open('tokenizer.pkl','rb') as f:
    tokenizer = pickle.load(f)
def predict_news(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq,maxlen=500)
    pred = model.predict(padded)[0][0]
    return '🛑 Fake News' if pred > 0.5 else '✅ Real News'
 
iface = gr.Interface(fn=predict_news,
                     inputs=gr.Textbox(lines=5,placeholder='Enter news here...'),
                     outputs='text',
                     title='📰 Fake News Detector',
                     description='Detects whether a news article is fake or real using an LSTM model.')
iface.launch()