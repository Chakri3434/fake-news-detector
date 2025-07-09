# 📰 Fake News Detection using LSTM

This project uses a deep learning model (LSTM) to classify news articles as **fake** or **real** based on their content.  
Deployed live using **Gradio** and **Hugging Face Spaces**.

## 🚀 Live Demo
👉 [Try the App on Hugging Face](https://huggingface.co/spaces/Chakri34/chakri-fake-news-detector)

## 📂 Dataset
- [Fake and Real News Dataset - Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

## 🧠 Model
- Text tokenization using Keras `Tokenizer`
- LSTM model built with TensorFlow/Keras
- Binary classification (1 = fake, 0 = real)

## 🛠️ Tools & Libraries
- Python
- TensorFlow / Keras
- Pandas, Scikit-learn
- Gradio
- Hugging Face Spaces

## 📦 Files
| File | Description |
|------|-------------|
| `app.py` | Gradio interface for deployment |
| `fake_news_lstm.py` | Model training script |
| `tokenizer.pkl` | Saved tokenizer |
| `lstm_fake_news_model.h5` | Trained LSTM model |
| `requirements.txt` | Dependencies for deployment |

## 📈 Results
- Test Accuracy: ~93%
- Lightweight model, suitable for fast inference

## 🙋‍♂️ Author
- Chakradhar Kalla

