import streamlit as st

def app():
    st.subheader('Trending Articles in Agriculture Business')

    # Sample trending articles with user information
    articles = [
        {
            "title": "The Future of Sustainable Farming",
            "author": "Jane Doe",
            "date": "2024-10-01",
            "content": (
                "Sustainable farming practices are essential for preserving our planet. "
                "Innovations such as precision agriculture, organic farming, and agroforestry "
                "are paving the way for more efficient food production while protecting the environment."
            )
        },
        {
            "title": "Emerging Technologies in Agriculture",
            "author": "John Smith",
            "date": "2024-09-15",
            "content": (
                "Technology is transforming the agricultural landscape. Drones, IoT devices, and "
                "AI are being utilized to enhance crop yields, monitor soil health, and manage resources."
            )
        },
        {
            "title": "Market Trends in Organic Produce",
            "author": "Emily Johnson",
            "date": "2024-08-20",
            "content": (
                "The demand for organic produce continues to rise. Farmers are adapting to this trend "
                "by increasing organic certifications and expanding their product lines to meet consumer expectations."
            )
        },
        {
            "title": "The Role of Agri-Tech Startups",
            "author": "Michael Brown",
            "date": "2024-07-10",
            "content": (
                "Agri-tech startups are at the forefront of agricultural innovation. They provide solutions "
                "for everything from pest management to supply chain logistics, ensuring farmers can work more effectively."
            )
        }
    ]

    # Display the articles as if they are user posts
    for article in articles:
        st.markdown(f"### {article['title']}")
        st.markdown(f"**Posted by:** {article['author']} | **Date:** {article['date']}")
        st.write(article['content'])
        st.markdown("---")  # Separator for better readability

    # Placeholder for potential future features
    st.text_area(label=' ', value='Stay tuned for more articles and insights on agriculture!', height=100, disabled=True)

