import streamlit as st

# Define the Streamlit app for the chatbot
def app():
    st.title("Agri Bot - Your Agriculture Assistant")

    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Expanded responses based on more topics in agriculture
    def get_bot_response(user_input):
        user_input = user_input.lower()
        
        # Crop Management
        if 'crop' in user_input:
            return (
                "Crop management involves selecting the right crop varieties, "
                "rotating crops to prevent soil depletion, and timing planting for optimal yield. "
                "Consider factors like soil type, climate, and pest resistance for better results."
            )
        
        # Pest Control
        elif 'pest' in user_input:
            return (
                "Pest control is essential for healthy crops. You can use natural predators, "
                "organic pesticides, or integrated pest management (IPM) techniques. IPM involves "
                "monitoring pest levels, using traps, and applying pesticides only when necessary."
            )
        
        # Weather and Climate
        elif 'weather' in user_input or 'climate' in user_input:
            return (
                "Weather and climate are key for planning agricultural activities. Checking forecasts "
                "and understanding seasonal changes can help you decide on planting, watering, and harvesting times. "
                "In some areas, drought-resistant crops may be beneficial."
            )
        
        # Soil Health
        elif 'soil' in user_input:
            return (
                "Soil health is critical. Regular testing can reveal nutrient levels and pH, which guide fertilization. "
                "Adding organic matter like compost can improve soil structure, water retention, and nutrient availability."
            )
        
        # Fertilization
        elif 'fertilizer' in user_input or 'fertilization' in user_input:
            return (
                "Fertilizers provide essential nutrients like nitrogen, phosphorus, and potassium. Organic fertilizers, "
                "such as compost, improve soil structure, while chemical fertilizers give immediate nutrient boosts. "
                "Use fertilizers based on soil testing results for best outcomes."
            )
        
        # Water Management
        elif 'water' in user_input or 'irrigation' in user_input:
            return (
                "Effective water management involves choosing the right irrigation method, such as drip irrigation "
                "for water conservation, and scheduling watering times. Overwatering can lead to root rot, so check "
                "soil moisture before watering."
            )
        
        # Sustainable Farming
        elif 'sustainable' in user_input or 'sustainability' in user_input:
            return (
                "Sustainable farming practices include crop rotation, minimal tillage, using organic fertilizers, "
                "and integrated pest management. These practices help maintain soil health, conserve water, "
                "and reduce chemical usage, leading to long-term farm viability."
            )
        
        # Climate Change Adaptation
        elif 'climate change' in user_input:
            return (
                "Adaptation to climate change can involve selecting drought-resistant crops, implementing water-saving "
                "irrigation techniques, and diversifying crops to reduce risks. Monitoring climate patterns helps "
                "adjust farming practices to changing conditions."
            )
        
        # Organic Farming
        elif 'organic' in user_input:
            return (
                "Organic farming avoids synthetic chemicals and focuses on natural pest control, compost, and crop rotation. "
                "It promotes biodiversity, improves soil health, and can produce healthier crops, though yields may be lower than conventional methods."
            )
        
        # Harvesting Techniques
        elif 'harvest' in user_input or 'harvesting' in user_input:
            return (
                "Harvesting at the right time ensures the best quality and yield. Timing varies by crop, and using proper tools "
                "reduces damage to the produce. After harvest, storing crops correctly prevents spoilage."
            )
        
        # Plant Diseases
        elif 'disease' in user_input:
            return (
                "Plant diseases like blight, mildew, and rust can reduce crop yield. Preventive measures include using disease-resistant "
                "varieties, crop rotation, and proper spacing. Fungicides may help, but prevention is key."
            )
        
        # Livestock and Animal Care
        elif 'livestock' in user_input or 'animal' in user_input:
            return (
                "Proper care for livestock involves providing balanced nutrition, maintaining clean housing, and regular health checks. "
                "Vaccinations and parasite control are crucial for animal health and productivity."
            )
        
        # General Greeting
        elif 'hello' in user_input or 'hi' in user_input:
            return "Hello! How can I assist you with your agricultural queries today?"
        
        # Default response
        else:
            return "I'm here to help with your agriculture-related questions. Could you ask something more specific?"

    # Get user input and generate response
    if prompt := st.chat_input("Ask me anything about farming!"):
        # Display user message
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate response from the bot
        response = get_bot_response(prompt)
        
        # Display assistant's response
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

