

# import streamlit as st
# import google.generativeai as genai
# from PIL import Image
# import io
# import json

# # --- Page Configuration (Must be the first Streamlit command) ---
# st.set_page_config(
#     page_title="ReceiptLens AI",
#     page_icon="🧾",
#     layout="centered" # Centered layout for a more focused look
# )

# # --- Custom CSS for the new "Midnight Blue" Professional Dark Theme ---
# st.markdown("""
# <style>
#     /* Set a professional dark theme background */
#     body {
#         background-color: #0E1117;
#         color: #E2E8F0; /* Light gray text for readability */
#     }
#     .main .block-container {
#         max-width: 900px; /* Controls the main content width */
#         padding-top: 2rem;
#         padding-bottom: 2rem;
#         padding-left: 2rem;
#         padding-right: 2rem;
#     }
    
#     /* Hiding the Streamlit branding */
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     header {visibility: hidden;}

#     /* Title and Header styling */
#     h1, h2, h3 {
#         color: #FFFFFF;
#     }
#     h1 {
#         font-size: 2.5rem;
#         font-weight: 700;
#     }
#     h2 {
#         font-size: 1.5rem;
#         font-weight: 600;
#         border-bottom: 2px solid #2d3748;
#         padding-bottom: 0.5rem;
#         margin-top: 2rem;
#         margin-bottom: 1rem;
#     }

#     /* Styling the file uploader */
#     [data-testid="stFileUploader"] {
#         border: 2px dashed #4A5568;
#         border-radius: 0.75rem;
#         padding: 2rem;
#         text-align: center;
#         background-color: #1A202C;
#     }
#     [data-testid="stFileUploader"]:hover {
#         border-color: #3B82F6; /* Blue accent on hover */
#         background-color: #2D3748;
#     }

#     /* New "beautiful" button styling */
#     .stButton>button[kind="primary"] {
#         background-color: #3B82F6;
#         color: white;
#         border: none;
#         padding: 0.75rem 1.5rem;
#         border-radius: 0.5rem;
#         font-weight: 600;
#         box-shadow: 0 4px 14px 0 rgba(0, 0, 0, 0.1);
#         transition: all 0.2s ease;
#     }
#     .stButton>button[kind="primary"]:hover {
#         background-color: #2563EB;
#         transform: translateY(-2px);
#         box-shadow: 0 6px 20px 0 rgba(0, 0, 0, 0.15);
#     }

#     /* Styling for results containers (cards) */
#     [data-testid="stMetric"] {
#         background-color: #1A202C;
#         border-radius: 0.5rem;
#         padding: 1rem;
#         border: 1px solid #2D3748;
#     }
#     [data-testid="stVerticalBlockBorder"] {
#         background-color: #1A202C;
#         border-radius: 0.75rem;
#         padding: 1.5rem;
#         border: 1px solid #2D3748;
#     }
# </style>
# """, unsafe_allow_html=True)


# # --- App Title and Description ---
# st.markdown("""
#     <div style="display: flex; align-items: baseline; gap: 1rem;">
#         <div style="background-color: #3B82F6; color: white; padding: 0.5rem 1rem; border-radius: 0.5rem; font-weight: 600; font-size: 1.25rem;">ReceiptLens</div>
#         <h1 style="margin: 0; padding: 0;">AI</h1>
#     </div>
# """, unsafe_allow_html=True)
# st.markdown("Welcome to the future of expense tracking! Upload a receipt, and let our AI instantly digitize the details for you.")
# st.divider()

# # --- API Key Management ---
# try:
#     genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
# except Exception:
#     st.error("Your Google AI API Key is not configured!")
#     st.info("Please create a `.streamlit/secrets.toml` file with your API key to continue.")
#     st.stop()


