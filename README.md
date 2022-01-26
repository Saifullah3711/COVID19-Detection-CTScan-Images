# COVID19-Detection-CTScan-Images
This model is designed in Keras and trained using CT-Scanned images of lungs to detect COVID19

This is an end to end project. Model is trained on CT-Scanned Images of Healthy and Covid19 infected persons. 

The trained model is saved and deployed in Streamlit. 

All instructions of how the model is trained, the dataset and code is available in Large_CT_Scan_Slice_Images_Tensorflow_Keras_Model___COVID_19.ipynb notebook. 

Run it on GPU especially on Google Colab to train the model fast and get better results. 

## How to run the deployed Model
1: Open the script app.py in VS Code or any other compatible environment
2: Open New Terminal and type there -> streamlit run app.py
3: This will start the server and run the streamlit app on the local browser
4: Do select the image from the Given Images of normal or covid infected
5: Load the images, click on the predict button to show the prediction


![Covidinfectedimg](https://user-images.githubusercontent.com/86683758/151152766-57d707c7-6641-43e7-8e30-7f4d491cb33d.PNG)
![Not Infected With Covid19](https://user-images.githubusercontent.com/86683758/151152787-c9683549-f865-49af-8a86-5d5be1e6e7f8.PNG)
