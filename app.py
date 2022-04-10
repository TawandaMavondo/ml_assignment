from grpc import Status
import search_object
from time import time
import streamlit as st
import io
import time
temp_folder = './temp/'
active = False
st.title('Video Object Detection')
st.subheader('Please Upload the video which you want to detect objects on.')

with st.sidebar:
    st.header('Group Members')
    st.write('Tawanda Godbless Mavondo R204447C')
    st.write("Eugenia Mavhura R202071N")
# Main application File


video_file = st.file_uploader(label="Video", type=['mp4'])


if video_file is not None:
    active = True
    st.video(video_file.read(), format=video_file.type)
    data_bytes = io.BytesIO(video_file.getvalue())
    file_dir = temp_folder + "upload.mp4"
    with open(file_dir, 'wb') as output:
        output.write(data_bytes.read())
    print("File saved")     
    output.close()

if active:
    object_str = st.text_input("Please enter object you need to search",
                               placeholder="car, bike etc")

    def on_click():
        status, label, frame = search_object.search(object_str)
        if status:
            st.image(frame)
        else:
            st.text("Unable To find Object in the video ")

    if st.button("Search"):
        on_click()
    with st.spinner("Splitting and Analysing Frames"):
        time.sleep(1)


    
    