# # --- AI Function ---
# def analyze_receipt(image_data):
#     vision_model = genai.GenerativeModel('gemini-1.5-flash-latest')
#     prompt = """
#     You are an expert receipt scanner. Analyze the receipt image and return a JSON object with the following fields:
#     - "merchant": The merchant's name.
#     - "total": The total amount as a float (e.g., 12.50).
#     - "date": The date in "YYYY-MM-DD" format.
#     - "category": A relevant category (e.g., "Dining", "Groceries", "Transport", "Vehicle", "Other").
#     - "items": A list of objects, where each object has "name" (string) and "price" (float).
#     If a value cannot be found, return "N/A" for strings, null for numbers, and an empty list for items.
#     """
#     response = vision_model.generate_content([prompt, image_data])
#     cleaned_json = response.text.strip().replace("```json", "").replace("```", "")
#     return json.loads(cleaned_json)


# # --- Main App UI ---
# st.header("Upload Receipt")
# uploaded_file = st.file_uploader(
#     "Click or drag your receipt image here.",
#     type=["png", "jpg", "jpeg"],
#     label_visibility="collapsed"
# )

# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
    
#     # Display the uploaded image centered
#     st.image(image, caption='Your Uploaded Receipt', width=350)

#     if st.button("Analyze Receipt", use_container_width=True, type="primary"):
#         st.divider()
#         st.header("Analysis Results")
#         with st.spinner("Analyzing receipt... Please wait."):
#             try:
#                 extracted_data = analyze_receipt(image)
#                 st.success("Analysis Complete!")
                
#                 with st.container(border=True):
#                     st.subheader("Summary")
#                     metric_col1, metric_col2 = st.columns(2)
#                     metric_col1.metric("Merchant", extracted_data.get("merchant", "N/A"))
#                     metric_col2.metric("Total Amount", f"${extracted_data.get('total', 0.0):.2f}")
                    
#                     st.markdown(
#                         f"**Date:** `{extracted_data.get('date', 'N/A')}` | "
#                         f"**Category:** `{extracted_data.get('category', 'N/A')}`"
#                     )

#                 items = extracted_data.get("items", [])
#                 if items:
#                     with st.container(border=True):
#                         st.subheader("Itemized List")
#                         st.dataframe(items, use_container_width=True)
#                 else:
#                     st.info("No individual items were found on the receipt.")
#             except Exception as e:
#                 st.error(f"An error occurred during analysis: {e}")
#                 st.warning("Please try a clearer image or check if your API key is valid.")
# else:
#     st.info("Upload an image to get started.")






# import streamlit as st
# import google.generativeai as genai
# from PIL import Image, ImageDraw, ImageFont
# import io
# import json

# # --- Page Configuration (Must be the first Streamlit command) ---
# st.set_page_config(
#     page_title="ReceiptLens AI",
#     page_icon="🧾",
#     layout="centered" # Centered layout for a more focused look
# )

# # --- Custom CSS for the new "Midnight Blue" Professional Dark Theme ---
# st.markdown("""
# <style>
#     /* Set a professional dark theme background */
#     body {
#         background-color: #0E1117;
#         color: #E2E8F0; /* Light gray text for readability */
#     }
#     .main .block-container {
#         max-width: 900px; /* Controls the main content width */
#         padding-top: 2rem;
#         padding-bottom: 2rem;
#         padding-left: 2rem;
#         padding-right: 2rem;
#     }
    
#     /* Hiding the Streamlit branding */
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     header {visibility: hidden;}

#     /* Title and Header styling */
#     h1, h2, h3 {
#         color: #FFFFFF;
#     }
#     h1 {
#         font-size: 2.5rem;
#         font-weight: 700;
#     }
#     h2 {
#         font-size: 1.5rem;
#         font-weight: 600;
#         border-bottom: 2px solid #2d3748;
#         padding-bottom: 0.5rem;
#         margin-top: 2rem;
#         margin-bottom: 1rem;
#     }

#     /* Styling the file uploader */
#     [data-testid="stFileUploader"] {
#         border: 2px dashed #4A5568;
#         border-radius: 0.75rem;
#         padding: 2rem;
#         text-align: center;
#         background-color: #1A202C;
#     }
#     [data-testid="stFileUploader"]:hover {
#         border-color: #3B82F6; /* Blue accent on hover */
#         background-color: #2D3748;
#     }

