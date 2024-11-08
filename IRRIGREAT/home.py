import streamlit as st
from firebase_admin import firestore

def app():
    # Initialize session state for username if not already initialized
    if 'username' not in st.session_state:
        st.session_state.username = ''  # Initialize with a default value (empty string)

    # Initialize session state for Firestore database client if not already initialized
    if 'db' not in st.session_state:
        st.session_state.db = firestore.client()

    db = st.session_state.db  # Use the initialized Firestore client

    # Display appropriate placeholder for post input based on user login status
    ph = ''
    if st.session_state.username == '':
        ph = 'Login to be able to post!!'
        st.write("Please log in to continue.")
        # Input field to set username
        st.session_state.username = st.text_input("Enter your username")
    else:
        ph = 'Post your thought'
    
    # Input text area for new posts
    post = st.text_area(label=' :orange[+ New Post]', placeholder=ph, height=None, max_chars=500)
    
    # Handle post submission
    if st.button('Post', use_container_width=20):
        if post != '':
            # Check if a document for the user already exists
            info = db.collection('Posts').document(st.session_state.username).get()
            
            if info.exists:
                info = info.to_dict()
                if 'Content' in info.keys():
                    # If content exists, append the new post
                    pos = db.collection('Posts').document(st.session_state.username)
                    pos.update({u'Content': firestore.ArrayUnion([u'{}'.format(post)])})
                else:
                    # Create a new content entry
                    data = {"Content": [post], 'Username': st.session_state.username}
                    db.collection('Posts').document(st.session_state.username).set(data)
            else:
                # Create a new document for the user
                data = {"Content": [post], 'Username': st.session_state.username}
                db.collection('Posts').document(st.session_state.username).set(data)
            
            st.success('Post uploaded!!')

    st.header(' :violet[Latest Posts] ')

    # Fetch and display all posts from the Firestore collection
    docs = db.collection('Posts').get()
    for doc in docs:
        d = doc.to_dict()
        try:
            st.markdown("""
                <style>
                .stTextArea [data-baseweb=base-input] [disabled=""]{
                    -webkit-text-fill-color: white;
                }
                </style>
                """, unsafe_allow_html=True)
            
            st.text_area(label=':green[Posted by:] ' + ':orange[{}]'.format(d['Username']), 
                         value=d['Content'][-1], height=20, disabled=True)
        except:
            pass