#     /* New "beautiful" button styling */
#     .stButton>button[kind="primary"] {
#         background-color: #3B82F6;
#         color: white;
#         border: none;
#         padding: 0.75rem 1.5rem;
#         border-radius: 0.5rem;
#         font-weight: 600;
#         box-shadow: 0 4px 14px 0 rgba(0, 0, 0, 0.1);
#         transition: all 0.2s ease;
#     }
#     .stButton>button[kind="primary"]:hover {
#         background-color: #2563EB;
#         transform: translateY(-2px);
#         box-shadow: 0 6px 20px 0 rgba(0, 0, 0, 0.15);
#     }

#     /* Styling for results containers (cards) */
#     [data-testid="stMetric"] {
#         background-color: #1A202C;
#         border-radius: 0.5rem;
#         padding: 1rem;
#         border: 1px solid #2D3748;
#     }
#     [data-testid="stVerticalBlockBorder"] {
#         background-color: #1A202C;
#         border-radius: 0.75rem;
#         padding: 1.5rem;
#         border: 1px solid #2D3748;
#     }
# </style>
# """, unsafe_allow_html=True)


# # --- App Title and Description ---
# st.markdown("""
#     <div style="display: flex; align-items: baseline; gap: 1rem;">
#         <div style="background-color: #3B82F6; color: white; padding: 0.5rem 1rem; border-radius: 0.5rem; font-weight: 600; font-size: 1.25rem;">ReceiptLens</div>
#         <h1 style="margin: 0; padding: 0;">AI</h1>
#     </div>
# """, unsafe_allow_html=True)
# st.markdown("Welcome to the future of expense tracking! Upload a receipt, and let our AI instantly digitize the details for you.")
# st.divider()

# # --- API Key Management ---
# try:
#     genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
# except Exception:
#     st.error("Your Google AI API Key is not configured!")
#     st.info("Please create a `.streamlit/secrets.toml` file with your API key to continue.")
#     st.stop()


# # --- AI Function ---
# def analyze_receipt(image_data):
#     vision_model = genai.GenerativeModel('gemini-1.5-flash-latest')
#     prompt = """
#     You are an expert receipt scanner. Analyze the receipt image and return a JSON object with the following fields:
#     - "merchant": The merchant's name.
#     - "total": The total amount as a float (e.g., 12.50).
#     - "date": The date in "YYYY-MM-DD" format.
#     - "category": A relevant category (e.g., "Dining", "Groceries", "Transport", "Vehicle", "Other").
#     - "items": A list of objects, where each object has "name" (string) and "price" (float).
#     If a value cannot be found, return "N/A" for strings, null for numbers, and an empty list for items.
#     """
#     response = vision_model.generate_content([prompt, image_data])
#     cleaned_json = response.text.strip().replace("```json", "").replace("```", "")
#     return json.loads(cleaned_json)

# # --- Image Generation Function ---
# def create_results_image(data):
#     # --- Configuration ---
#     width, padding = 800, 50
#     bg_color = "#1A202C"
#     text_color = "#E2E8F0"
#     accent_color = "#3B82F6"
#     font_path = "DejaVuSans.ttf" # A common font, may need to adjust for deployment environment

#     # --- Font Loading ---
#     try:
#         font_regular = ImageFont.truetype(font_path, 24)
#         font_bold = ImageFont.truetype(font_path, 32)
#         font_large = ImageFont.truetype(font_path, 48)
#         font_small = ImageFont.truetype(font_path, 20)
#     except IOError:
#         st.warning("Default font not found. Using Streamlit's default font.")
#         font_regular = ImageFont.load_default()
#         font_bold = font_regular
#         font_large = font_regular
#         font_small = font_regular

#     # --- Dynamic Height Calculation ---
#     current_y = padding
#     current_y += 70 # Header
#     current_y += 70 # Merchant and Total
#     current_y += 50 # Date and Category
    
#     items = data.get("items", [])
#     if items:
#         current_y += 60 # Item header
#         current_y += len(items) * 35 # Height for each item
    
#     height = current_y + padding

#     # --- Image Creation ---
#     img = Image.new('RGB', (width, height), color=bg_color)
#     draw = ImageDraw.Draw(img)

#     # --- Drawing Content ---
#     # Header
#     draw.text((padding, padding), "ReceiptLens AI Summary", font=font_bold, fill=accent_color)
#     current_y = padding + 70

#     # Merchant and Total
#     draw.text((padding, current_y), data.get("merchant", "N/A"), font=font_large, fill=text_color)
#     total_text = f"${data.get('total', 0.0):.2f}"
#     total_width = draw.textlength(total_text, font=font_large)
#     draw.text((width - padding - total_width, current_y), total_text, font=font_large, fill=accent_color)
#     current_y += 70

#     # Date and Category
#     draw.text((padding, current_y), f"Date: {data.get('date', 'N/A')}", font=font_regular, fill=text_color)
#     category_text = f"Category: {data.get('category', 'N/A')}"
#     category_width = draw.textlength(category_text, font=font_regular)
#     draw.text((width - padding - category_width, current_y), category_text, font=font_regular, fill=text_color)
#     current_y += 50
    
#     # Itemized List
#     if items:
#         draw.line([(padding, current_y), (width - padding, current_y)], fill="#4A5568", width=2)
#         current_y += 20
#         draw.text((padding, current_y), "Itemized List", font=font_bold, fill=text_color)
#         current_y += 40

#         for item in items:
#             name = item.get("name", "N/A")
#             price = f"${item.get('price', 0.0):.2f}"
#             price_width = draw.textlength(price, font=font_regular)
            
#             draw.text((padding, current_y), name, font=font_small, fill=text_color)
#             draw.text((width - padding - price_width, current_y), price, font=font_small, fill=text_color)
#             current_y += 35

#     # --- Convert to Bytes ---
#     buf = io.BytesIO()
#     img.save(buf, format="PNG")
#     byte_im = buf.getvalue()
#     return byte_im


# # --- Main App UI ---
# st.header("Upload Receipt")
# uploaded_file = st.file_uploader(
#     "Click or drag your receipt image here.",
#     type=["png", "jpg", "jpeg"],
#     label_visibility="collapsed"
# )

# # Store data in session state to persist it
# if 'extracted_data' not in st.session_state:
#     st.session_state.extracted_data = None

# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption='Your Uploaded Receipt', width=350)

#     if st.button("Analyze Receipt", use_container_width=True, type="primary"):
#         with st.spinner("Analyzing receipt... Please wait."):
#             try:
#                 st.session_state.extracted_data = analyze_receipt(image)
#             except Exception as e:
#                 st.session_state.extracted_data = None
#                 st.error(f"An error occurred during analysis: {e}")
#                 st.warning("Please try a clearer image or check if your API key is valid.")

# if st.session_state.extracted_data:
#     st.divider()
#     st.header("Analysis Results")
#     st.success("Analysis Complete!")
    
#     data = st.session_state.extracted_data
#     with st.container(border=True):
#         st.subheader("Summary")
#         metric_col1, metric_col2 = st.columns(2)
#         metric_col1.metric("Merchant", data.get("merchant", "N/A"))
#         metric_col2.metric("Total Amount", f"${data.get('total', 0.0):.2f}")
#         st.markdown(
#             f"**Date:** `{data.get('date', 'N/A')}` | "
#             f"**Category:** `{data.get('category', 'N/A')}`"
#         )

#     items = data.get("items", [])
#     if items:
#         with st.container(border=True):
#             st.subheader("Itemized List")
#             st.dataframe(items, use_container_width=True)
#     else:
#         st.info("No individual items were found on the receipt.")
    
#     # --- Download Button Logic ---
#     st.divider()
#     image_bytes = create_results_image(data)
#     st.download_button(
#         label="Download Results as Image",
#         data=image_bytes,
#         file_name=f"receipt_summary_{data.get('merchant', 'scan')}.png",
#         mime="image/png",
#         use_container_width=True
#     )
# else:
#     if uploaded_file is None:
#         st.info("Upload an image to get started.")









import streamlit as st
import google.generativeai as genai
from PIL import Image, ImageDraw, ImageFont
import io
import json

# --- Page Configuration (Must be the first Streamlit command) ---
st.set_page_config(
    page_title="ReceiptLens AI",
    page_icon="🧾",
    layout="centered" # Centered layout for a more focused look
)

# --- Custom CSS for the new "Midnight Blue" Professional Dark Theme ---
st.markdown("""
<style>
    /* Set a professional dark theme background */
    body {
        background-color: #0E1117;
        color: #E2E8F0; /* Light gray text for readability */
    }
    .main .block-container {
        max-width: 900px; /* Controls the main content width */
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    
    /* Hiding the Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Title and Header styling */
    h1, h2, h3 {
        color: #FFFFFF;
    }
    h1 {
        font-size: 2.5rem;
        font-weight: 700;
    }
    h2 {
        font-size: 1.5rem;
        font-weight: 600;
        border-bottom: 2px solid #2d3748;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }

    /* Styling the file uploader */
    [data-testid="stFileUploader"] {
        border: 2px dashed #4A5568;
        border-radius: 0.75rem;
        padding: 2rem;
        text-align: center;
        background-color: #1A202C;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: #3B82F6; /* Blue accent on hover */
        background-color: #2D3748;
    }

    /* New "beautiful" button styling */
    .stButton>button[kind="primary"] {
        background-color: #3B82F6;
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
        font-weight: 600;
        box-shadow: 0 4px 14px 0 rgba(0, 0, 0, 0.1);
        transition: all 0.2s ease;
    }
    .stButton>button[kind="primary"]:hover {
        background-color: #2563EB;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px 0 rgba(0, 0, 0, 0.15);
    }

    /* Styling for results containers (cards) */
    [data-testid="stMetric"] {
        background-color: #1A202C;
        border-radius: 0.5rem;
        padding: 1rem;
        border: 1px solid #2D3748;
    }
    [data-testid="stVerticalBlockBorder"] {
        background-color: #1A202C;
        border-radius: 0.75rem;
        padding: 1.5rem;
        border: 1px solid #2D3748;
    }
</style>
""", unsafe_allow_html=True)


# --- App Title and Description ---
st.markdown("""
    <div style="display: flex; align-items: baseline; gap: 1rem;">
        <div style="background-color: #3B82F6; color: white; padding: 0.5rem 1rem; border-radius: 0.5rem; font-weight: 600; font-size: 1.25rem;">ReceiptLens</div>
        <h1 style="margin: 0; padding: 0;">AI</h1>
    </div>
""", unsafe_allow_html=True)
st.markdown("Welcome to the future of expense tracking! Upload a receipt, and let our AI instantly digitize the details for you.")
st.divider()

# --- API Key Management ---
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception:
    st.error("Your Google AI API Key is not configured!")
    st.info("Please create a `.streamlit/secrets.toml` file with your API key to continue.")
    st.stop()


# --- AI Function ---
def analyze_receipt(image_data):
    vision_model = genai.GenerativeModel('gemini-1.5-flash-latest')
    prompt = """
    You are an expert receipt scanner. Analyze the receipt image and return a JSON object with the following fields:
    - "merchant": The merchant's name.
    - "total": The total amount as a float (e.g., 12.50).
    - "date": The date in "YYYY-MM-DD" format.
    - "category": A relevant category (e.g., "Dining", "Groceries", "Transport", "Vehicle", "Other").
    - "items": A list of objects, where each object has "name" (string) and "price" (float).
    If a value cannot be found, return "N/A" for strings, null for numbers, and an empty list for items.
    """
    response = vision_model.generate_content([prompt, image_data])
    cleaned_json = response.text.strip().replace("```json", "").replace("```", "")
    return json.loads(cleaned_json)


# --- Image Generation Function ---
def create_results_image(data):
    # --- Configuration ---
    width, padding = 800, 50
    bg_color = "#1A202C"
    text_color = "#E2E8F0"
    accent_color = "#3B82F6"

    # --- Font Loading (Simplified to use built-in default font) ---
    # This removes the need for downloads and eliminates related errors.
    font = ImageFont.load_default()

    # --- Dynamic Height Calculation ---
    current_y = padding
    current_y += 30 # Header
    current_y += 50 # Merchant and Total
    current_y += 30 # Date and Category
    
    items = data.get("items", [])
    if items:
        current_y += 40 # Item header
        current_y += len(items) * 20 # Height for each item
    
    height = current_y + padding

    # --- Image Creation ---
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # --- Drawing Content ---
    # Note: All text will now be the same default size.
    # Header
    draw.text((padding, padding), "ReceiptLens AI Summary", font=font, fill=accent_color)
    current_y = padding + 30

    # Merchant and Total
    draw.text((padding, current_y), data.get("merchant", "N/A"), font=font, fill=text_color)
    total_text = f"${data.get('total', 0.0):.2f}"
    total_width = draw.textlength(total_text, font=font)
    draw.text((width - padding - total_width, current_y), total_text, font=font, fill=accent_color)
    current_y += 50

    # Date and Category
    draw.text((padding, current_y), f"Date: {data.get('date', 'N/A')}", font=font, fill=text_color)
    category_text = f"Category: {data.get('category', 'N/A')}"
    category_width = draw.textlength(category_text, font=font)
    draw.text((width - padding - category_width, current_y), category_text, font=font, fill=text_color)
    current_y += 30
    
    # Itemized List
    if items:
        draw.line([(padding, current_y), (width - padding, current_y)], fill="#4A5568", width=2)
        current_y += 10
        draw.text((padding, current_y), "Itemized List", font=font, fill=text_color)
        current_y += 30

        for item in items:
            name = item.get("name", "N/A")
            price = f"${item.get('price', 0.0):.2f}"
            price_width = draw.textlength(price, font=font)
            
            draw.text((padding, current_y), name, font=font, fill=text_color)
            draw.text((width - padding - price_width, current_y), price, font=font, fill=text_color)
            current_y += 20

    # --- Convert to Bytes ---
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


# --- Main App UI ---
st.header("Upload Receipt")
uploaded_file = st.file_uploader(
    "Click or drag your receipt image here.",
    type=["png", "jpg", "jpeg"],
    label_visibility="collapsed"
)

# Store data in session state to persist it
if 'extracted_data' not in st.session_state:
    st.session_state.extracted_data = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Your Uploaded Receipt', width=350)

    if st.button("Analyze Receipt", use_container_width=True, type="primary"):
        with st.spinner("Analyzing receipt... Please wait."):
            try:
                st.session_state.extracted_data = analyze_receipt(image)
            except Exception as e:
                st.session_state.extracted_data = None
                st.error(f"An error occurred during analysis: {e}")
                st.warning("Please try a clearer image or check if your API key is valid.")

if st.session_state.extracted_data:
    st.divider()
    st.header("Analysis Results")
    st.success("Analysis Complete!")
    
    data = st.session_state.extracted_data
    with st.container(border=True):
        st.subheader("Summary")
        metric_col1, metric_col2 = st.columns(2)
        metric_col1.metric("Merchant", data.get("merchant", "N/A"))
        metric_col2.metric("Total Amount", f"${data.get('total', 0.0):.2f}")
        st.markdown(
            f"**Date:** `{data.get('date', 'N/A')}` | "
            f"**Category:** `{data.get('category', 'N/A')}`"
        )

    items = data.get("items", [])
    if items:
        with st.container(border=True):
            st.subheader("Itemized List")
            st.dataframe(items, use_container_width=True)
    else:
        st.info("No individual items were found on the receipt.")
    
    # --- Download Button Logic ---
    st.divider()
    image_bytes = create_results_image(data)
    st.download_button(
        label="Download Results as Image",
        data=image_bytes,
        file_name=f"receipt_summary_{data.get('merchant', 'scan')}.png",
        mime="image/png",
        use_container_width=True
    )
else:
    if uploaded_file is None:
        st.info("Upload an image to get started.")

